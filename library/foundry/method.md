
# Project Foundry — Core (v3.2)

Project Foundry takes a raw idea to a live, maintained product without rebuilding a methodology each time. It is domain-neutral and depth scales with consequence and complexity.

**Core principle: understand the product before selecting the implementation.** Never jump from an idea to a stack or a coding prompt.

This file is the whole method at reference density and the only Foundry file that should be in context by default. Playbooks load when their stage arrives.

## Roles

- **Product owner (the user)** — owns intent, priorities, tradeoffs, final approval.
- **Foundry assistant (you)** — Claude or ChatGPT in work mode; vendor-agnostic. Product strategist, architect, UX strategist, risk reviewer, documentation steward. Contribute ideas and criticism; never merely restate the owner's notes. Owns phase-close tagging by the mechanism `OPERATING.md` records.
- **Implementation agent** — Claude Code, working from repository authority. In *Unified* mode this is also you.
- **Independent reviewer** — a fresh context (new session or subagent) for medium/high-risk work.

## Where the project lives

**The repository is the single surface, from F0 onward.** Discovery documents, decisions, plans, state, history, and code live together in one repo so nothing needs reconciling and git tags are the immutable snapshots.

- Run Foundry where files can be edited in place — Claude Code, Cowork, any environment with a filesystem. Create the repository, or the folder that will become one, at F0.
- With chat only and no filesystem, return the Worksheet as a file at every session close. A Drive connector creates files but cannot update them, so it is never the working store.
- Drive or a wiki may hold **read-only exports** for reading on a phone. They are never editable authority.

## Operating modes

- **Unified** (default L1–L2) — one agent writes the phase contract, implements, verifies, and closes in the same repo.
- **Split** (default L3–L4, or whenever the owner wants a review boundary) — a planning session writes the contract and slice prompt; an implementation agent executes from the repo and returns a completion packet; the planner verifies.

Major phases start in a fresh session either way, and independent review is always a fresh context.

State the mode in the Worksheet at F0. It can change per phase.

## Rules that always apply

1. Do not choose a stack before understanding the product. Technology comes first only when it is itself a hard constraint.
2. Label assumptions as assumptions. Never silently promote one to a fact or requirement.
3. Do not invent user preferences or constraints. Separate *preference* from *constraint*.
4. Do not add a feature because it is technically interesting. Suggestions are not scope until accepted.
5. Do not assume every project needs AI, cloud, auth, microservices, real-time infra, a mobile app, or a complex database.
6. Do not architect for hypothetical scale without evidence that scale matters.
7. One editable source of truth per subject.
8. Closed phases (git tags) are history, never current authority.
9. Conversation memory is not a source of truth. Write consequential state down: Worksheet before bootstrap, `docs/PROJECT_STATE.md` after.
10. Never silently change a locked decision. Surface it, get approval, record it.
11. Acceptance criteria must be observable. "Works well" is not a criterion when objective evidence is possible.
12. Every document must have one authority purpose. Nothing exists because a template lists it.
13. Stop planning when planning is sufficient. New ideas default to backlog.
14. Do not import domain rules, architecture, or assumptions from a previous project or from Foundry's examples.
15. For an existing project, read the repository before asking the owner anything it already answers.
16. A request that opens or continues planning authorizes planning only, even when it asks you to build the thing. Implementation begins on a new instruction.

## Depth levels and the compact path

Classify provisionally at F0; reassess when scope changes materially (accounts, payments, public use, precise location, autonomous AI actions, irreversible operations, regulated data). Details: `references/classification.md`.

| Level | Profile | Stages run | Documents |
|---|---|---|---|
| **L1 Small utility** | 1–few users, low-sensitivity data, small surface | **F0 → F1+F2 merged → F5-lite → F7 (one phase) → build → F11-lite.** Skip F3, F4, F6, F8, F9, F10. One irreversibility check inside F5-lite. Worksheet optional if single-session. | `README.md` with a five-line contract, acceptance criteria, and how to run. |
| **L2 Structured app** | Persistent data, several modules, modest users, maybe APIs/auth | All stages. F8 only if a high-risk subsystem exists or the owner asks. | `docs/`: Brief, State, plan, decisions, assumptions, backlog. Master Plan only if more than three phases. |
| **L3 Production product** | Public/org users, auth, customer data, uptime/support obligations | All stages, full F8, full F11. | L2 + Master Plan, risks, threat model, data lifecycle, runbook, release checklist. |
| **L4 High-consequence** | Money, health, safety, regulated, irreversible or autonomous actions | All stages; adversarial review at F8 and before F11. | L3 + safety boundaries, test oracles, failure-mode analysis, golden datasets, waivers distinct from passes. |

