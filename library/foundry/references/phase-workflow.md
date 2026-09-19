# Phase Development Workflow — F7 and every implementation phase

Read when F7 opens, at the start of each implementation phase, and before any hotfix, change, or reconcile. After discovery, implementation proceeds in repeatable, evidence-based units, not one long coding conversation.

Three grains of work, smallest first. **Hotfix** — a defect in the released product: *Behavior deltas* and *Hotfix path*, plus steps 3 and 4, and step 5 if it touches a high-risk area. **Change** — behavior too small for a phase: *Behavior deltas* and *The change path*, plus steps 3, 4, and 7, with steps 5 and 6 conditional. **Phase** — everything else: the whole file.

## Phase 0 — the walking skeleton

Always the first phase. The thinnest end-to-end slice through every major boundary the architecture defines: UI (if any) → logic → persistence → deployment target, with CI running and one real test proving the path. It delivers almost no user value on purpose; it proves the architecture and the toolchain. Objective criteria only: "`GET /health` returns 200 from the deployed environment; CI runs the suite on every PR; one record round-trips through storage."

## M1 — first usable milestone

Named in F7: the earliest phase after which the owner (or a real user) can do the primary job end-to-end, however roughly. When M1 ships, run the **M1 reality check** before planning the next phase: use it for real for a few days; record what changed in the Brief, feature classes, backlog, and level; update `docs/decisions.md`. This is the one mandatory replan point.

## Behavior deltas

Locked behavior is recorded as a **delta** — what this phase or change adds, alters, or removes — never as a rewrite of the whole specification. The delta lives in the contract; at close it merges into `docs/specs/locked-behavior.md`, which is the product's current behavioral truth.

```markdown
## ADDED Requirements
### BEH-<area>-NN — <name>
The system SHALL <normative statement>.
#### Scenario: <name>
- **WHEN** <condition>
- **THEN** <observable outcome>

## MODIFIED Requirements
### BEH-<area>-NN — <name>        <!-- the entire block, rewritten -->

## REMOVED Requirements
### BEH-<area>-NN — <name> — reason · migration

## RENAMED Requirements
- `BEH-<area>-NN` — FROM "<old name>" TO "<new name>"
```

- **IDs are stable and never reused.** A requirement keeps its ID through renames and rewrites. That is what lets acceptance criteria, slices, and tests cite behavior instead of describing it.
- **MODIFIED carries the entire requirement block**, every surviving scenario included, because the merge replaces the whole block. A scenario that still applies but is missing from the block is a defect in the delta, not a decision to drop it. Copy the current block, then edit it.
- **Every requirement has at least one scenario** in observable WHEN/THEN form. A requirement with no scenario is a preference, not a specification.
- **A unit of work with no behavior change writes `Spec delta: none — <reason>`.** Never invent a requirement to fill the section; refactors, tooling, documentation, and infrastructure legitimately have none.
- **Merging happens at close, before the tag**, and each merged requirement records the phase or PR that locked it.

At L1 this is one line per behavior in the README. It earns its structure at L2+, where the alternative is rewriting a growing document by hand every phase and silently losing detail.

## The seven steps of a phase

**1. Contract.** One observable outcome · exact scope · 3–7 non-goals · acceptance criteria with stable phase-qualified IDs (`AC-5C-01`) · **spec delta** (or `none` with a reason) · **checkpoint** — what the owner can do at the end that they could not do before · relevant locked decisions · dependencies · risk class low/medium/high · branch/PR target · required evidence and review classes. Write it to `docs/plans/phase-NN.md`.

**Every criterion cites what it serves** — a `BEH-` requirement, a risk control, a product principle — and every slice cites the AC IDs it satisfies. This costs seconds while writing the contract and makes coverage countable afterwards: an AC no slice claims, or a risk control no AC enforces, is then found by reading a table instead of by remembering.

