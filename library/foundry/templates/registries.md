# Registry Templates

Small, high-leverage records. Before bootstrap they live in the Foundry Worksheet; after bootstrap they become repository-owned files (`docs/decisions.md`, `docs/assumptions.md`, `docs/open-items.md`, `docs/risks.md`, `docs/backlog.md`, `docs/tdr/`, `docs/specs/locked-behavior.md`).

## Decision Log

```markdown
### D-01 — <statement>
- **Status:** proposed / accepted / superseded by D-nn
- **Date / version:**
- **Rationale:**
- **Alternatives considered:**
- **Consequences and tradeoffs:**
```

A decision is not an assumption. Never change a locked decision silently.

## Assumptions Registry

```markdown
### A-01 — <statement>
- **Source:**
- **Confidence:** high / medium / low
- **Date verified:**
- **What depends on it:**
- **Reverify when:**
- **If false:**
```

External vendor facts belong here or in a TDR, never frozen into architecture.

## Open Items

```markdown
| ID | Question / decision required | Why it matters | Resolve by | Owner | Blocking? |
|----|------------------------------|----------------|-----------|-------|-----------|
| Q-01 | | | F5 | | no |
```

## Tooling Decision Record

```markdown
### TDR-01 — <requirement>
- **Candidates:**
- **Current verified capabilities:**
- **Pricing / limits (if material):**
- **Evidence source and date:**
- **Selected:**
- **Fallback:**
- **Revalidation trigger:**
```

## Risk Register

```markdown
| ID | Risk | Cause | Consequence | Likelihood | Severity | Control | Detection | Residual | Owner/Phase | Status |
|----|------|-------|-------------|-----------|----------|---------|-----------|----------|-------------|--------|
| R-01 | | | | | | | | | | open |
```

Qualitative likelihood is more honest than invented numbers.

## Locked Behavior (`docs/specs/locked-behavior.md`)

`BEH-<area>-NN` requirements with WHEN/THEN scenarios, each recording the phase or PR that locked it.
Written as deltas in a contract (ADDED / MODIFIED / REMOVED / RENAMED) and merged here at close; IDs are
stable, never reused, and survive renames. Delta grammar and merge rules: `references/phase-workflow.md`.
Skeleton: `templates/repo-documents.md`.

## Backlog

```markdown
### B-01 — <title>
- **User problem:**
- **Proposed capability:**
- **Why it matters:**
- **Dependencies:**
- **Rough complexity / risk:**
- **Recommended timing:**
- **Disposition:** next-phase candidate / product backlog / research backlog / rejected
- **Related:** D-nn, R-nn
```

Do not fully design backlog items when they are filed.
