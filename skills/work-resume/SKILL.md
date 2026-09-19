---
name: work-resume
description: "Reconstruct where the project actually is and the next authorized action from state, branches, approved plans and active work. Use when returning to a project or handing it over."
allowed-tools: Bash(python3 ${CLAUDE_PLUGIN_ROOT}/scripts/resolve_workflow.py:*), Read, Glob, Grep
---

Resolve the project's pinned process release before applying any process instruction. On Claude Code:

```sh
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/resolve_workflow.py" --project-root "${CLAUDE_PROJECT_DIR}" --skill work-resume
```

On Codex or any other assistant, the package root is two directories above this `SKILL.md` and the project root is the working directory:

```sh
python3 "<package root>/scripts/resolve_workflow.py" --project-root "$PWD" --skill work-resume
```

Use the real project root even when the session's checkout differs from the package location. Read only the files the resolver lists under `files`, then the project's own bindings in `docs/OPERATING.md`. A `ready` result names the exact process; apply it within the scope the user authorized. An `error` result is reported with its `required_identity`; never substitute another release or assume adoption.

If `python3` is unavailable, read the adoption block in `docs/OPERATING.md`, take its `release`, and read `playbooks/<release>/core.md` and `playbooks/<release>/stages/resume.md` from the package root, stating that payload hashes were not verified.

Finish with the handoff the process requires (core rule C07): where the work stands and the single next action, in the project's guidance mode.
