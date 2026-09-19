---
name: work-adopt
description: "Inspect an existing project and prepare, or carry out when authorized, its adoption of The Pantomime's Paradox, preserving in-flight work. Use for 'bring this repo under the workflow', 'adopt this project'."
allowed-tools: Bash(python3 ${CLAUDE_PLUGIN_ROOT}/scripts/resolve_workflow.py:*), Read, Glob, Grep
---

Resolve the project's pinned process release before applying any process instruction. On Claude Code:

```sh
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/resolve_workflow.py" --project-root "${CLAUDE_PROJECT_DIR}" --skill work-adopt
```

On Codex or any other assistant, the package root is two directories above this `SKILL.md` and the project root is the working directory:

```sh
python3 "<package root>/scripts/resolve_workflow.py" --project-root "$PWD" --skill work-adopt
```

For a project that has not adopted, add `--bootstrap`; that reads guidance and adopts nothing. For an adopted project run it without the flag.

Use the real project root even when the session's checkout differs from the package location. Read only the files the resolver lists under `files`, then the project's existing instructions and `docs/OPERATING.md` when present. A `ready` result names the exact process; apply it within the scope the user authorized. An `error` result is reported with its `required_identity`; never substitute another release or assume adoption.

Before writing an adoption block, read `${CLAUDE_PLUGIN_ROOT}/docs/resolver-contract.md` for the exact markers, fields and where each value comes from; do not infer the schema or invent the `source_commit`. Read `${CLAUDE_PLUGIN_ROOT}/docs/project-state-contract.md` only if the user asks for a machine-readable state block.

If `python3` is unavailable, read the adoption block in `docs/OPERATING.md`, take its `release`, and read `playbooks/<release>/core.md` and `playbooks/<release>/stages/adopt.md` from the package root, stating that payload hashes were not verified. Without an adoption block, the bootstrap release is the `bootstrap` value in `playbooks/manifest.json`.

Finish with the handoff the process requires (core rule C07): where the work stands and the single next action, in the project's guidance mode.
