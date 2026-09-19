---
name: work-evidence
description: Check whether the available results actually prove the acceptance criteria for one exact candidate, including human and environment limits.
argument-hint: "[candidate or claim to verify]"
allowed-tools: Bash(python3 ${CLAUDE_PLUGIN_ROOT}/scripts/resolve_workflow.py:*), Read, Glob, Grep
---

Resolve the project's pinned process release before applying any process instruction. The package root is `${CLAUDE_PLUGIN_ROOT}` on Claude Code, or two directories above this file elsewhere:

```sh
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/resolve_workflow.py" --project-root "${CLAUDE_PROJECT_DIR}" --skill work-evidence
```

Use the real project root even when the session's checkout differs from the package location. Read only the files the resolver lists under `files`, then the project's own bindings in `docs/OPERATING.md`. A `ready` result names the exact process; apply it within the scope the user authorized. An `error` result is reported with its `required_identity`; never substitute another release or assume adoption.

If `python3` is unavailable, read the adoption block in `docs/OPERATING.md`, take its `release`, and read `playbooks/<release>/core.md` and `playbooks/<release>/stages/evidence.md` from the package root, stating that payload hashes were not verified.

Finish with the handoff the process requires (core rule C07): where the work stands and the single next action, in the project's guidance mode.
