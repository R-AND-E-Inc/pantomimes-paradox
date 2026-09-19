#!/usr/bin/env python3
"""Build deterministic release and package manifests; never resolve or execute work."""

import argparse
import os
from pathlib import Path
import stat
import sys
import tempfile

sys.dont_write_bytecode = True
from resolve_workflow import (  # noqa: E402
    ACCEPTED_PLUGINS, BOOTSTRAP, LEGACY, LEGACY_SKILLS, PLUGIN, SCHEMA, SKILLS,
    WorkflowError, canonical_json, check_release, checked_root, fail,
    parse_json, read_file, safe_file, sha256, validate_catalog, validate_manifest,
)


def collect_files(release_root):
    files = {}
    for directory, dirs, names in os.walk(release_root, followlinks=False):
        for name in dirs + names:
            path = Path(directory) / name
            info = path.lstat()
            if stat.S_ISLNK(info.st_mode):
                fail("unsafe_path", "A release must not contain symlinks: " + str(path))
            if not (stat.S_ISREG(info.st_mode) or stat.S_ISDIR(info.st_mode)):
                fail("unsafe_path", "A release must contain regular files and directories only")
        for name in sorted(names):
            path = Path(directory) / name
            relative = path.relative_to(release_root).as_posix()
            if relative == "manifest.json":
                continue
            files[relative] = sha256(read_file(path))
    return files


def skill_mapping(release, overrides):
    expected = LEGACY_SKILLS if release == LEGACY else SKILLS
    if overrides:
        mapping = {}
        for item in overrides:
            skill, separator, paths = item.partition("=")
            if not separator or skill in mapping:
                fail("invalid_mapping", "Use unique --skill name=path[,path] arguments")
            mapping[skill] = paths.split(",")
        return mapping
    if release == LEGACY:
        return {skill: ["skills/" + skill + "/SKILL.md"] for skill in expected}
    return {skill: ["core.md", "stages/" + skill.removeprefix("work-") + ".md"] for skill in expected}


def atomic_write(path, data):
    descriptor, temporary = tempfile.mkstemp(prefix=".manifest-", dir=str(path.parent))
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def build(plugin_root, release, overrides=(), replace_unreleased=False, check=False):
    check_release(release, allow_legacy=True)
    plugin_root = checked_root(plugin_root, "Plugin root")
    # Check the entire directory chain before using it for reads or writes.
    release_relative = "playbooks/" + release
    for relative in ("playbooks", release_relative):
        path = plugin_root / relative
        if path.is_symlink() or not path.is_dir():
            fail("unsafe_path", "Expected an existing release directory without symlinks: " + str(path))
    release_root = plugin_root / release_relative
    manifest_path = safe_file(plugin_root, release_relative + "/manifest.json", optional=True)
    existing = read_file(manifest_path) if manifest_path else None
    # A release published under the process's former name keeps that identity so its
    # pinned manifest bytes never change; only new releases carry the current name.
    identity = PLUGIN
    if existing is not None:
        recorded = parse_json(existing, "release manifest").get("plugin")
        if recorded in ACCEPTED_PLUGINS:
            identity = recorded
    manifest = {
        "schema": SCHEMA, "plugin": identity, "release": release,
        "files": collect_files(release_root), "skills": skill_mapping(release, overrides),
    }
    validate_manifest(manifest, release)
    manifest_bytes = canonical_json(manifest)
    if existing is not None and existing != manifest_bytes and not replace_unreleased:
        fail("immutable_release", "Release content changed; use a new release, or --replace-unreleased only in staging")
    catalog_path = safe_file(plugin_root, "playbooks/manifest.json", optional=True)
    if catalog_path:
        catalog = parse_json(read_file(catalog_path), "package playbook manifest")
        validate_catalog(catalog)
    else:
        catalog = {"schema": SCHEMA, "plugin": PLUGIN, "bootstrap": BOOTSTRAP, "releases": {}}
    selected = catalog["releases"].get(release)
    if selected and selected["manifest_sha256"] != sha256(manifest_bytes) and not replace_unreleased:
        fail("immutable_release", "Generated content differs from the cataloged release; a missing manifest does not remove its pin")
    for other_release, entry in catalog["releases"].items():
        if other_release == release:
            continue
        other_path = safe_file(plugin_root, "playbooks/" + other_release + "/manifest.json")
        if sha256(read_file(other_path)) != entry["manifest_sha256"]:
            fail("integrity_mismatch", "An existing release manifest changed: " + other_release)
    catalog["releases"][release] = {"manifest_sha256": sha256(manifest_bytes)}
    validate_catalog(catalog)
    catalog_bytes = canonical_json(catalog)
    if check:
        if existing != manifest_bytes or catalog_path is None or read_file(catalog_path) != catalog_bytes:
            fail("outdated_manifests", "Generated manifests differ from the files on disk")
    else:
        if existing != manifest_bytes:
            atomic_write(release_root / "manifest.json", manifest_bytes)
        if catalog_path is None or read_file(catalog_path) != catalog_bytes:
            atomic_write(plugin_root / "playbooks/manifest.json", catalog_bytes)
    return {"status": "verified" if check else "built", "release": release,
            "manifest_sha256": sha256(manifest_bytes), "files": len(manifest["files"])}


def check_all(plugin_root):
    plugin_root = checked_root(plugin_root, "Plugin root")
    catalog_path = safe_file(plugin_root, "playbooks/manifest.json")
    catalog = parse_json(read_file(catalog_path), "package playbook manifest")
    validate_catalog(catalog)
    directories = set()
    for path in (plugin_root / "playbooks").iterdir():
        if path.is_symlink():
            fail("unsafe_path", "Playbooks must not contain symlinks")
        if path.is_dir():
            directories.add(path.name)
        elif path.name != "manifest.json":
            fail("untracked_payload", "Unexpected file in playbooks: " + path.name)
    if directories != set(catalog["releases"]):
        fail("untracked_release", "Release directories must exactly match the package manifest")
    if not {LEGACY, BOOTSTRAP}.issubset(directories):
        fail("missing_release", "A complete package must contain legacy and bootstrap releases")
    results = []
    for release in sorted(directories):
        path = safe_file(plugin_root, "playbooks/" + release + "/manifest.json")
        manifest = parse_json(read_file(path), "release manifest")
        validate_manifest(manifest, release)
        overrides = [skill + "=" + ",".join(paths) for skill, paths in manifest["skills"].items()]
        results.append(build(plugin_root, release, overrides=overrides, check=True))
    return {"status": "verified", "releases": results}


def main(argv=None):
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin-root", default=str(Path(__file__).absolute().parent.parent))
    parser.add_argument("--release")
    parser.add_argument("--skill", action="append", default=[], help="Complete explicit mapping: name=path[,path]")
    parser.add_argument("--replace-unreleased", action="store_true", help="Rebuild changed staging content only")
    parser.add_argument("--check", action="store_true", help="Compare without writing")
    args = parser.parse_args(argv)
    if not args.release and (not args.check or args.skill or args.replace_unreleased):
        parser.error("--release is required unless using --check alone")
    try:
        result = (build(args.plugin_root, args.release, args.skill, args.replace_unreleased, args.check)
                  if args.release else check_all(args.plugin_root))
    except (WorkflowError, OSError) as error:
        print(json.dumps({"status": "error", "code": getattr(error, "code", "filesystem_error"), "message": str(error)}))
        return 1
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
