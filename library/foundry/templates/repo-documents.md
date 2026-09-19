# Repository Document Templates

Skeletons for everything generated at F10. Fill only what applies at the project's level; delete headings that do not. Definitions and rules: `references/document-package.md`.

---

## docs/PROJECT_STATE.md

```markdown
# <Project> — Project State

**Updated:** <date> · **Phase:** <NN title> · **Step:** <1–7> · **Gate:** <open/closed> · **Mode:** Unified/Split
<!-- Hard cap 4 KB. Status only. Locked behavior goes to docs/specs/locked-behavior.md. -->
**Main head:** <sha> · **Open PRs:** <list or none> · **Last green CI:** <sha>

## Exists now
## Does not exist yet
## Blockers and known issues
## Deploy / runtime / migration state
## Open configuration and research items
## Next exact action
<one line — the next session starts here>
```

---

## docs/PRODUCT_BRIEF.md

```markdown
# <Project> — Product Brief

**Level:** L? · **Last decision affecting this doc:** D-nn

## Vision
## Problem
## Users
## Primary jobs
## Core workflows
## Product principles
## Feature architecture
| Class | Capabilities |
|---|---|
| Foundation | |
| Core | |
| Enhancement | |
| Advanced | |
| Experimental | |
| Excluded | |
## Non-goals
## UX and design principles
## Device and responsive priorities
## Accessibility
## Trust and provenance
## Stable boundaries
```

---

## docs/OPERATING.md

```markdown
# <Project> — Operating Rules

Foundry v3 phase workflow applies. This file records how it is instantiated here.

## Branches and PRs
## Commands
- Install:
- Run locally:
- Targeted tests:
- Full suite:
- Lint / typecheck:
- Build:
## Review tiers for this project
- Low risk:
- Medium risk:
- High risk (list the high-risk areas of this codebase):
## Merge rules
- Required status check: <name> · enforced by branch protection: yes/no
- Workflow-only closeouts may merge early: yes/no (depends on the line above)
- Who authorizes merges:
## Phase-close tagging
- Mechanism: `Create phase tags` workflow triggered by the assistant via the GitHub connector / Actions tab by the owner / local push by the owner (read-only CI policy) — pick one.
- The tag goes on the commit carrying the closing record, not on the phase merge.
## Spec evolution
- Behavior is recorded as deltas in each contract and merged into `docs/specs/locked-behavior.md` at close. `locked-behavior.md` is never rewritten wholesale.
## Work grains used here
- Phase / change / hotfix — and what qualifies for the change path in this codebase.
## Model routing (by task nature, not phase risk)
- Strongest model: master planning, replans, adversarial review of high-risk work
- Workhorse: implementation, corrections, drift checks
- Cheapest: mechanical volume only; never persistence, migration, state machines, async lifecycle
- Corrections stay in the session that produced the work.
## Prompt budgets
- Planning / implementation / review / correction: <words each>; exceed only when the change cannot be specified safely within them.
## Deploy
## Rollback
## Who approves what
## Release cadence
```

---

## CLAUDE.md

```markdown
# <Project> — Agent Contract

Read `docs/PROJECT_STATE.md` before doing anything. Current phase plan is in `docs/plans/`.

## Architectural boundaries
## Security invariants
## Data invariants
## Testing requirements
## Code quality
## Scope rules
- Implement only the approved slice. New ideas go to `docs/backlog.md`.
- If repository reality invalidates the plan, stop and report; do not invent architecture.
## Prohibited shortcuts
## Environment and mode rules
## Where to look first
- `docs/PROJECT_STATE.md`, then the current phase contract in `docs/plans/`.
- `docs/specs/locked-behavior.md` when touching an area it covers.
- `docs/PHASE_HISTORY.md` is not a startup read; open it only when rationale is needed.
```

---

## docs/PHASE_HISTORY.md

```markdown
# <Project> — Phase History

## Phase NN — <title>  (closed <date>, tag `phase-NN-closed`)
- Scope and outcome:
- PRs:
- Summary:
- Evidence:
- Review findings and dispositions:
- Decisions changed:
- Waivers:
- Deferred:

## CHANGE <date> — <one line>  (PR #n, delta merged / none)
## HOTFIX <date> — <one line>
## RELEASE <version> <date> — checklist result, waivers
## INCIDENT <date> — what, impact, cause, fix, what changes
## OPS REVIEW <date> — broke / asked / stale / dependencies / runbook
```

---

## docs/plans/phase-NN.md

```markdown
# Phase NN — <title>

**Outcome:** <one observable outcome>
**Checkpoint:** <what the owner can do at the end that they could not do before>
**Risk class:** low / medium / high
**Branch / PR:**
**Mode:** Unified / Split
**Reclassification triggers checked:** <none / which, and what it changes>

## Scope
## Non-goals (3–7)
## Acceptance criteria
- AC-01 <objective, observable> — serves: <BEH-area-NN / R-nn / principle>
## Spec delta
<ADDED / MODIFIED / REMOVED / RENAMED requirements — or: none — reason>
## Locked decisions that apply
## Dependencies
## Required evidence
## Required review
## Slices
- S1 <one coherent behavior> — satisfies AC-01, AC-02 — verified by <action>, delivers <value>
```

---

## docs/specs/locked-behavior.md

```markdown
# <Project> — Locked Behavior

Current truth about how the product behaves, by area. Maintained by merging each contract's spec delta
at close — never rewritten wholesale. Read when touching an area. Not a startup read.

## <Area, e.g. Persistence and resume>

### BEH-persist-01 — Session resume
The system SHALL restore the reader to the exact position held at the last close.
#### Scenario: Reopening after a crash
- **WHEN** the app is reopened after a non-graceful exit
- **THEN** the last committed position is restored, and no progress written before the exit is lost
*Locked: Phase 4C, PR #18.*
```

The prose form — `- <rule> — Phase NN, PR #n` — is enough at L1–L2 for areas with no scenarios worth
enumerating. Use the `BEH-` form wherever acceptance criteria, tests, or reviews need to cite the behavior.

---

## .github/workflows/create-phase-tags.yml

Copy `templates/create-phase-tags.yml` verbatim at bootstrap. It creates annotated tags from `docs/history/phase-tags.tsv` or from single-tag inputs, is idempotent, and refuses to move an existing tag. Triggered by whichever mechanism `OPERATING.md` records; omit the file entirely on a project that tags locally.

---

## README.md

```markdown
# <Project>

<one paragraph: what it is, for whom>

## Setup
<from a clean checkout; prerequisites; `cp .env.example .env`>
## Run
## Test
## Deploy
<pointer to docs/runbook.md at L3+>
## Structure
## Working on this project
Read `CLAUDE.md`, then `docs/PROJECT_STATE.md`.
```

For L1 the README is the entire document package: add a five-line contract (what, for whom, does, does not, done when) and the acceptance criteria.

---

## docs/runbook.md (L3+)

```markdown
# <Project> — Runbook

## Deploy
## Rollback  (last rehearsed: <date>)
## Restore from backup  (last drill: <date>, duration: <n>)
## Alerts — what each means and what to do
## Degraded modes
## Contacts / on-call
```

Every procedure here has been executed at least once before F11 passes.
