#!/usr/bin/env python3
"""Read-only selection and integrity checking for The Pantomime's Paradox playbooks."""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
from urllib.parse import urlsplit


PLUGIN = "pantomimes-paradox"
# Personal Workflows was the name of this process before it became The Pantomime's Paradox.
# Its releases, manifests and adoption blocks remain valid so pinned projects keep resolving.
LEGACY_PLUGIN = "personal-workflows"
ACCEPTED_PLUGINS = (PLUGIN, LEGACY_PLUGIN)
SCHEMA = 1
LEGACY = "legacy-personal-workflows"
BOOTSTRAP = "2.2.0"
MARKERS = tuple(("<!-- " + name + ":begin -->", "<!-- " + name + ":end -->") for name in ACCEPTED_PLUGINS)
BEGIN, END = MARKERS[0]
LEGACY_SKILLS = (
    "work-steps", "work-plan", "work-resume", "work-review",
    "work-evidence", "work-flow-check", "work-closeout",
)
BOOTSTRAP_SKILLS = ("work-start", "work-adopt")
SKILLS = LEGACY_SKILLS + BOOTSTRAP_SKILLS + ("work-deliver",)
RELEASE_PATTERN = re.compile(
    r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"
    r"(?:-[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?"
    r"(?:\+[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?"
)
HASH_PATTERN = re.compile(r"[0-9a-f]{64}")