Also at Step 1: **check the reclassification triggers** for this phase's scope (accounts, payments, public exposure, sensitive data, autonomous actions, irreversible operations). A phase that introduces one changes the level of the subsystem it touches, and the release gate grows accordingly.

**Contract self-check before approval.** Every mechanical AC (a size cap, a grep, a count) is run against the contract's own mandated outputs and against measured inputs. A threshold written against a file you have not measured, or a forbidden-string list that contains a phrase the scope requires, is a defect in the contract, not the implementation. If an input is unknown, the AC is not yet writable.

Weak criterion: "the planner works well." Strong: "a user can place, resize, move, and delete a bed; refresh preserves exact geometry; overlaps follow the approved collision rule."

*Exit:* no unresolved product decision blocks implementation.

**2. Plan when required.** Low-risk: skip. Medium/high-risk: inspect the real repository first — current behavior, affected modules, data/schema changes, sequence, tests, migration/compatibility, risk areas, open implementation decisions. Derive PR-sized slice plans from the phase contract; never re-plan the whole program each session. Approved master plans are committed under `docs/plans/` and referenced by path, never pasted. *Exit:* plan approved or explicitly unnecessary.

**3. Implement one coherent slice.** Verify the base SHA against the remote host before branching — a sandbox's local view of `main` is not evidence and can be stale. Stay in scope; inspect source before editing; keep `CLAUDE.md` invariants; tests move with behavior; synthetic fixtures where data is sensitive; no opportunistic refactors; one **draft** PR. New ideas → `docs/backlog.md` unless required for correctness, security, or an approved dependency.

If the contract cannot be satisfied as written, keep the mandated behavior and record a **named deviation** with the exact residual output in the packet. Never edit content purely to satisfy a mechanical check.

The opposite failure is quieter. When a task turns out to need work beyond the contract, or you are tempted to drop, narrow, defer, or accept an exception to specified behavior, surface it and ask. Scope is never absorbed silently in either direction.

*Completion packet (the PR body):* summary · systems changed · one row per AC (status, oracle, environment, exact-head evidence, limitations) · targeted test results · **exact deployment evidence** (immutable preview URL, status, represented SHA — a branch alias is not exact-head evidence) · **rendered desktop and mobile screenshots for every visually judged AC** · known compromises and unverified claims · exact head.

**4. Verify the exact candidate.** Targeted checks during implementation and review. The **one complete authoritative run** happens on the post-review head; any later change is a new head needing a new run. The draft PR is the staging surface until then. Investigate failures instead of raising retries, timeouts, or skips. A waiver is `WAIVED`, never `PASS` — record scope, owner, reason, residual risk.

**The packet is evidence to inspect, not a conclusion to inherit.** Inspection is scoped by risk: *full* (PR, exact diff, review threads, CI directly) for high risk, any red or suspicious run, experiential ACs, or a packet/evidence discrepancy; *standard* (CI green on the exact head; packet against ACs; sampled diff) otherwise. A packet claim contradicted by CI or the diff closes the gate at any risk class.

**Rendered evidence.** DOM visibility proves presence, never perception. Visually judged criteria require representative renders from the exact-head deployment; a local production render is pre-review evidence only, labeled local.

**Verification scripts.** Any repository-owned script cited as evidence computes its claim from primary data, exits nonzero on failure, and prints one success-only marker only after every assertion passes. Absence checks need a positive control. Reported counts derive from raw output, not from the summary being certified. Documentation migrations are verified under the same rule (see `document-package.md`).

**Reconciling code against intent.** Verification asks whether the candidate meets its criteria. Reconciliation asks the wider question: does the code match what the contract, the delta, and locked behavior actually say? Read the artifacts as the statement of intent, audit the code against them, and type every gap:

- **missing** — required behavior with no implementation
- **partial** — implemented, but not to the requirement
- **contradicts** — implemented differently from what the requirement says
- **unrequested** — implemented, but nothing requires it

