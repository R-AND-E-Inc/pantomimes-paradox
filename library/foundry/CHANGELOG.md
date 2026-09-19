# Project Foundry — Changelog

## Version 3.2 — 2026-08-29

Two sources. The four open findings from real projects (28–31), and a study of two mature spec-driven toolkits — [OpenSpec](https://github.com/Fission-AI/OpenSpec) and [GitHub Spec Kit](https://github.com/github/spec-kit) — for mechanisms Foundry lacked. Both tools cover roughly Foundry's F7-to-implementation span and nothing of its discovery, risk, release, or operations stages; what they had that Foundry did not was a way to keep behavioral truth current without rewriting it, and a way to make consistency checking countable instead of judgmental. Those two things are the substance of this release.

Nothing was adopted as tooling. Both projects ship CLIs; both projects' gates are, on inspection, prompt-level instructions to an agent. Foundry keeps the formats and leaves the packages alone.

### Added

**Behavior deltas** (`phase-workflow.md`). Locked behavior is now recorded as a delta — ADDED / MODIFIED / REMOVED / RENAMED requirements with `BEH-` IDs and WHEN/THEN scenarios — written into the contract and merged into `docs/specs/locked-behavior.md` at close. MODIFIED carries the entire requirement block, because the merge replaces the whole block and a silently dropped scenario is the failure mode this format exists to prevent. Work with no behavior change writes `Spec delta: none — <reason>` rather than inventing a requirement. Adapted from OpenSpec's delta specs, with stable IDs added: OpenSpec identifies requirements by header text, which cannot survive a rename or be cited by a test.

**The change path** (`phase-workflow.md`). A third grain of work between a phase and a hotfix, for the small capability or behavior tweak that is most of what happens after M1. The whole artifact is the PR description: why · what changes · spec delta · tasks with their own verification · risk class. Steps 3 and 4 apply unchanged; the PR description replaces step 1; step 2 is skipped; steps 5 and 6 are conditional; step 7 applies except the tag. Logged as `CHANGE` in Phase History. Guarded against becoming a phase-avoidance loophole: two changes in a row against one area, or a change needing a second PR, means the work was phase-sized.

**Reconciling code against intent** (`phase-workflow.md`, Step 4). Gap typing — missing / partial / contradicts / unrequested — each naming its source ID, with unrequested code surfaced rather than deleted, and correction tasks as the pass's only write. Repeat until no missing or contradicting gap remains. Runs at Step 4 of medium- and high-risk phases, at the M1 reality check, and as the code half of F0-R. From Spec Kit's converge command.

**Question budgets** (`discovery-interview.md`). At most three open questions in a batch and three unresolved blocking unknowns at any time; past that, propose and label an assumption. Rank by impact × uncertainty. Questions must be answerable — a full question with two to four options or a few-word form; a topic heading is not a question. Each answer is encoded into the Worksheet as it lands, deleting what it supersedes in the same edit. A domain sweep marking clear / partial / missing closes F1. From Spec Kit's specify and clarify commands.

**The cross-document audit became a procedure** (`document-package.md`). Inventory of stable IDs; coverage checked in both directions with counts and a percentage; six named passes (duplication, ambiguity, underspecification, invariant conflict, coverage gaps, inconsistency); a findings table with severities where CRITICAL closes the gate; determinism required on re-run. It now also runs **before F8**, so the red team spends its attention on judgment rather than bookkeeping. From Spec Kit's analyze command — which infers task-to-requirement mapping by keyword because its tasks carry no IDs. Foundry has stable IDs, so the coverage check is countable rather than inferential; the supporting rule is that every AC cites what it serves and every slice cites its ACs.

**Checkpoints and independent tests** (`phase-workflow.md`). Each phase names the checkpoint it reaches — what the owner can do at the end that they could not do before — and each slice names its independent test in one line. M1 is redefined as simply the first checkpoint at which the primary job is doable end-to-end. A phase whose checkpoint the owner cannot perform is not finished. From Spec Kit's independently-testable user stories.

**Rule 16.** A request that opens or continues planning authorizes planning only, even when it asks you to build the thing. Implementation begins on a new instruction. From OpenSpec's planning boundary, which exists because agents reliably read "help me plan X" as permission to start X.

### Changed

- **Step 7 ordering (finding 31).** The tag goes on the commit carrying the closing record, not on the phase merge — a tag whose tree lacks its own Phase History entry cannot document the phase it names. Prefer folding the close-out updates into the phase PR so merge and close are one commit; otherwise tag the close-out commit. Delta merge is now step 2 of the close, before Project State.
- **Read-only CI is a supported tagging policy (finding 28).** Where CI deliberately holds no write token — a legitimate L4 choice — the owner or a local agent pushes the tag, and `OPERATING.md` records that as the project's mechanism rather than a workaround.
- **Master plans above ~50 KB must be split (finding 29)** into `docs/specs/NN-title.md` with section numbers preserved in filenames, plus a ~10 KB index holding the product contract and section map. "Read by section, by reference" is not achievable when a connector returns whole files. The split is a move verified by the zero-loss oracle, never a summary.
- **The F10 decomposition map was off by one and incomplete.** It had mapped Worksheet §7 to the
  Brief since v3.0, when the correct source became §8 — the shift dates from *Implemented reality*
  being inserted as §2 without renumbering the map. Corrected, and the four sections it never named
  (§1, §2, §3, §7) now have destinations, so bootstrap cannot silently drop part of the Worksheet.
- **Legacy projects keep their own names (finding 30).** A project that predates Foundry records the mapping once (S0.1 = Phase 0) instead of renaming, but M1 must be named even in a legacy plan.
- **Step 3** gains the anti-narrowing guard: scope is never absorbed silently in either direction. The named-deviation rule covered adding scope but not quietly dropping it.
- **Step 5 and F8** gain a severity dampener: when severity is genuinely uncertain, choose the lower one.
- **Scope change** gains amend-or-open-new: amend if the intent is unchanged and most scope still applies; open new if the intent moved. The deciding question is whether the current contract could be honestly closed without the idea.
- **OPERATING.md** gains spec evolution model, tagging mechanism, and work grains used; the phase contract skeleton gains checkpoint, spec delta, reclassification triggers checked, and AC-to-slice citation; Phase History gains a `CHANGE` entry; `locked-behavior.md` gains the `BEH-` form alongside the prose form.
- Core is **2,449 words** — whitespace-delimited tokens, the stricter of the two counts — under the 2,470 ceiling set in v3.1. Ten compressions paid for the additions, most of them removing text the playbooks already carried.

### Considered and not adopted

- **A CLI or an app.** The distribution problem those tools solve — thirty-plus agents, thousands of strangers — is not Foundry's. Their enforcement is prompt-level regardless, and Foundry already has a stronger gate available in CI and branch protection.
- **A separate dated clarifications log** (Spec Kit). The decisions and assumptions registries already own that content; a second log would be a second editable source of truth for the same subject. The timing rule was adopted; the artifact was not.
- **Semantically versioned constitution machinery** (Spec Kit). `CLAUDE.md` invariants plus locked decisions cover it with less apparatus.
- **Fully gateless fluidity** (OpenSpec). Right for the change grain, which is why the change path has no planning step; wrong for the discovery arc, where the gates are the quality mechanism.
- **Tests optional by default** (Spec Kit). Foundry's evidence rules are stricter and stay so.
- **Priority labels** (P1/P2). Feature classes already carry that information with more meaning.

### A caution on this release

Findings 1–27 came from a real migration. Findings 28–31 came from real projects. The six mechanisms adopted from OpenSpec and Spec Kit did not: they are proven in those tools' contexts, not yet in a Foundry project. Neither project has yet exercised the M1 reality check, a hotfix under real pressure, the F11 release gate, or the post-launch operating rhythm — and the change path in particular is designed for exactly the period none of them has reached. Treat the change path, the reconcile loop, and the audit procedure as v3.2's hypotheses. The first project to run them should record what turned out to be true.

---

## Version 3.1 — 2026-08-27

The first release shaped by a real project. Artax Lives — eleven phases, production on Vercel, 800 tests — was migrated from a v1-style Drive-plus-repo layout to the v3 single-surface model in two workflow-only phases (PRs #24 and #25). Twenty-seven findings came out of it: eight rules the project had discovered that Foundry lacked, several failure modes the migration exposed, and four defects in contracts Foundry's own author wrote. All are incorporated. Full list: `foundry-v3.1-findings.md` in the migration package.

### Rules learned from Artax (phase-workflow.md)

- **Rendered visual evidence** for visually judged criteria; DOM visibility proves presence, not perception.
- **Fail-closed verification scripts**: compute from primary data, nonzero exit, success-only marker, positive controls, counts derived not copied.
- **Exact deployment evidence** in the packet (immutable URL, status, represented SHA).
- **The packet is evidence to inspect, not a conclusion to inherit**; inspection scoped full/standard by risk; a contradicted claim closes the gate at any risk class.
- **One authoritative run on the post-review head** (v3.0 had "full suite before review," which is the wrong order); draft PR as staging surface.
- **Revision limits**: two failed attempts → fresh session; three correction rounds → scope review.
- **Workflow-only closeout rule**, with the branch-protection and draft-guard caveats made explicit.
- **Model routing and prompt budgets** as OPERATING.md sections.

### Failure modes fixed

- **Project State bloat.** Locked behavior is current truth but not status; it now lives in `docs/specs/locked-behavior.md`, and `PROJECT_STATE.md` has a 4 KB cap checked at close. Artax's had reached 50 KB.
- **Master plan at session open.** Session open is `CLAUDE.md` + `PROJECT_STATE.md` + the current phase contract. Master plans are read by section, by reference. The v3.0 wording was ambiguous enough that an AC was written against the wrong set.
- **History in the startup read**, and version changelogs inside current docs — both excluded by rule.
- **Sandbox refs are not evidence.** Base SHA verified against the remote before branching. A cloud sandbox's `main` was twelve commits stale.
- **Tag pushes can be refused.** Tags are now created by a dispatchable workflow (`templates/create-phase-tags.yml`), triggered by the assistant through the GitHub connector's `run_workflow`. The Actions tab is the fallback. The assistant owns phase-close tagging.
- **Reclassification triggers checked at Step 1** of every phase, not only when the level obviously changes.

### Contract hygiene (self-inflicted)

- Never write a size cap against an unmeasured file.
- Derive forbidden-string lists from the scope; run every mechanical AC against the contract's own mandated outputs before approval.
- A heading map is not a zero-loss oracle; body-level, fail-closed verification for `verbatim` rows.
- The implementer keeps mandated behavior and records a **named deviation** rather than editing content to satisfy a check.

### Added

- `document-package.md` → *Migrating an existing document set*: mapping table with Treatment column, body-level oracle, raw-bytes import, prior-snapshot import, old-location neutralization, measured startup-read AC.
- `release-and-operations.md`: when F11 runs relative to phases; client-side-only persistence handling; real-device gate for browser-facing products.
- `templates/create-phase-tags.yml` and a `locked-behavior.md` skeleton.
- Roles: the assistant is Claude or ChatGPT in work mode, vendor-agnostic; the coding agent is Claude Code.

### Changed

Core grew to ~2,470 words. That is now the ceiling.

---

## Version 3.0 — 2026-08-27

Extends the framework from "plan a project" to "carry a project through release and live operation," and removes the two-surface continuity model. Driven by three test runs against v2.0 (an L1 utility, an L3 SaaS, and an existing repository), which confirmed the gaps identified in review and found three more.

### Added

**F11 Release gate and an Operate stage** (`references/release-and-operations.md`). A level-scaled checklist between "works here" and "real users depend on it" — L1: runs and destroys nothing; L3: restore drill, alerting drill, rollback rehearsal, secret rotation, data lifecycle, legal basics, load sanity, supply chain, observability, support path; L4: adversarial review, environment isolation proven, golden-dataset verification on the release head, clean-machine recovery. Post-launch rhythm for incidents, feedback triage, reclassification, ops reviews, and sunset.

**Phase 0 defined** as the walking skeleton — the thinnest end-to-end slice through every architectural boundary, deployed, with CI and one real test. "Stage 0" was referenced throughout v1 and v2 and defined nowhere.

**M1 (first usable milestone) and the M1 reality check.** Named in F7; after it ships, real use feeds back into the Brief, feature classes, backlog, and level. The one mandatory replan point.

**Hotfix path.** Abbreviated contract in the PR, same evidence rules, no planning step, independent review only for high-risk areas, logged in Phase History.

**F0-R Reconcile** — a first-class entry for existing projects in the core. Read the repository first; separate implemented reality from documented intent; enter the lifecycle at the first unsatisfied stage. Previously this existed only as a prompt. Rule 15 added: read the repo before asking what it already answers.

**Compact path.** L1 runs F0 → F1+F2 → F5-lite → F7 (one phase) → build → F11-lite; the Worksheet is optional for single-session work and the README is the whole document package. L2 skips F8 unless a high-risk subsystem exists.

**Propose-then-confirm** as the default interview form. Recommended answers with alternatives; the owner corrects rather than composes. Open-ended questions reserved for the wedge, primary user, non-goals, hard constraints. Explicit **delegation** handling: "you decide" switches to propose-only with delegated decisions recorded as locked.

**Operating modes.** *Unified* (one agent plans and builds in the repo; default L1–L2) and *Split* (planner writes contracts and slice prompts, implementation agent executes; default L3–L4).

**README.md** for humans, and the optional **intake form** restored (dropped without note in v2.0).

**Worksheet** gains an *Implemented reality* section, mode, Phase 0 and M1 slots, and the L1 opt-out.

### Changed

**Single surface.** The repository holds everything from F0: `docs/WORKSHEET.md` through `docs/PROJECT_STATE.md`. Git tags (`phase-NN-closed`, `release-<version>`) are the immutable snapshots. The Drive-plus-repository model and its `10 - PHASE SNAPSHOTS` folder are gone; Drive or a wiki may hold read-only exports only. Reason: the two-surface model dates from assistants that could not touch a repository, and its reconciliation steps were the heaviest ceremony in the framework. Also, chat Drive connectors can create files but not update them, which broke the Worksheet update loop.

**Phase close** collapsed from twelve steps to six.

**Document package trimmed.** Handoff Brief removed (it duplicated Project State, the Brief, and the resume prompt). Operating Instructions is now `docs/OPERATING.md`, the project-specific instantiation of the phase workflow — commands, branch rules, review tiers, deploy/rollback — so a repository is self-sufficient without the skill installed. Execution Manual is now `README.md` plus `docs/runbook.md`. `CLAUDE.md` holds invariants only.

**Terminology.** Foundry *stages* F0–F11; phase workflow *steps* 1–7; *Phase 0*; *M1*. "Stage" no longer means three things.

**Banner** includes mode; post-bootstrap form includes phase, step, and head.

### File map v2.0 → v3.0

`templates/continuity-package.md` + `templates/implementation-package.md` → `templates/repo-documents.md`. `references/document-package.md` rewritten for the repo layout. `references/phase-workflow.md` rewritten. New: `references/release-and-operations.md`, `README.md`, `templates/intake-form.md`.

### Test evidence

`foundry-workspace/iteration-1/` holds the three v2.0 test runs and their findings. v3.0 should be tested the same way before further changes.

---

## Version 2.0 — 2026-08-27

Restructure for context efficiency and usability. **No methodology was removed.** Every rule, gate, schema, and protocol from v1.0 survives; the delivery changed.

### What changed

**Three-tier loading.** v1.0 asked an assistant to read five documents (~10k tokens) before learning anything about the project, then load more mid-conversation. v2.0 puts the entire method in one always-loaded core (`SKILL.md`, ~2,300 words) and defers six stage playbooks that load once, when their gate opens.

**Packaged as a skill.** Progressive disclosure is now enforced by the platform instead of by instructions the assistant has to remember to follow. The same structure works as Claude Project instructions + project knowledge, or as `CLAUDE.md` + `docs/` in a repository.

**Quality gates merged into the lifecycle.** v1.0 had eleven stage gates (F0–F10) and eleven quality gates (Q0–Q10) covering overlapping ground in two documents. v2.0 has one gate per stage, stated where the stage is defined. `12 - QUALITY GATES.md` is retired; its Q0 source-coverage check now lives in the F0 gate and its final cross-document audit in `references/document-package.md`.

**New: the Foundry Worksheet.** v1.0's documents began at F10, so all discovery state (F0–F9) lived only in conversation memory — which v1.0's own rule 9 forbids for consequential state. The Worksheet is one living file created at F0 and updated at every synthesis. A fresh session resumes by reading it and nothing else. At F10 it decomposes into the continuity package and retires to cross-phase references.

**New: the stage banner.** Every synthesis opens with `[Foundry F1 · L2 · Gate F1 open · 4 open items · Worksheet v3]`, so position is visible without re-reading anything.

**Deduplication.** `00 - START HERE` restated the Master Blueprint, Classification, and Scope docs; the README restated `START A NEW PROJECT`; Startup Prompts A–C restated the launch modes; the Portable Blueprint restated everything. All merged. Thirteen core files plus three launch/index files became one core, six references, and one prompts file.

**Checklists compressed to dimensions.** The 80-question interview bank, the 20-item architecture list, and the 23-item risk list were reference material a capable model does not need spelled out. They are now one-line prompts for judgment. The rules and gates — the part that actually changes behavior — kept their full weight.

**Portable Blueprint retired.** An 83 KB attachment sits in context on every turn, which was the exact problem the framework was trying to solve. Portable mode now means pasting the ~2,300-word core, with playbooks pasted on request.

**Drive escaping avoided.** Reading these files through a Drive connector adds 20–30% token overhead in backslash escapes. Keeping the core in skill/project instructions removes both that overhead and the per-file latency.

### Kept unchanged

The garden dry run, in full. It is the best teacher of the method's feel, and its length earns its place.

### Migration

Old v1.0 files can be archived. Projects already using v1.0 documents keep working: the authority order, five-document package, phase workflow, and phase-close transaction are identical.

---

## Version 1.0 — 2026-08-26

Initial formal release. Staged discovery before architecture; product/design/operating/implementation authority separation; risk-based phase planning; exact-candidate verification; five-document continuity; Drive + repository authority; immutable phase snapshots; scope and backlog discipline; red-team preflight; planning-sufficiency gate; complexity-scaled depth; synthetic and golden test data; current-state versus history separation.
