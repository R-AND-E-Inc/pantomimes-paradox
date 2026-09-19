# Complexity and Consequence Classification

Read at F0 only if the level is not obvious from the core's level table. The classification is a planning tool, not a prestige level: it scales documentation, review, testing, security, and operational rigor to **consequence, complexity, uncertainty, and irreversibility**.

## Dimensions

Judge across all of these rather than one score:

- **Scale** — one user or many; private/internal/public; anonymous or authenticated; one role or several; collaboration/concurrency.
- **Data sensitivity** — none → preferences → precise location → customer confidential → credentials → financial → health → legally protected.
- **Action consequence** — display → save editable content → send messages → charge money → move money → delete irreplaceable data → control hardware/infrastructure → automate consequential decisions.
- **Irreversibility** — a styling bug is reversible; a corrupted ledger, sent payment, deleted record, or unsafe automation may not be.
- **Technical complexity** — modules, statefulness, real-time, background jobs, integrations, distribution, concurrency, migrations, offline/sync, media, AI/ML, domain rules.
- **External dependency** — third-party APIs, paid data, vendor approval, app stores, regulation, third-party identity/payments, unstable data.
- **Reliability** — can it be down for a day, a minute, never during business hours?
- **AI consequence** — cosmetic → convenience → analytical → recommendation-producing → autonomous/action-taking → safety-critical domain.
- **Legal/regulatory surface** — money, health, children, privacy regimes, employment, contracts, regulated professions.
- **Longevity** — weekend prototype vs multi-year system. Long-lived means stronger source-of-truth, migration, dependency, and recovery discipline.

## Levels

| | L1 Small utility | L2 Structured app | L3 Production product | L4 High-consequence |
|---|---|---|---|---|
| Examples | converter, static tool, hobby tracker | garden planner, media library, internal workflow tool | subscription SaaS, team platform, public consumer app | financial execution, clinical decision support, destructive infra automation |
| Docs | compact brief; short architecture decision; light plan | full brief; concise Master Plan; decision log; assumptions | complete package; threat model; data lifecycle; DR | L3 + safety boundaries, test oracles, failure-mode analysis, golden datasets |
| Continuity | Worksheet optional if single-session | `docs/` in the repo | `docs/` + runbook | `docs/` + runbook + drills |
| Review | none | independent review for high-risk phases | strong CI; independent review for high-risk changes | adversarial independent review; clean-machine recovery exercises; explicit waivers |

## Mixed profiles

A project can be L2 overall with an L4 subsystem (a gardening app with an optional irrigation controller). Treat the subsystem at its own level; do not inflate unrelated features.

## Reclassify when

Accounts/auth added; payments added; personal → public; precise location stored; autonomous AI actions introduced; irreversible operations added; regulated data added. **Not** merely because the codebase grew.

## Phase risk (separate from project level)

- **Low** — documentation, copy, isolated styling, simple deterministic changes.
- **Medium** — new bounded workflows, responsive behavior, ordinary integrations, user-state features.
- **High** — security, migrations, persistence semantics, money, destructive actions, background execution, permissions, difficult concurrency, major boundaries.

Project level sets baseline rigor; phase risk sets review intensity.
