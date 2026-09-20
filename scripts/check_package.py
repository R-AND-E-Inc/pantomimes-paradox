#!/usr/bin/env python3
"""Mechanical package checks: manifests parse, skills are complete, no project-specific leftovers."""
import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ["work-independent-reviewer", "work-explorer", "work-researcher", "work-verifier"]
SKILLS = ["work-start", "work-adopt", "work-steps", "work-plan", "work-resume", "work-deliver",
          "work-review", "work-evidence", "work-flow-check", "work-closeout", "paradox-setup", "paradox-mode"]
# Words that belong to the owner's own projects, not to the shared package. Provenance and the
# frozen releases published under the former name are exempt.
LEFTOVERS = re.compile(r"Artax|5D\.3A|vn_library|R-AND-E-Inc/personal-workflows|Truth and Reconciliation")
CHECKED_TEXT = ["skills", "guide", "templates", "hooks", "agents", "README.md", "NOTICE.md", "playbooks/2.0.0", "docs"]
MAX_BYTES = 300_000


def main():
    problems = []
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    codex = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
    codex_market = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    if codex_market["plugins"][0]["name"] != "pantomimes-paradox" or codex_market["plugins"][0]["source"]["path"] != "./":
        problems.append("Codex marketplace entry must point at this repository root")
    json.loads((ROOT / "hooks/hooks.json").read_text())
    if not (plugin["name"] == marketplace["plugins"][0]["name"] == codex["name"] == "pantomimes-paradox"):
        problems.append("plugin names differ across manifests")
    if plugin["version"] != codex["version"]:
        problems.append("plugin versions differ between Claude and Codex manifests")
    if "hooks" in codex:
        problems.append("the Codex plugin validator rejects a hooks field in the manifest")
    for skill in SKILLS:
        path = ROOT / "skills" / skill / "SKILL.md"
        if not path.exists():
            problems.append("missing skill: " + skill)
            continue
        text = path.read_text()
        if not text.startswith("---\nname: " + skill + "\n"):
            problems.append("skill frontmatter name mismatch: " + skill)
        front = text.split("---", 2)[1]
        if "description:" not in front:
            problems.append("skill without description: " + skill)
        for line in front.splitlines():
            key, sep, value = line.partition(": ")
            if sep and key in {"name", "description"} and ": " in value and not value.startswith('"'):
                problems.append("unquoted colon in frontmatter %s of %s" % (key, skill))
            if key == "argument-hint":
                problems.append("argument-hint is rejected by the Codex validator: " + skill)
        if not (ROOT / "skills" / skill / "agents/openai.yaml").exists():
            problems.append("missing Codex interface file: " + skill)
    for agent in AGENTS:
        path = ROOT / "agents" / (agent + ".md")
        if not path.exists():
            problems.append("missing agent: " + agent)
            continue
        front = path.read_text().split("---", 2)[1]
        if "name: " + agent not in front:
            problems.append("agent frontmatter name mismatch: " + agent)
        if agent != "work-independent-reviewer" and "model:" not in front:
            problems.append("delegate without an explicit model: " + agent)
        if "disallowedTools:" not in front:
            problems.append("agent without a write denylist: " + agent)
    for extra in (ROOT / "agents").iterdir():
        if extra.suffix == ".md" and extra.stem not in AGENTS:
            problems.append("unexpected agent file: " + extra.name)
    # Codex cannot declare agents in a plugin manifest, so the same roster ships as templates the
    # user copies into ~/.codex/agents. The two rosters must not drift apart.
    codex_agents = ROOT / "templates/codex/agents"
    for agent in AGENTS:
        path = codex_agents / (agent + ".toml")
        if not path.exists():
            problems.append("missing Codex delegate template: " + agent)
            continue
        try:
            value = tomllib.loads(path.read_text())
        except tomllib.TOMLDecodeError as error:
            problems.append("unparsable Codex delegate %s: %s" % (agent, error))
            continue
        unknown = set(value) - {"name", "description", "developer_instructions", "model",
                                "model_reasoning_effort", "sandbox_mode", "mcp_servers"}
        if unknown:
            problems.append("undocumented Codex agent field in %s: %s" % (agent, ", ".join(sorted(unknown))))
        for required in ("name", "description", "developer_instructions"):
            if not value.get(required):
                problems.append("Codex delegate %s is missing %s" % (agent, required))
        if value.get("name") != agent:
            problems.append("Codex delegate name mismatch: " + agent)
        if value.get("sandbox_mode") not in {"read-only", "workspace-write"}:
            problems.append("Codex delegate %s needs a bounded sandbox_mode" % agent)
        if agent == "work-independent-reviewer" and "model_reasoning_effort" in value:
            problems.append("the reviewer must inherit the session model and effort, not be routed down")
        if agent != "work-independent-reviewer" and "model_reasoning_effort" not in value:
            problems.append("Codex delegate without routed effort: " + agent)
    for extra in codex_agents.iterdir():
        if extra.suffix == ".toml" and extra.stem not in AGENTS:
            problems.append("unexpected Codex delegate file: " + extra.name)
    for extra in (ROOT / "skills").iterdir():
        if extra.is_dir() and extra.name not in SKILLS:
            problems.append("unexpected skill folder: " + extra.name)
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.name == ".DS_Store":
            problems.append("stray file: " + str(path.relative_to(ROOT)))
        if path.stat().st_size > MAX_BYTES:
            problems.append("oversized file: " + str(path.relative_to(ROOT)))
    for entry in CHECKED_TEXT:
        base = ROOT / entry
        files = [base] if base.is_file() else [p for p in base.rglob("*") if p.is_file()]
        for path in files:
            if path.suffix not in {".md", ".json", ".yaml", ".yml", ".mjs"}:
                continue
            for number, line in enumerate(path.read_text().splitlines(), 1):
                if LEFTOVERS.search(line):
                    problems.append("project-specific text at %s:%d" % (path.relative_to(ROOT), number))
    for problem in problems:
        print(problem)
    print(json.dumps({"status": "ok" if not problems else "problems", "count": len(problems)}))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
