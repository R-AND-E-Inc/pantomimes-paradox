# Project Foundry — Prompts

Short by design: the method lives in `SKILL.md`. With the skill installed, launch prompts can be one line. The longer forms are for assistants without the skill loaded.

---

## Launch — new idea

```text
New Foundry project: <DESCRIBE IDEA>
```

Long form:

```text
Start a new project using Project Foundry.
My idea: <DESCRIBE IDEA>
I may add notes, documents, screenshots, or reference products.
Begin at F0. Create the repository and docs/WORKSHEET.md. Do not jump to a stack.
Use propose-then-confirm: recommend answers and let me correct them.
```

## Launch — with source material

```text
New Foundry project from the attached material.
Read it first. Begin F0 by separating explicit facts, inferred assumptions, constraints,
unresolved questions, contradictions, and opportunities. Do not assume it is a complete spec.
```

## Launch — existing project

```text
Bring this repository under Project Foundry (F0-R).
Read the code, tests, CI, and recent commits before asking me anything.
Separate implemented reality, documented intent, historical decisions, assumptions,
drift, and missing definition. Tell me which stages are already satisfied and enter at
the first that isn't. Preserve sound work; do not restart for template conformity.
```

## Delegation (add to any launch)

```text
You decide anything that doesn't change what the product does, who it's for, its level,
its cost, or what's irreversible. Record delegated choices as decisions and only ask me
about the rest.
```

## Resume — before bootstrap

```text
Continue <PROJECT> with Foundry. Read docs/WORKSHEET.md and start from "Next exact action".
```

## Resume — after bootstrap

```text
Continue <PROJECT>. Read CLAUDE.md, docs/PROJECT_STATE.md, and the current phase plan.
Check git log, open PRs, and last CI. Report any drift, then state phase, step, gate,
and next required evidence. Don't ask me to retell anything in those files.
```

## Phase 0 / new phase (Unified mode)

```text
Open Phase <NN> per docs/plans/phase-NN.md. Follow the seven steps. Fresh session, so
bootstrap from CLAUDE.md and PROJECT_STATE.md first.
```

## Implementation slice (Split mode — the planner fills this from the phase contract)

```text
Base: <sha of main, verified against GitHub — not the sandbox ref>
Read CLAUDE.md, docs/PROJECT_STATE.md, docs/plans/phase-NN.md, and the specs/decision IDs listed
there before editing.

Implement only slice S<n>:
OUTCOME: <one observable outcome>
SCOPE: <scope>
NON-GOALS: <3–7>
ACCEPTANCE CRITERIA: <AC-ids and exact criteria>
RISK / SPECIAL RULES: <high-risk areas that apply>
REQUIRED EVIDENCE: <tests and checks>

Do not broaden scope. If repository reality invalidates the plan, stop and report. If a mechanical
AC cannot be met without breaking a mandated behavior, keep the behavior and record a named deviation.
Open a draft PR. Return a completion packet with exact head, evidence per criterion, exact deployment
evidence, renders for visual ACs, and known limitations. Do not merge.
```

## Red-team review (fresh conversation)

```text
Fresh-context adversarial review of <PROJECT> using the Foundry red-team protocol.
Read docs/WORKSHEET.md (or docs/ if bootstrapped). Do not optimize for agreement.
For each material finding: severity, evidence, impact, disposition
(ACCEPT / BACKLOG / REJECT / RESEARCH / ACCEPT-RISK). Separate blockers from backlog.
```

## Phase close — tag

```text
Phase <NN> merged at <merge sha>. Complete the seven-step close from phase-workflow.md — delta
merged, Project State, registries, Phase History — then tag the commit that carries that closing
record (not the merge) using the mechanism docs/OPERATING.md records. If that is the workflow: run
"Create phase tags" with tag=phase-NN-closed, sha=<closing commit sha>, message="Phase NN — <title>".
Confirm the tag exists and that its tree contains the Phase History entry for phase NN.
```

## Change (smaller than a phase)

```text
Change on <PROJECT>: <what should be different>.
Use the Foundry change path. Confirm it qualifies (low/medium risk, one PR, no new boundary,
no locked decision contradicted, no reclassification trigger) — if it doesn't, tell me and stop.
PR description carries why, what changes, the spec delta (or none with a reason), tasks with their
own verification, and risk class. Exact-head evidence. Merge the delta at close and log it as CHANGE.
```

## Reconcile code against intent

```text
Reconcile <PROJECT> against its own documents. Read the phase contract, spec deltas, and
docs/specs/locked-behavior.md as the statement of intent, then audit the code.
Type every gap as missing / partial / contradicts / unrequested with its source ID.
Write nothing except correction tasks. Surface unrequested code, do not delete it.
Report converged only when no missing or contradicting gap remains — that word means the code and the documents agree, nothing more.
```

## Cross-document audit

```text
Run the Foundry cross-document audit on <PROJECT> before <F8 / F11>.
Inventory the stable IDs, check coverage in both directions with counts, run the six passes,
and return one findings table with severities and the document that owns each correction.
Read-only: propose corrections, don't make them. Don't report anything missing without opening the file.
```

## Hotfix

```text
Hotfix on <PROJECT>: <observed defect>.
Use the Foundry hotfix path: abbreviated contract in the PR, exact-head evidence,
independent review only if it touches a high-risk area. Log it in PHASE_HISTORY.
```

## Release (F11)

```text
Run the Foundry F11 release gate for <PROJECT> at level L<n>.
Work through the checklist; each item is PASS, WAIVED (with my approval and residual risk
recorded), or N/A with a reason. Do not mark a drill done unless it was actually performed.
Tag release-<version> when it passes.
```

## Portable mode (no skill, no filesystem)

Paste `SKILL.md`, then:

```text
Use the framework above as the process for this project — methodology, not requirements.
Begin at F0. Maintain the Worksheet and give me the updated file at the end of each session.
Tell me which reference to paste when a stage needs its playbook.
```