Each gap names its source (`AC-5C-01`, `BEH-reader-03`, a `CLAUDE.md` invariant). Missing and contradicting gaps against this phase's criteria are corrections; a partial gap is a correction or a named deviation; **unrequested code is surfaced, never silently deleted** — it goes to the owner as a decision or to `docs/backlog.md`. The only thing this pass writes is correction tasks. Repeat until a pass finds no missing or contradicting gap. That state is **converged**, and it is all the word means: the code and the documents now say the same thing. It is not a claim that either is good.

Run it at Step 4 of medium- and high-risk phases, at the M1 reality check, and as the code half of F0-R.

Older-head evidence explains history; it never certifies the merge head.

**5. Independent review by risk.** Low: none. Medium: when architecture, state, UX complexity, integration uncertainty, or evidence warrants. High: fresh-context review required (new session or subagent). Findings carry severity, evidence, location, impact, narrow correction. When severity is genuinely uncertain, choose the lower one: an inflated finding costs a correction round, and a reviewer who inflates is discounted the next time it matters. The reviewer's report is itself evidence; verify it covered the highest-risk seams on the exact head. Re-review only when a correction adds substantial logic or leaves material uncertainty.

**Revision limits.** Combine findings on the same system into one correction. Don't polish report wording when code and evidence are right. Two failed attempts on one defect → fresh implementation session. Three meaningful correction rounds → scope review; split or defer. A data-loss, security, migration, or architecture defect keeps the gate closed regardless of schedule.

**6. Experiential review.** Only what automation cannot judge: hierarchy, readability, interaction feel, device behavior, real-world workflows, tone, known compromises. Begins after rendered evidence has been independently reviewed — this step is product judgment, not first visual QA. Never ask the owner to re-run automated tests. Infrastructure-only phases may have none.

**7. Close.** Merged ≠ closed. In order:

1. Confirm merged main head, required CI green on that head, deployment/migration state.
2. Merge the spec delta into `docs/specs/locked-behavior.md`, recording the phase or PR that locked each requirement.
3. Update `docs/PROJECT_STATE.md` — what exists, what does not, blockers, next exact action. **Hard cap 4 KB.** If it is growing, locked behavior is leaking in; step 2 is where it belongs.
4. Update changed `decisions.md` / `assumptions.md` / specs / TDRs / `CLAUDE.md` invariants.
5. Append the phase to `docs/PHASE_HISTORY.md`.
6. Tag `phase-NN-closed`. **The tag goes on the commit that carries the closing record, not on the phase merge** — a tag whose tree lacks its own Phase History entry cannot document the phase it names. Prefer folding steps 2–5 into the phase PR so that merge and close are one commit; otherwise tag the close-out commit that follows. Create it with the `Create phase tags` workflow (`templates/create-phase-tags.yml`), triggered by the assistant through the GitHub connector's `run_workflow`; the owner runs it from the Actions tab if the connector lacks Actions write. **Where CI is deliberately read-only** — a legitimate L4 policy — the owner or a local agent pushes the tag instead. `OPERATING.md` records which mechanism this project uses. Sandboxed coding agents typically cannot push tag refs. The tag is the immutable snapshot; nothing is copied.
7. Write the next-session prompt into Project State's *Next exact action*.

**Workflow-only closeout.** Low-risk documentation, workflow, or storage changes after product acceptance may merge without the product matrix when the owner approves, the change is statically inspected, product code is untouched, and any first-execution limitation is recorded as `WAIVED`, not `PASS`. If CI runs the matrix anyway (draft-guarded repos run it on ready-for-review), let it run and record the result. If branch protection enforces the check, this rule is aspirational; `OPERATING.md` should say which.

Major phases begin in a fresh session bootstrapped from `CLAUDE.md`, `docs/PROJECT_STATE.md`, and the current phase contract.

## Hotfix path

For a defect in the released product. Do not open a phase.

