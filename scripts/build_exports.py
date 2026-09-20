#!/usr/bin/env python3
"""Build chat-only skill exports (ChatGPT and claude.ai uploads) from a committed source tree.

Each export is one zip per skill: a small loader SKILL.md, the exact process files that skill
needs (byte-identical to playbooks/<release>/), the release manifest and an identity record.
A chat surface cannot run the resolver, so the loader tells the assistant what it can and cannot
verify. Outputs are deterministic for a given source commit.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_manifests import check_all  # noqa: E402
from resolve_workflow import BOOTSTRAP, PLUGIN, check_release  # noqa: E402

SOURCE_URL = "https://github.com/R-AND-E-Inc/pantomimes-paradox"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def archive(path, files):
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(files.items()):
            entry = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            z.writestr(entry, data)
    return {"file": path.name, "sha256": digest(path.read_bytes()), "entries": len(files)}


def loader_text(skill, description, paths, release):
    files = ", ".join("`payload/" + p + "`" for p in paths)
    return (
        "---\nname: " + skill + "\ndescription: " + json.dumps(description) + "\n---\n\n"
        "This is a chat-only export of The Pantomime's Paradox skill `" + skill + "`, process release "
        + release + ". It is for ChatGPT or claude.ai conversations that cannot run the package's resolver.\n\n"
        "1. Read `identity.json`. If the user's project has a `docs/OPERATING.md` adoption block, compare its "
        "`release` and `manifest_sha256` with this identity; a mismatch means this export is for a different "
        "release, so say so and stop. A match is reported provenance, not a hash you computed.\n"
        "2. Read only " + files + ". They are byte-identical to the package's process files.\n"
        "3. Apply them within what the user authorized, using whatever tools this conversation really has. "
        "Never claim local execution, Git access, test runs, task dispatch or independent review that did not happen; "
        "name each such gap. A copyable prompt is not execution.\n"
        "4. For a project that has not adopted the workflow, only `work-start` and `work-adopt` may use this "
        "export as bootstrap guidance; other skills need an adopted project.\n"
        "5. **This surface has no delegates.** The process names `work-explorer`, `work-researcher`, "
        "`work-verifier` and `work-independent-reviewer`; none of them exist in a plain chat. Do the bounded "
        "work yourself where the conversation allows it and say that no delegate ran, or return the brief for "
        "the user to run in Codex or Claude Code. Never describe a delegate's report you did not receive, and "
        "never call a same-context second pass an independent review.\n"
        "6. End every reply with where the work stands and the single next action (core rule C07), in the "
        "project's guidance mode: guided, expert, or terse, with guided the default when none is recorded. "
        "No mode removes a disclosed limitation, an unverified claim, a failure, or a required approval.\n"
    )


def build(root, output, release=BOOTSTRAP):
    root = Path(root).resolve()
    check_release(release)
    check_all(root)
    git = lambda *args: subprocess.check_output(["git", "-C", str(root), *args])  # noqa: E731
    if git("status", "--porcelain").strip():
        raise ValueError("Exports require a clean committed source tree")
    commit = git("rev-parse", "HEAD").decode().strip()
    output = Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError("Output must be outside the source checkout")
    output.mkdir(parents=True, exist_ok=True)
    version = json.loads((root / ".claude-plugin/plugin.json").read_text())["version"]
    manifest_path = root / "playbooks" / release / "manifest.json"
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    identity = {"schema": 1, "plugin": PLUGIN, "release": release, "source": SOURCE_URL,
                "source_commit": commit, "manifest_sha256": digest(manifest_bytes)}
    artifacts = []
    for skill, paths in sorted(manifest["skills"].items()):
        raw = (root / "skills" / skill / "SKILL.md").read_text()
        description = ""
        for line in raw.split("---", 2)[1].splitlines():
            key, sep, value = line.partition(":")
            if sep and key.strip() == "description":
                description = value.strip().strip('"')
        packet = {skill + "/payload/" + p: (manifest_path.parent / p).read_bytes() for p in paths}
        if skill == "work-deliver":
            for p in manifest["skills"]["work-steps"]:
                packet[skill + "/payload/" + p] = (manifest_path.parent / p).read_bytes()
        payload_names = [k.split("/payload/", 1)[1] for k in sorted(packet)]
        packet[skill + "/SKILL.md"] = loader_text(skill, description, payload_names, release).encode()
        packet[skill + "/payload/manifest.json"] = manifest_bytes
        packet[skill + "/identity.json"] = (json.dumps(identity, indent=2) + "\n").encode()
        artifacts.append(archive(output / (skill + "-chat-" + release + ".zip"), packet))
    receipt = {"source_commit": commit, "package_version": version, "identity": identity, "artifacts": artifacts}
    (output / "exports-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin-root", default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument("--output", required=True)
    parser.add_argument("--release", default=BOOTSTRAP)
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.plugin_root, args.output, args.release), indent=2))
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
