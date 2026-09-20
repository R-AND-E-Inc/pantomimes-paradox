# Codex and chat parity for process 2.1.0

Package version 1.3.0. No process change: releases through 2.1.0 are untouched, and every pinned project is unaffected.

Process 2.1.0 named a four-role delegation roster, but only Claude Code could load it, because the roster ships in the plugin's `agents/` folder. This release gives Codex the same roster and corrects two claims the guides made about Codex.

## What was wrong

Both statements were in `guide/codex.md` and the Codex AGENTS snippet, and both are false:

- "Codex has no plugin-defined subagent." Codex does have subagents. They are declared by the user as `~/.codex/agents/<name>.toml` (or `.codex/agents/` per repository) with `name`, `description` and `developer_instructions` required, and `model`, `model_reasoning_effort`, `sandbox_mode` and `mcp_servers` optional. What Codex lacks is a *plugin* field to declare one; `plugin.json` has no `agents` key, tracked upstream as an open request since April 2026.
- "Codex has no session-start hook." Codex has a `SessionStart` hook whose stdout is added as developer context, and the published plugin manifest spec lists a `hooks` field. However, the plugin validator shipped with current Codex rejects `hooks` in the manifest. Verified empirically on 2026-09-20: adding the field produced `plugin.json field 'hooks' is not accepted by plugin validation`, and removing it passed. The published spec and the shipped validator disagree, so the package follows the validator.

## What changed

- **`templates/codex/agents/*.toml`**: the four delegates for Codex, copied once into `~/.codex/agents/`. They carry the same briefs as the Claude definitions, with two deliberate differences. Limits use `sandbox_mode`, read-only for the explorer, researcher and reviewer, and workspace-write for the verifier, because tests and builds write artifacts; that sandbox cannot forbid source edits by itself, so the verifier's instructions carry the rule. Routing uses `model_reasoning_effort = "low"` rather than a model name, because a wrong model string would break the role and the valid set differs per account. The reviewer sets neither, so it inherits the session's model and effort: it judges correctness, which C04 says is never routed down.
- **`guide/codex.md`**: rewritten with the delegate install, the corrected claims, and a differences section that states what Codex expresses differently rather than what it lacks.
- **`templates/codex/AGENTS-global-snippet.md`**: the false header claim replaced, and the delegate names added to the retrieval rule with the fallback when they are not installed.
- **Chat exports** (`scripts/build_exports.py`): the loader now tells a chat surface that it has no delegates, names all four so the assistant cannot read C05's roster and claim one ran, and names the three guidance modes. `guide/chatgpt.md` says the same in the reader's terms.
- **`scripts/check_package.py`**: the two rosters must match, every Codex delegate must parse as TOML with only documented fields, carry a bounded `sandbox_mode`, and route effort except the reviewer, which must not. The Codex manifest must not regain `hooks`.
- **`tests/test_exports.py`**: the chat loader must disclose the missing delegates and name the guidance mode.

## Controls

Each new check was proven to fail when violated, on 2026-09-20: removing a Codex delegate, adding routed effort to the reviewer, restoring `hooks` to the Codex manifest, and weakening the loader's delegate disclosure each produced the expected failure, and the tree passed with them restored.

## Not done

No Codex hook config is shipped. The AGENTS.md snippet already carries the standing behaviour, is stable across installed versions, and does not depend on a version-numbered cache path. Shipping both would give one rule two owners, which the method forbids.