class WorkflowError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def fail(code, message):
    raise WorkflowError(code, message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            fail("invalid_json", "Duplicate JSON key: " + key)
        result[key] = value
    return result


def invalid_constant(value):
    fail("invalid_json", "Non-finite JSON number: " + value)


def parse_json(raw, label):
    try:
        return json.loads(raw, object_pairs_hook=unique_object,
                          parse_constant=invalid_constant)
    except (ValueError, UnicodeError) as error:
        fail("invalid_json", "Cannot parse " + label + ": " + str(error))


def canonical_json(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def check_hash(value, label):
    if not isinstance(value, str) or not HASH_PATTERN.fullmatch(value):
        fail("invalid_manifest", label + " must be a lowercase SHA-256 digest")


def check_release(value, allow_legacy=False):
    if allow_legacy and value == LEGACY:
        return
    if not isinstance(value, str) or not RELEASE_PATTERN.fullmatch(value):
        fail("invalid_release", "Expected an exact release, not a range or path")


def object_fields(value, fields, label):
    if not isinstance(value, dict) or set(value) != set(fields):
        fail("invalid_schema", label + " must contain exactly: " + ", ".join(sorted(fields)))


def check_header(value, label, plugins=ACCEPTED_PLUGINS):
    if type(value["schema"]) is not int or value["schema"] != SCHEMA:
        fail("unsupported_schema", label + " uses an unsupported schema")
    if value["plugin"] not in plugins:
        fail("invalid_schema", label + " is not for " + PLUGIN)


def checked_root(value, label):
    # Resolve platform aliases such as /tmp, but reject a symlink supplied as the root.
    root = Path(os.path.abspath(os.path.expanduser(str(value))))
    try:
        info = root.lstat()
    except OSError as error:
        fail("missing_root", label + " is unavailable: " + str(error))
    if stat.S_ISLNK(info.st_mode) or not stat.S_ISDIR(info.st_mode):
        fail("unsafe_path", label + " must be a directory, not a symlink")
    return root.resolve(strict=True)


def checked_relative(value):
    if not isinstance(value, str) or not value or "\\" in value or ":" in value or "\x00" in value:
        fail("unsafe_path", "Invalid relative payload path")
    path = PurePosixPath(value)
    if path.is_absolute() or str(path) != value or any(part in (".", "..") for part in path.parts):
        fail("unsafe_path", "Payload paths must stay inside their release directory: " + value)
    if not path.parts:
        fail("unsafe_path", "Empty payload path")
    return path


def safe_file(root, relative, optional=False):
    parts = checked_relative(relative).parts
    current = root
    for index, part in enumerate(parts):
        current = current / part
        try:
            info = current.lstat()
        except FileNotFoundError:
            if optional:
                return None
            fail("missing_file", "Required file is unavailable: " + str(current))
        except OSError as error:
            fail("unreadable_file", "Cannot inspect file: " + str(error))
        if stat.S_ISLNK(info.st_mode):
            fail("unsafe_path", "Symlinks are not accepted: " + str(current))
        if index < len(parts) - 1:
            if not stat.S_ISDIR(info.st_mode):
                fail("unsafe_path", "A path component is not a directory: " + str(current))
        elif not stat.S_ISREG(info.st_mode):
            fail("unsafe_path", "Expected a regular file: " + str(current))
    return current


def read_file(path):
    try:
        return path.read_bytes()
    except OSError as error:
        fail("unreadable_file", "Cannot read file: " + str(error))


def read_profile(project_root):
    path = safe_file(project_root, "docs/OPERATING.md", optional=True)
    if path is None:
        return None
    try:
        text = read_file(path).decode("utf-8")
    except UnicodeError:
        fail("invalid_profile", "docs/OPERATING.md must be UTF-8")
    counts = [(text.count(begin), text.count(end)) for begin, end in MARKERS]
    if not any(count for pair in counts for count in pair):
        return None
    present = [pair for pair, count in zip(MARKERS, counts) if count != (0, 0)]
    if len(present) != 1 or counts[MARKERS.index(present[0])] != (1, 1):
        fail("invalid_profile", "Expected one complete, ordered adoption metadata block")
    begin, end = present[0]
    if text.index(end) < text.index(begin):
        fail("invalid_profile", "Expected one complete, ordered adoption metadata block")
    raw = text.split(begin, 1)[1].split(end, 1)[0].strip()
    profile = parse_json(raw, "workflow adoption metadata")
    object_fields(profile, ("schema", "plugin", "release", "source", "source_commit", "manifest_sha256"), "Adoption metadata")
    check_header(profile, "Adoption metadata")
    check_release(profile["release"])
    check_hash(profile["manifest_sha256"], "manifest_sha256")
    commit = profile["source_commit"]
    if not isinstance(commit, str) or not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", commit):
        fail("invalid_profile", "source_commit must be a complete lowercase Git commit identity")
    source = profile["source"]
    if not isinstance(source, str):
        fail("invalid_profile", "source must be an HTTPS repository URL")
    try:
        parsed = urlsplit(source)
        valid_source = (parsed.scheme == "https" and bool(parsed.hostname)
                        and not parsed.username and not parsed.password
                        and not parsed.query and not parsed.fragment
                        and bool(parsed.path.strip("/"))
                        and not any(char.isspace() for char in source))
    except ValueError:
        valid_source = False
    if not valid_source:
        fail("invalid_profile", "source must be an HTTPS repository URL without credentials, query, or fragment")
    return profile


def validate_catalog(catalog):
    object_fields(catalog, ("schema", "plugin", "bootstrap", "releases"), "Package playbook manifest")
    check_header(catalog, "Package playbook manifest", plugins=(PLUGIN,))
    if catalog["bootstrap"] != BOOTSTRAP:
        fail("unsupported_bootstrap", "This dispatcher requires bootstrap release " + BOOTSTRAP)
    releases = catalog["releases"]
    if not isinstance(releases, dict) or not releases:
        fail("invalid_manifest", "Package playbook manifest must list releases")
    for release, entry in releases.items():
        check_release(release, allow_legacy=True)
        object_fields(entry, ("manifest_sha256",), "Release catalog entry")
        check_hash(entry["manifest_sha256"], "manifest_sha256")


def validate_manifest(manifest, release):
    object_fields(manifest, ("schema", "plugin", "release", "files", "skills"), "Release manifest")
    check_header(manifest, "Release manifest")
    if manifest["release"] != release:
        fail("invalid_manifest", "Release manifest identity does not match the selected release")
    files, skills = manifest["files"], manifest["skills"]
    if not isinstance(files, dict) or not files:
        fail("invalid_manifest", "Release manifest must list payload files")
    for path, digest in files.items():
        checked_relative(path)
        if path == "manifest.json":
            fail("invalid_manifest", "A release manifest cannot hash itself")
        check_hash(digest, "File digest")
    expected = LEGACY_SKILLS if release == LEGACY else SKILLS
    if not isinstance(skills, dict) or set(skills) != set(expected):
        fail("invalid_manifest", "Release manifest must map exactly its supported public skills")
    for skill, paths in skills.items():
        if (not isinstance(paths, list) or not paths
                or any(not isinstance(path, str) for path in paths)
                or len(set(paths)) != len(paths)):
            fail("invalid_manifest", "Invalid ordered file list for " + skill)
        for path in paths:
            checked_relative(path)
            if path not in files:
                fail("invalid_manifest", "Skill references an unhashed file: " + path)


def resolve(plugin_root, project_root, skill, bootstrap=False, profile_path=None):
    if skill not in SKILLS:
        fail("unknown_skill", "Unknown workflow skill: " + str(skill))
    if bootstrap and skill not in BOOTSTRAP_SKILLS:
        fail("invalid_bootstrap", "--bootstrap is only supported for work-start and work-adopt")
    project_root = checked_root(project_root, "Project root")
    if profile_path is not None:
        supplied = Path(os.path.abspath(os.path.expanduser(str(profile_path))))
        expected = project_root / "docs/OPERATING.md"
        if supplied.is_symlink() or supplied.resolve(strict=False) != expected.resolve(strict=False):
            fail("invalid_profile_path", "--profile must identify this project's docs/OPERATING.md")
    profile = read_profile(project_root)
    if profile is not None and bootstrap:
        fail("invalid_bootstrap", "An adopted project must resolve its pinned release without --bootstrap")
    if profile is not None:
        mode, release = "adopted", profile["release"]
    elif bootstrap:
        mode, release = "bootstrap", BOOTSTRAP
    elif skill in LEGACY_SKILLS:
        mode, release = "legacy", LEGACY
    elif skill in BOOTSTRAP_SKILLS:
        fail("bootstrap_required", "No adoption metadata: explicit --bootstrap is required for " + skill)
    else:
        fail("adoption_required", "work-deliver requires explicit project adoption")
    try:
        plugin_root = checked_root(plugin_root, "Plugin root")
        return resolve_payload(plugin_root, project_root, skill, mode, release, profile)
    except (WorkflowError, OSError) as error:
        if profile is not None:
            error.required_identity = profile
        raise


def resolve_payload(plugin_root, project_root, skill, mode, release, profile):
    catalog_path = safe_file(plugin_root, "playbooks/manifest.json")
    catalog = parse_json(read_file(catalog_path), "package playbook manifest")
    validate_catalog(catalog)
    entry = catalog["releases"].get(release)
    if entry is None:
        fail("missing_release", "The installed package does not contain required release " + release)
    manifest_path = safe_file(plugin_root, "playbooks/" + release + "/manifest.json")
    raw = read_file(manifest_path)
    digest = sha256(raw)
    if digest != entry["manifest_sha256"]:
        fail("integrity_mismatch", "Release manifest does not match the installed package manifest")
    if profile is not None and digest != profile["manifest_sha256"]:
        fail("integrity_mismatch", "Release manifest does not match docs/OPERATING.md")
    manifest = parse_json(raw, "release manifest")
    validate_manifest(manifest, release)
    release_root = manifest_path.parent
    verified = {}
    for relative, expected in manifest["files"].items():
        path = safe_file(release_root, relative)
        if sha256(read_file(path)) != expected:
            fail("integrity_mismatch", "Payload file does not match its manifest: " + relative)
        verified[relative] = path
    result = {
        "status": "ready", "mode": mode, "plugin": PLUGIN,
        "release": release, "manifest_sha256": digest,
        "identity_verified": True,
        "identity_basis": "project-and-package-manifests" if profile else "installed-package-manifest",
        "project_root": str(project_root), "skill": skill,
        "files": [{"path": str(verified[path]), "sha256": manifest["files"][path]}
                  for path in manifest["skills"][skill]],
    }
    if profile:
        result["source"] = profile["source"]
        result["source_commit"] = profile["source_commit"]
        result["source_commit_verified"] = False
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--skill", required=True)
    parser.add_argument("--bootstrap", action="store_true")
    parser.add_argument("--profile", help="Optional assertion of the project's docs/OPERATING.md path")
    parser.add_argument("--plugin-root", default=str(Path(__file__).absolute().parent.parent))
    args = parser.parse_args(argv)
    try:
        result = resolve(args.plugin_root, args.project_root, args.skill, args.bootstrap, args.profile)
    except WorkflowError as error:
        value = {"status": "error", "code": error.code, "message": str(error)}
        if hasattr(error, "required_identity"):
            value["required_identity"] = error.required_identity
        print(json.dumps(value))
        return 1
    except OSError as error:
        value = {"status": "error", "code": "filesystem_error", "message": str(error)}
        if hasattr(error, "required_identity"):
            value["required_identity"] = error.required_identity
        print(json.dumps(value))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
