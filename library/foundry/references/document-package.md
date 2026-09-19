# Document Package and Repository Layout — F10 and post-bootstrap sessions

Read when F10 opens, when the cross-document audit runs (before F8, at F10, before F11), and when a post-bootstrap session needs to know where something lives. Objective: persistent project memory with clear roles, not documentation volume. The conversation is disposable; the repository is persistent.

## Generation rules

1. Create a document only when the level justifies it (see the core's level table), never because this file lists it.
2. Each document answers one question and holds one kind of authority.
3. No duplicate editable sources of truth. Exports for reading elsewhere are read-only.
4. Stable IDs (`D-` decisions, `A-` assumptions, `Q-` open items, `R-` risks, `B-` backlog, `AC-` acceptance criteria, `BEH-` locked behavior) wherever traceability matters. IDs are never reused and survive renames.
5. Current-state documents stay compact; deep detail lives in plans and specs.
6. History is tagged and appended, never rewritten.
7. Prose never substitutes for executable acceptance evidence where tests are possible.
8. No real sensitive production or customer data in docs, prompts, PRs, or tests unless the approved security model requires and protects it. Use synthetic fixtures and stable fake identifiers.
9. Current-state documents carry a version number; the history of versions lives in `PHASE_HISTORY.md` under "Workflow history," never inside the document itself.
10. `PROJECT_STATE.md` has a hard cap of 4 KB. Locked behavior per area — "the reader does X, decided at Phase 4C" — is current truth but not status; it lives in `docs/specs/locked-behavior.md` and is read only when touching that area.

## Repository layout

```
CLAUDE.md                     engineering invariants the coding agent always follows
README.md                     what it is, how to run it, how to develop it
.github/workflows/
  create-phase-tags.yml       dispatchable tag workflow (templates/); used where OPERATING.md names it as the mechanism
docs/
  WORKSHEET.md                F0–F10 only; archived to docs/history/ at bootstrap
  PROJECT_STATE.md            where exactly are we now — current truth only
  PRODUCT_BRIEF.md            what are we building and what should it be like
  OPERATING.md                this project's instantiation of the phase workflow
  PHASE_HISTORY.md            how we got here — phases, hotfixes, releases, incidents, ops reviews
  MASTER_PLAN.md              governing spec and program (L2 with >3 phases; L3–L4)
  decisions.md · assumptions.md · open-items.md · risks.md · backlog.md
  plans/phase-NN.md           phase contracts — read at session open
  plans/<program>-master-plan.md   program-level authority — read by section, by reference, never at session open
  specs/locked-behavior.md    per-area locked behavior with the phase/PR that locked it — read when touching that area
  specs/                      domain, data, API, AI-eval, threat model, design system — when justified
  tdr/                        tooling decision records
  runbook.md                  deploy, rollback, restore, alerts, on-call — L3+
  history/                    archived Worksheet, superseded plans
```

**A master plan larger than a connector can return is not readable by section.** Above roughly 50 KB, split it into `docs/specs/NN-title.md` files with the section numbers preserved in the filenames, plus an index of about 10 KB holding the product contract and the section map. The split is a move, verified by the *Zero-loss oracle* under *Migrating an existing document set* below — never a summary.

Git tags: `phase-NN-closed`, `release-<version>`. They are the snapshots from the commit that introduced `docs/` onward. Nothing is copied to a snapshot folder. Tags are created by whichever mechanism `OPERATING.md` records, on the commit carrying the closing record; see `phase-workflow.md` step 7.

## The documents

| Document | Question it answers | Content | Rule |
|---|---|---|---|
| **PROJECT_STATE.md** | Where exactly are we now? | date · phase/step/gate · mode · main head · exists now · not yet · blockers · CI/deploy/migration state · open config/research items · **next exact action** | Current truth only. No narrative. Never paste the plan here. |
| **PRODUCT_BRIEF.md** | What are we building and what should it be like? | vision · problem · users · jobs · core workflows · principles · feature architecture summary · non-goals · UX/design principles · device priorities · accessibility · trust/provenance · stable boundaries | Durable intent. Changes only via a decision record. |
| **OPERATING.md** | How does *this project* run its phases? | branch and PR rules · CI commands · test commands and what "full suite" means · review tiers by risk for this project · deploy and rollback commands · **merge rules, including whether branch protection enforces the required check** · **spec evolution model** · **which tagging mechanism this project uses** · model routing by task nature · prompt budgets · who approves what · release cadence | Project-specific instantiation of `phase-workflow.md`, so the repo is self-sufficient without the Foundry skill. Do not restate Foundry philosophy. |
| **CLAUDE.md** | What must the coding agent never violate? | architectural boundaries · security invariants · data invariants · testing requirements · code quality rules · scope rules · prohibited shortcuts · environment/mode rules · where to look first (and that `PHASE_HISTORY.md` is not a startup read) | Invariants only. Process lives in OPERATING.md; status in PROJECT_STATE.md. Keep it short enough to read every session. |
| **PHASE_HISTORY.md** | How did we get here? | per phase: id/title · scope/outcome · PRs · summary · evidence · review findings and dispositions · decisions changed · waivers · deferred work. Plus `HOTFIX`, `RELEASE`, `INCIDENT`, `OPS REVIEW` entries. | Append-only narrative. Never authority. |
| **MASTER_PLAN.md** | What is the full specification and program? | product contract · scope/principles · system architecture · data architecture · modules · integrations · UX/design system · security/privacy/reliability · AI architecture if relevant · functional and nonfunctional requirements · test strategy · phased program · risk register · open items | Drop headings that do not apply. |
| **specs/locked-behavior.md** | How does the product behave today? | `BEH-` requirements with scenarios, by area, each recording the phase or PR that locked it | Current behavioral truth. Maintained by merging spec deltas at close, never by rewriting. Read when touching an area; not a startup read. |
| **README.md** | How do I run and develop this? | purpose · setup from clean checkout · environment variables (`.env.example`) · run · test · deploy pointer · structure overview | For humans and agents alike. |
| **runbook.md** | What do I do when it is 2 a.m.? | deploy · rollback · restore from backup (with the last drill date) · alert meanings · degraded modes · contacts | L3+. Every procedure has been executed at least once. |

Registries (`decisions`, `assumptions`, `open-items`, `risks`, `backlog`, `tdr/`) and `specs/locked-behavior.md`: field definitions in `templates/registries.md`; the `locked-behavior.md` skeleton is in `templates/repo-documents.md`.

## Optional artifacts (when justified)

Threat model · data model/contract · API spec · AI evaluation plan (tasks, datasets, metrics, failure classes, regression tests, human review) · golden dataset spec · design system · accessibility spec · privacy/data lifecycle spec · migration/compatibility plan.

## F10 procedure

1. Confirm `PLANNING SUFFICIENT` is declared in the Worksheet.
2. Decompose the Worksheet: §8 → `PRODUCT_BRIEF.md`; §4 → `decisions.md`; §5 → `assumptions.md`; §6 → `open-items.md`; §9 → Brief's feature section; §10–11 → Brief and `specs/` or `MASTER_PLAN.md`; §12 → `risks.md`; §13 → `plans/phase-00.md` and `MASTER_PLAN.md`; §14 → `risks.md`/`backlog.md`; §15 → `backlog.md`. §1 seeds the Brief's vision; §2 (implemented reality) informs `PROJECT_STATE.md` and the first `PHASE_HISTORY.md` entry; §3 (confirmed facts) distributes into the Brief's constraints and the relevant specs; §7 (recommendations still pending) goes to `backlog.md` or is dropped with the owner's agreement — nothing in the Worksheet is left without a destination or an explicit decision to drop it. (Section numbers are the Worksheet's own; verify them against `templates/foundry-worksheet.md` rather than from memory.)
3. Write `CLAUDE.md`, `OPERATING.md`, `README.md` (and `runbook.md` skeleton at L3+).
4. Write `PROJECT_STATE.md` with *Next exact action* = "Phase 0: <first slice>".
5. Create `docs/specs/locked-behavior.md` — empty at bootstrap unless behavior is already implemented; it fills by delta merge from Phase 0 onward.
6. Move the Worksheet to `docs/history/WORKSHEET-final.md`. Commit. Tag `bootstrap`.
7. Run the cross-document audit (below) for L2+.
8. Produce the Phase 0 prompt from `prompts.md`.

## Cross-document audit (L2–L4, before F8, at F10, and before F11)

A mechanical consistency pass, not a judgment pass. It finds bookkeeping failures so that the red team can spend its attention on substance — which is why it runs *before* F8, not instead of it. It is read-only: it produces findings; corrections are a separate, approved step.

**1. Inventory.** List every stable ID and where it is defined: `D-` · `A-` · `Q-` · `R-` · `B-` · `AC-` · `BEH-`.

**2. Coverage, in both directions.** Every Brief capability appears in a phase, and every phase outcome traces to a Brief capability. Every risk control is enforced by an acceptance criterion, and every AC cites what it serves. Every AC is claimed by a slice, and every slice cites its ACs. Every UX principle is reflected in at least one phase. Report counts and a percentage, not an impression.

**3. Six passes.**

| Pass | Looks for |
|---|---|
| Duplication | the same requirement stated twice, in different words, in two documents |
| Ambiguity | unquantified adjectives — fast, robust, intuitive, seamless, secure, scalable — where a number or a named oracle is possible; `TBD`, `TODO`, `???` |
| Underspecification | a verb with no object or outcome; a criterion with no oracle; a task naming a file or module that does not exist |
| Invariant conflict | anything contradicting `CLAUDE.md`, a locked decision, or the approved security model |
| Coverage gaps | the misses from step 2, both directions |
| Inconsistency | terminology drift; entities in the architecture absent from the Brief; stale vendor facts; contradictory ordering; unexplained hard constraints |

**4. Findings.** One table: ID (pass initial plus number), severity, location, a one-line statement, the correction, and which document owns it. Severity is **CRITICAL** (contradicts an invariant, a locked decision, or the security model; a blocking requirement with no coverage), **HIGH** (conflicting or duplicated requirements; an untestable criterion on consequential behavior), **MEDIUM** (drift, missing non-functional coverage, an underspecified edge case), or **LOW** (wording). A CRITICAL finding closes the gate.

**5. Determinism.** The same documents produce the same findings, the same IDs, and the same counts on a re-run. If they do not, the pass is guessing. Never report a section as missing without opening the file.

Also check, as always: history inside `PROJECT_STATE.md` · a current-state document carrying its own version history · open items with no resolution timing · scope leaking from the backlog into a contract · stale assumptions · the startup prompt pointing at the wrong files.

## Migrating an existing document set (F0-R for a post-bootstrap project)

When a project already has documents elsewhere — Drive, a wiki, a previous framework — F0-R is a map-and-move, run as a **workflow-only closeout phase between two product phases**, never inside one.

1. **Mapping table** in the phase contract: every source document → destination, with a **Treatment** column: `verbatim` / `merged` / `rewritten`. Split any "current state" document that has accumulated locked behavior, architecture, or product overview.
2. **Zero-loss oracle.** A heading map is not enough — a passage under a mapped heading can vanish silently. Verify `verbatim` rows mechanically: for every source section, a distinctive body line (the longest works) must appear in the declared destination; fail closed; report the count. `merged` and `rewritten` rows are excluded from the byte check and inspected by reading. Commit the map as `docs/history/migration-map.md`.
3. **Read the sources as raw bytes**, not through a connector's rendered text, which may escape markdown. Record a hash per imported file.
4. **Prior snapshots.** Retroactive tags on old merges mark history but cannot recover document states that lived outside the repo. Import them under `docs/history/snapshots/<phase>/` (small, obviously non-authoritative, removes the external dependency) or state explicitly that the external archive is retained and why.
5. **Neutralize the old location** only after merge: replace it with a pointer to the repository; keep originals recoverable for a period; then retire.
6. **Startup-read AC.** Measure before writing: the AC compares `CLAUDE.md` + `PROJECT_STATE.md` + the current phase contract against a cap, and excludes program-level master plans.

## Read-only exports

If the owner wants documents readable outside the repo (Drive, a wiki, a phone), export copies and mark them `EXPORT — not authoritative — see repo`. Never edit an export.
