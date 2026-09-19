# Codex → Claude conversion notes

This package was converted from Personal Workflows `1.1.0+codex.20260907203350`. It is a **Claude Code plugin**, not a single skill: it carries ten separately invocable workflows, four immutable playbook releases, a read-only resolver, a subagent, and maintainer tooling.

The resolver, manifests, playbooks, provenance ledger, and tests were already platform independent and moved across unchanged except where listed below.

## Direct equivalents

| Codex / ChatGPT | Claude | Notes |
|---|---|---|
| `.codex-plugin/plugin.json` | `.claude-plugin/plugin.json` | Schema rewritten; `interface` block folded into `displayName`, `description`, `keywords`, `metadata` |
| `$work-plan` | `/work-plan` (or `/personal-workflows:work-plan`) | All ten command names preserved |
| `skills/<n>/agents/openai.yaml` | skill frontmatter | `display_name`/`short_description`/`default_prompt` preserved under `metadata:`; `argument-hint` added |
| "package root is two directories above this skill" | `${CLAUDE_PLUGIN_ROOT}` | Resolved absolutely, so the resolver no longer depends on the caller's working directory |
| implicit project root | `${CLAUDE_PROJECT_DIR}` | Passed explicitly to `--project-root` |
| Codex desktop and CLI | Claude Code (CLI, desktop, IDE, web) | `docs/surface-adapters.md` |
| ChatGPT without local execution | claude.ai chat with an uploaded Skill | Customize → Skills |
| ChatGPT with filesystem and Python | claude.ai / Cowork / Claude Code on the web | Resolver runs normally |
| ChatGPT stage export `<skill>-chatgpt-<release>.zip` | `<skill>-claude-skill-<release>.zip` | Same packet shape; loader frontmatter reduced to portable `name` + `description` |
| ChatGPT native subagents | Claude Code subagents | Plus a concrete `work-independent-reviewer` agent |
| ChatGPT native worktrees | Claude Code git worktrees | |
| `codex plugin add personal-workflows@personal --json` | `/plugin marketplace add …` + `/plugin install personal-workflows@personal-workflows` | Or the `claude plugin …` CLI |
| Codex `marketplace-entry.json` | `.claude-plugin/marketplace.json` | Claude marketplace schema |
| cachebuster transport reload | plugin reinstall/update | No cachebuster concept in Claude |
| `learn.chatgpt.com` / `developers.openai.com` references | `code.claude.com/docs` references | |

## Added for Claude

These did not exist in the Codex package. Each implements a rule the process already stated.

- **`agents/work-independent-reviewer.md`** — the process requires a review that did not author the candidate ("a same-context second pass is not independent"). Codex expressed this as a sidebar task or native subagent; Claude expresses it as a subagent definition. Tool-gated to never write, edit, or merge.
- **`allowed-tools` on every skill** — pre-approves only the read-only resolver command plus read tools, so the first step of each workflow does not prompt. Everything after that follows the session's ordinary permission mode.
- **`disallowed-tools` on `work-steps`** — `work-steps` already declared itself guidance-only ("Do not execute generated prompts, edit project files, or dispatch tasks"). Claude can enforce that mechanically; Codex could not. No other skill is restricted.
- **`.claude-plugin/marketplace.json`** — lets the unzipped folder be installed directly with `/plugin marketplace add`.
- **`playbooks/1.2.0/`** and **`docs/process-1.2-claude-port.md`** — see those notes.

## Cannot be reproduced in Claude

| Codex feature | Status |
|---|---|
| `interface.defaultPrompt` (Codex prefilled the prompt box when you picked a skill) | **No equivalent.** Claude Code has no prefilled-prompt field. The exact string is preserved as inert `metadata.defaultPrompt` and appears in the user guide; `argument-hint` is the closest live affordance. |
| `interface.displayName` / `shortDescription` per skill | **No dedicated field.** Claude surfaces the skill by command name and `description`. Both strings are preserved under `metadata:` but Claude does not render them. |
| `interface.longDescription` / `category` / `capabilities` | **No plugin.json equivalent.** Moved to `metadata`, `keywords`, and the marketplace entry's `category`. |
| Marketplace `policy: {installation: AVAILABLE, authentication: ON_INSTALL}` | **No equivalent.** Claude marketplaces have no install-policy or authentication-on-install field. Dropped; install authorization is the user's own `/plugin` action. |
| ChatGPT "sidebar task" as a user-visible object the owner returns to | **Partial.** Claude has subagents, background tasks, and separate sessions, but no identical persistent sidebar object. The process text now says "background sessions or tasks". |
| Codex-specific capability validation run | **Not performed here.** Installation in your account, connector authorization, and real cloud execution remain a separate acceptance step, exactly as the original package required. |

## Things to check before you rely on them

- **The generated `marketplace.json` pins a local build commit.** `scripts/build_distribution.py` records the commit of whatever checkout it ran against. The copy shipped in `.claude-plugin/` uses a relative `./` source instead and is safe; regenerate the Git-pinned one from the real upstream repository before using it as a reviewable SHA selection.
- **`docs/source-obligations.json` is ~644 KB of full-text provenance** covering owner-supplied private source material (Project Foundry v3.2 segments). It is required by `scripts/verify_traceability.py` and was kept so that check still passes. It contains no credentials, but it does contain your private authored text — remove it if you intend to share this package.
- **The traceability ledger covers `1.1.0`, not `1.2.0`.** `docs/source-obligations.json` pins 39 destination rules to exact line ranges in `playbooks/1.1.0/`. That is why `1.1.0` had to stay frozen, and it means `verify_traceability.py` proves provenance for `1.1.0` only. `1.2.0`'s relationship to `1.1.0` is established instead by `diff -r playbooks/1.1.0 playbooks/1.2.0`, which shows exactly the five changed lines listed in `process-1.2-claude-port.md`.
- **`source` remains `https://github.com/R-AND-E-Inc/personal-workflows`.** That is a repository URL used for identity, not a credential, and the resolver validates that it carries no username, password, query, or fragment.

## Verification performed

- `python3 -m unittest discover -s tests` → 42 tests, all pass
- `python3 scripts/build_manifests.py --check` → all four releases verified
- `python3 scripts/verify_traceability.py` → `integrity_verified`, 663 source segments, 39 destination rules
- `python3 scripts/build_distribution.py` → reproducible plugin archive plus ten claude.ai Skill exports
- Live resolve against a real adopted repository → `mode: adopted`, release `1.1.0`, `identity_verified: true`
- Live bootstrap against an unadopted directory → `mode: bootstrap`, release `1.2.0`
- Live legacy route for the original seven skills → `mode: legacy`
- `work-deliver` without adoption → `adoption_required` refusal, unchanged
- Secret scan across all files → no tokens, keys, credentials, or machine-specific paths
