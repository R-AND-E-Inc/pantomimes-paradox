---
name: paradox-setup
description: First-time setup and orientation for The Pantomime's Paradox. Checks that the package resolves, sets guided or expert mode, and routes a new idea to work-start or an existing codebase to work-adopt. Use for "set me up", "get started", "how do I use this", or right after installing.
argument-hint: "[guided|expert] [new|existing]"
allowed-tools: Bash(python3 ${CLAUDE_PLUGIN_ROOT}/scripts/resolve_workflow.py:*), Read, Glob, Grep
---

This skill orients the user and hands them one next prompt. It creates no files and adopts nothing. Read `${CLAUDE_PLUGIN_ROOT}/guide/commands.md` once for the command summaries.

1. **Confirm the package works.** Run the resolver in bootstrap mode against the current directory:

   ```sh
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/resolve_workflow.py" --project-root "${CLAUDE_PROJECT_DIR}" --skill work-start --bootstrap
   ```

   `status: ready` with `mode: bootstrap` means the package is intact and this folder has not adopted the workflow; report the `release`. `mode: adopted` (or the error `invalid_bootstrap`) means this project is already adopted: say so, run `work-resume` instead of continuing here, and stop. Any other error is reported verbatim with its `required_identity`; do not repair or install anything.

2. **Set the guidance mode.** If the user did not say, ask one question with a recommendation: *guided* (each reply explains what happened, why the next step matters, what they will see, and how to tell it worked) or *expert* (one-line handoffs). Recommend guided for anyone who has not run a software project with an assistant before. Remember the answer for this session; it is written into the project's `docs/OPERATING.md` as `Guidance mode: <mode>` when `work-start` or `work-adopt` creates that file (every adopted project has one, even a small utility that otherwise has only a README).

3. **Route.** Ask, if not already clear, whether this is a new idea or an existing codebase, then explain in three lines what the next skill will do and what it will ask for. Do not start discovery or read the codebase here.

4. **Hand off** (core rule C07 applies from here on): give the exact next prompt to paste, and nothing else to do. For a new idea: `/pantomimes-paradox:work-start <one sentence about the idea>`. For an existing codebase: `/pantomimes-paradox:work-adopt this project; inspect it and propose the migration first`. On Codex the same commands are `$work-start` and `$work-adopt`.

In guided mode also list the twelve commands in one line each from `guide/commands.md`, point to `${CLAUDE_PLUGIN_ROOT}/guide/guided.md` as the long read for later, and say that plain language works: the assistant picks the right skill from an ordinary request, so the commands are shortcuts, not homework. In expert mode point to `guide/expert.md` instead.
