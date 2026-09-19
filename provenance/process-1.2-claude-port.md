# Process 1.2.0 — Claude port

`1.2.0` exists because this package moved from Codex/ChatGPT to Claude Code and claude.ai. The package's own rule is that a released playbook is never mutated in place and a process change gets a new release with an explicit project transition. Three sentences in `1.1.0` named platform capabilities that do not exist on Claude, so those sentences changed and the release number moved.

Nothing else about the method changed. `1.2.0` keeps every rule, boundary, stage routing, authority order, and acceptance requirement of `1.1.0`, and keeps all ten public command names.

## Exact differences from 1.1.0

| Location | `1.1.0` | `1.2.0` |
|---|---|---|
| `core.md` title | `process 1.1.0` | `process 1.2.0 (Claude)` |
| `core.md` intro | — | adds one sentence recording that this is `1.1.0` ported to Claude, method unchanged |
| `core.md` C04 | "Use available Codex/ChatGPT skills, connectors, native worktrees, review tools, and app capabilities" | "Use available Claude skills, plugins, MCP connectors, git worktrees, subagents, review tools, and app capabilities" |
| `core.md` C05 | "User-owned app tasks"; "does not request sidebar tasks"; "Native subagents" | "User-owned background sessions or tasks"; "does not request separate sessions"; "Subagents" |
| `stages/steps.md` | offer one `` `$work-deliver` `` prompt | offer one `` `/work-deliver` `` prompt |

No other byte differs. `diff -r playbooks/1.1.0 playbooks/1.2.0` shows exactly these five changed lines.

## What is preserved byte for byte

`playbooks/legacy-personal-workflows`, `playbooks/1.0.0`, and `playbooks/1.1.0` are unchanged from the Codex package, and their release-manifest digests are identical:

| Release | `manifest_sha256` |
|---|---|
| `legacy-personal-workflows` | `7a285cb257317a1c1efbe00113c6b20754dd17868d5dfbf79461e0675a5d86fa` |
| `1.0.0` | `cfb40d4d31f1e633d9a7b5a03b59225806183983444145479aceb0e60529aef8` |
| `1.1.0` | `896db76c15bd1faf3ce44fb6f1dbe4a15c0311efc8175623721201b191d4d9c1` |
| `1.2.0` | `022d49db243dc18a07bf275bd48c647d8ebf5927063ecd7a024f7462dd6d81e0` |

A project whose `docs/OPERATING.md` pins `1.1.0` and `896db76c…` therefore resolves against this Claude package with no repository change at all, and keeps the exact `1.1.0` wording until it chooses to migrate. That includes the first adopter, Artax Lives.

## Bootstrap

The package bootstrap release moved from `1.1.0` to `1.2.0`. Bootstrap affects only `work-start` and `work-adopt` on a project that has not adopted; it still never writes an adoption record. Adopted projects are unaffected.

## Migrating

Migration is optional and is a normal adoption change. See [installation and rollback](INSTALLATION.md#migrating-an-adopted-project-from-110-to-120).
