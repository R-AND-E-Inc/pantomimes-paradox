# Using it with Codex

The same package installs into Codex from GitHub. The skills, process files and templates are identical to the Claude Code ones; the commands and the packaging differ, and the delegate roster is installed separately because a Codex plugin cannot ship one yet.

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

## Add the delegates

The process delegates bounded reading, external questions and long check runs so that their material never fills your session. Codex supports this, but a Codex plugin has no way to declare an agent, so you install the four roles yourself, once, by copying them into your personal agents folder:

```sh
mkdir -p ~/.codex/agents
cp templates/codex/agents/*.toml ~/.codex/agents/
```

Use `.codex/agents/` inside a repository instead if you want them for that project only. Start a new thread afterwards. You then have `work-explorer`, `work-researcher`, `work-verifier` and `work-independent-reviewer`, which the skills hand bounded tasks to by name.

Without them nothing breaks: the process says to do the work inline and disclose that no delegate ran. You lose the context isolation, not the method.

## Add the standing reminder

Claude Code gets a session-start hook that restates the handoff rule, the retrieval rule and the plain-disagreement rule. Codex has a `SessionStart` hook of its own, but the plugin validator on current Codex rejects a `hooks` field in the plugin manifest, so the package cannot ship one. Paste [templates/codex/AGENTS-global-snippet.md](../templates/codex/AGENTS-global-snippet.md) into `~/.codex/AGENTS.md` instead, which is simpler and does not depend on an install path. If you would rather use the hook, it is documented under Codex hooks and its stdout is added as developer context; keep only one of the two so the rule has a single owner.

## Commands

Every command is `$<name>`: `$paradox-setup`, `$work-start`, `$work-adopt`, `$work-steps`, `$work-plan`, `$work-resume`, `$work-deliver`, `$work-review`, `$work-evidence`, `$work-flow-check`, `$work-closeout`, `$paradox-mode`. Plain language reaches the same skills. See [commands.md](commands.md).

## Differences from Claude Code

- **Delegates are user-installed, not shipped.** Claude Code loads them from the plugin's `agents/` folder; Codex has no plugin field for that, so the same four roles ship as templates you copy once. Tracked upstream as an open request.
- **Delegate limits are expressed differently.** The Claude definitions restrict tools directly with a write denylist. The Codex definitions use `sandbox_mode`, which is read-only for the explorer, researcher and reviewer, and workspace-write for the verifier because tests and builds produce artifacts. That sandbox cannot by itself stop the verifier editing source, so its instructions carry that rule and the coordinator still inspects what it reports.
- **Model routing uses effort, not a model name.** The retrieval roles set `model_reasoning_effort = "low"` rather than naming a cheaper model, because a wrong model string would break the role and the valid set differs per account. Add `model = "..."` yourself if you want it. The reviewer deliberately sets neither, so it inherits your session's model; it judges correctness, which the routing rule says never to route down.
- **Package root:** the skills give Codex its own command form (the package root is two directories above each `SKILL.md`; the project root is the working directory).

## Update

```sh
codex plugin marketplace upgrade
codex plugin add pantomimes-paradox@pantomimes-paradox
```

Then start a new thread. An update never changes a project's pinned release. Re-copy the agent templates after an update only if the release notes say the roster changed.