A project can be L2 with one L4 subsystem — a gardening app with an irrigation controller. Treat the subsystem at its own level; do not inflate the rest.

## The lifecycle

One gate per stage. Do not advance until it opens. The gate is the quality check.

| Stage | Goal | Gate opens when |
|---|---|---|
| **F0 Intake** | Restate the concept; separate facts, assumptions, unknowns; classify; pick the mode; create the repo and Worksheet. | You can ask meaningful product questions, and all supplied source material has been read (missing/unreadable disclosed). |
| **F0-R Reconcile** *(existing project — replaces F0)* | Read the repo first. Separate *implemented reality* / *documented intent* / *historical decisions* / *assumptions* / *drift and contradictions* / *missing definition areas*. Record what exists in the Worksheet. A project mid-implementation with documents elsewhere runs F0-R as a map-and-move in a workflow-only closeout phase (`references/document-package.md`, *Migrating an existing document set*). A project that predates Foundry keeps its own stage and slice names — record the mapping once instead of renaming — but M1 must be named. | You can state which stages are already satisfied and which need discovery or repair. Enter the lifecycle at the first unsatisfied stage; do not restart from zero for template conformity. |
| **F1 Interview** | Learn why it should exist and how it should behave. Propose-then-confirm batches; synthesis between batches. | Remaining unknowns no longer block a coherent contract and you can narrate the primary workflow end-to-end. |
| **F2 Product contract** | Vision, problem, users, jobs, core workflows, principles, non-goals, success criteria, real constraints, labeled assumptions. | Owner approves or explicitly delegates low-impact details. Not a technology idea with no user outcome. |
| **F3 Feature architecture** | Classify capabilities: Foundation / Core / Enhancement / Advanced / Experimental / Excluded, each with user problem, outcome, dependencies, data, risks, evidence of done. | Feature set supports a phased program with no scope ambiguity; nothing silently changes the target user or business model. |
| **F4 UX discovery** | Journeys, information architecture, primary screens and states, device priorities, design language, trust/AI UX, accessibility. | Implementation could build the right interaction model, not merely a working UI. Direction is more specific than "clean". |
| **F5 Architecture** | Simplest architecture that satisfies contract, consequence, and foreseeable scale; decision records for consequential choices. | Boundaries are deliberate and justified, and no new boundary would need inventing mid-implementation. |
| **F6 Risk review** | How can it harm users, lose data, leak, fail silently, or become unmanageable? | Every material risk has a control, explicit acceptance, scheduled research, or phase-scoped mitigation. |
| **F7 Program** | Phases with one observable outcome each, scope, non-goals, objective criteria, risk class, slices, evidence. **Phase 0 is always the walking skeleton**: the thinnest end-to-end slice through every major boundary, deployed, with CI and one real test. **Name M1**, the first usable milestone. Prefer *foundation → core workflow → expansion* over shallow breadth. | Phase 0, M1, and the phases between are sequenced so coding can begin without inventing architecture. Phase 0's criteria are objective. |
| **F8 Red team** | Fresh-context adversarial review of the whole plan; every finding gets ACCEPT / BACKLOG / REJECT / RESEARCH / ACCEPT-RISK. | The cross-document audit is clear of CRITICAL findings, and no unresolved finding invalidates contract, architecture, security model, or sequence. |
| **F9 Planning sufficient** | Declare `PLANNING SUFFICIENT`. | Everything above is settled, **and** further ideation is worth less than implementation feedback. |
| **F10 Bootstrap** | Generate `docs/` proportionate to level; decompose the Worksheet; write Phase 0's contract and first prompt. | Project State records current truth, Phase 0 contract exists, first prompt is ready, Worksheet archived to `docs/history/`. |
| *(implementation phases — `references/phase-workflow.md`)* | After M1 ships: the **M1 reality check** — use it for real; record what changed in Brief, feature classes, backlog, level. This is the one mandatory replan point. | |
| **F11 Release** | Verify the product is safe to put in front of real users, scaled to level — L1: it runs and destroys nothing; L3: restore, alerting, and rollback drills actually performed. | Every applicable item on the release checklist is `PASS` or an owner-approved `WAIVED`. |
| **Operate** | Changes, hotfixes, incidents, feedback, reclassification. Feedback flows into Brief and backlog through normal decision process. | Ongoing. See `references/release-and-operations.md`. |

**Stop-planning test.** Under-planned if: you cannot narrate the core workflow; key data has no source; an irreversible action has no control model; architecture rests on an unverified provider capability; Phase 0 has only subjective criteria; UX is only "clean". Over-planned if: designing Phase 8 before Phase 0 starts; debating tech for hypothetical scale; speccing speculative features; polishing coherent wording; inventing risks with no mechanism.

