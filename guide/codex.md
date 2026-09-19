# Using it with Codex

The same package installs into Codex from GitHub. The skills, process files and templates are identical to the Claude Code ones; only the commands and the packaging differ.

## Install

Codex reads plugins from marketplaces. This repository is one. On a machine with the Codex CLI (the Codex desktop app ships it; on macOS it is at `/Applications/ChatGPT.app/Contents/Resources/codex` if `codex` is not on your PATH):

```sh
codex plugin marketplace add R-AND-E-Inc/pantomimes-paradox
codex plugin add pantomimes-paradox@pantomimes-paradox
```

Start a new thread so Codex picks up the skills. Then, in the folder of a project:

```
$paradox-setup
```

The Codex app's plugin settings can also add a marketplace and install from it; the marketplace source is the same `R-AND-E-Inc/pantomimes-paradox`.

Requirement: `python3` on the machine (macOS and Linux have it; on Windows install Python 3). Without it the skills still run, cannot verify the process files' hashes, and say so.

## Commands

Every command is `$<name>`: `$paradox-setup`, `$work-start`, `$work-adopt`, `$work-steps`, `$work-plan`, `$work-resume`, `$work-deliver`, `$work-review`, `$work-evidence`, `$work-flow-check`, `$work-closeout`, `$paradox-mode`. Plain language reaches the same skills. See [commands.md](commands.md).

## Differences from Claude Code

- Independent review: Codex has no plugin-defined subagent, so `work-review` runs the fresh-context review as a separate task or Codex subagent that receives only the neutral brief; the package's `agents/` folder is ignored.
- Session reminder: Claude Code gets a session-start hook that restates the handoff rule; Codex has no equivalent. Paste [templates/codex/AGENTS-global-snippet.md](../templates/codex/AGENTS-global-snippet.md) into `~/.codex/AGENTS.md` if you want the rule outside the skills too.
- Package root: the skills give Codex its own command form (the package root is two directories above each `SKILL.md`; the project root is the working directory).

## Update

```sh
codex plugin marketplace upgrade
codex plugin add pantomimes-paradox@pantomimes-paradox
```

Then start a new thread. An update never changes a project's pinned release.