1. Abbreviated contract in the PR description: observed defect · one acceptance criterion that proves it fixed · spec delta, since a fix that changes released behavior changes locked behavior (or `none — restores specified behavior`) · risk class · evidence required.
2. Skip Step 2. Steps 3–4 apply unchanged, including exact-head evidence and rendered evidence if visual.
3. Step 5 applies if the fix touches a high-risk area (auth, money, persistence semantics, permissions, destructive actions, async lifecycle).
4. Deploy; verify in the released environment.
5. Merge any delta into `docs/specs/locked-behavior.md`. Log under the current phase in `docs/PHASE_HISTORY.md` as `HOTFIX`; add a backlog or risk entry if the defect exposed a class of problem. No tag.

## The change path

Between a phase and a hotfix lies a third grain, and most work after M1 is this size: a small capability, a behavior tweak, a layout or copy change the owner asked for. Opening a phase for it costs more than the work does; calling it a hotfix loses the record of why it happened.

Use the change path when **all** of these hold: low or medium risk, fits one PR, needs no new architectural boundary, contradicts no locked decision, triggers no reclassification. Otherwise open a phase.

The whole artifact is the PR description:

- **Why** — one or two sentences.
- **What changes** — bullets; breaking changes marked **BREAKING**.
- **Spec delta** — behavior added, altered, or removed, or `none — <reason>`.
- **Tasks** — a checklist in which each item states its own verification.
- **Risk class** and the evidence required.

The PR description replaces step 1 and step 2 is skipped. Steps 3 and 4 apply unchanged — exact-head evidence, rendered evidence for visual criteria. Step 5 applies only if the change touches a high-risk area; step 6 when a person has to judge the result. Step 7 applies except the tag: confirm the head and CI, merge the delta into locked behavior, update Project State, update any decision, assumption, or `CLAUDE.md` invariant the change touched, and log it in `docs/PHASE_HISTORY.md` as `CHANGE` rather than as a phase. Tag only if the owner wants one.

**This is not a way to avoid a phase.** Two changes in a row against the same area, a change that needs a second PR, or a change whose delta touches a requirement another open change is also editing — each means the work was phase-sized. Stop and open one.

## Slice design

Good slices create one coherent behavior, are independently reviewable, have bounded risk, produce useful evidence, avoid sprawling cross-cutting change. Bad: "build the whole backend", "finish all UI", "refactor everything while adding X", cleanup bundled with a high-risk behavioral change.

**Each slice names its independent test** in one line — "verified by <action>, delivers <value>" — and each phase names the **checkpoint** it reaches: what the owner can do at the end that they could not do before. A phase whose honest checkpoint is "the code is better structured" is an infrastructure phase and should say so plainly. A phase whose checkpoint the owner cannot perform is not finished. **M1 is simply the first checkpoint at which the primary job is doable end-to-end.** Order slices so the checkpoint is reachable as early as possible; a slice that pays off only when a later slice lands is a sequencing smell.

## Exact-head evidence

Evidence names the exact candidate it certifies. The failure it prevents: commit A passes CI → code moves to B → docs still cite A's green run → B merges as though tested.

## Scope change mid-implementation

If reality invalidates approved architecture: stop the affected work → report the contradiction → decide whether a narrow replan solves it → update contract and `decisions.md` if approved → continue only once authority is clear. Adding an attractive unrelated feature is not this; that goes to backlog.

**Amend or open new?** When an idea lands against work already contracted, amend the existing contract if the intent is unchanged and most of its scope still applies; open a new phase or change if the intent itself moved. Amending preserves context; a new unit gives clarity. When both look defensible, ask whether the current contract could be honestly closed without the idea — if it could, the idea is a new unit.

## Post-implementation learning

Implementation legitimately reveals opportunities, simplifications, unnecessary planned features, better sequencing, provider limits, UI revisions. Fold them in through decisions and backlog. The Master Plan is not sacred text.