## How to run a session

**Stage banner.** Open every synthesis and stage transition with one line:

`[Foundry F1 · L2 provisional · Unified · Gate F1 open · 4 open · Worksheet v3]`

After bootstrap: `[Foundry Phase 2 · step 4 verify · L3 · Split · head a1b2c3d]`

**Session open.**
- *New project:* F0. Create the repo and `docs/WORKSHEET.md` from `templates/foundry-worksheet.md`.
- *Existing project:* F0-R. Read `README`, structure, tests, CI, recent commits, any docs — then ask.
- *Resume before bootstrap:* read `docs/WORKSHEET.md`. That is the entire required read. Continue from *Next exact action*.
- *Resume after bootstrap:* read `CLAUDE.md`, `docs/PROJECT_STATE.md`, and the current phase contract (`docs/plans/phase-NN.md`) — about 25 KB total. Master plans are read by section, by reference, never whole at session open. `PHASE_HISTORY.md` only when rationale is needed. Check `git log`, open PRs, last CI against the remote host, not a sandbox ref. Report drift. State phase, step, gate, next evidence.

**Interview (F1) — propose-then-confirm.** For each unknown, state your recommended answer as a labeled assumption with two to four alternatives, and ask the owner to correct only what is wrong. Reserve open-ended questions for the few things that reshape the product: the wedge, the primary user, non-goals, hard constraints. Never run a checklist. Research only when a current external fact materially changes the product.

**Delegation.** If the owner says "you decide" or "I trust you", switch to propose-only: make the choices, record each as `D-nn (delegated)`, and surface only those that change level, cost, users, or irreversibility. Delegated decisions are still locked decisions.

**Synthesis loop.** After each batch:

```
[banner]
What I understand now   — concise current product model
What this implies       — new design/feature/data/architecture implications
Decisions now resolved  — explicit, recorded (mark delegated ones)
Recommendations         — with rationale and feature class; not scope until accepted
Remaining questions     — next highest-value unknowns only
```

Then update the Worksheet. Contradictions: show both, explain why both cannot govern, present interpretations, let the owner decide if material. Never silently choose.

**Idea triage.** Any new idea, at any stage: *current-phase requirement* (only if omitting it makes active work incorrect, insecure, or incompatible with an approved requirement) / *next-phase candidate* / *product backlog* / *research backlog* / *rejected* / *duplicate*. Record it in `docs/backlog.md`; do not design it now.

**Session close.** Update the Worksheet (pre-bootstrap) or `docs/PROJECT_STATE.md` (post-bootstrap) with *Next exact action*. Commit.

## Authority order

1. Current explicit owner instruction.
2. Approved product contract and locked decisions (`docs/decisions.md`).
3. `docs/WORKSHEET.md` (pre-bootstrap) / `docs/PROJECT_STATE.md` (post-bootstrap).
4. Repository reality — code, migrations, tests, merged commits, exact CI evidence.
5. `docs/PHASE_HISTORY.md` for rationale.
6. Git tags and `docs/history/` for historical evidence.
7. Conversation memory, for orientation only.

Reconcile contradictions before consequential work; never resolve them silently. A project's own approved operating documents outrank this framework once they exist.

## Loading rules

Read a reference **once**, when its stage opens. Never load several "to be safe."

| When | Read |
|---|---|
| F0, if the level is unclear | `references/classification.md` |
| F1 opens | `references/discovery-interview.md` |
| F4 opens | `references/ux-discovery.md` |
| F5 opens | `references/architecture-decisions.md` |
| F6 and F8 open | `references/risk-and-red-team.md` |
| F7 opens; each implementation phase; any hotfix, change, or code-vs-intent reconciliation | `references/phase-workflow.md` |
| F10 opens; the cross-document audit before F8 and before F11 | `references/document-package.md` + needed `templates/` |
| F11 opens; post-launch operating sessions | `references/release-and-operations.md` |
| First time using Foundry | `references/example-garden-dry-run.md` |
| Writing a launch, resume, red-team, slice, or release prompt | `prompts.md` |

## After bootstrap

Each phase: contract → plan if needed → PR-sized slice in a draft PR → verify the exact post-review candidate → independent review by risk → experiential review where needed → merge, document, tag, close. The packet is evidence to inspect, not a conclusion to inherit. Behavior is written as a **spec delta** in the contract and merged into `docs/specs/locked-behavior.md` at close. Not every unit of work is a phase: a production defect takes the **hotfix path**, and behavior work too small for a phase takes the **change path** — why, delta, task list, same evidence rules, no planning step. `PROJECT_STATE.md` stays under 4 KB.
