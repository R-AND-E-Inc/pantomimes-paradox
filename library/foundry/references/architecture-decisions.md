# Architecture and Technology Decisions — F5 playbook

Read once when F5 opens. Goal: prevent premature, fashionable, or inherited choices from becoming architecture.

## Constraints first

Before naming any technology, know: user/device context; online/offline needs; data volume and lifetime; sensitivity; collaboration/concurrency; required integrations; background/real-time behavior; reliability; scale; deployment constraints; budget; operator skill/capacity; legacy systems.

## Default biases (biases, not laws)

Monolith before microservices · one database before many · request/response before event streaming · managed capability before bespoke infra when lock-in, cost, and security stay acceptable · deterministic logic before AI for deterministic problems · background/async only when the product needs it · responsive web before native · caching only when performance evidence demands it.

## Decision record — for every consequential choice

Problem · hard requirements · nice-to-haves · credible candidates (no straw men) · evidence (current docs when capability, pricing, limits, or policy can change; with date) · decision · project-specific why · costs/tradeoffs · reconsideration triggers (scale exceeds X, provider drops Y, cost passes Z, offline requirement appears, team grows, sensitivity changes).

Record in the Decision Log or as a Tooling Decision Record (see `document-package.md`). Do not choose by fashion or familiarity alone.

## Domain notes

- **Frontend** — decide on interaction complexity, SSR/SEO, offline, device APIs, ecosystem, testability, deployment target.
- **Backend** — none if the product does not need one. Otherwise: domain logic, integrations, concurrency, data libraries, team skill, operations.
- **Database** — relationships, transactions, query patterns, scale, offline, durability. Not trend.
- **Auth** — first ask whether accounts are needed at all. Then identity, sessions, recovery, authorization, reauthentication for sensitive ops, threat model.
- **Hosting** — static frontend vs stateful app vs background jobs vs local-first vs always-on workers vs regulated data are different problems.
- **Real-time** — define it. Most "real-time" is "refresh within 30s" or "update on return".
- **AI** — classify the use (interpretation, generation, retrieval, vision, prediction, classification, agentic). Keep deterministic truth outside the model; prefer tool-backed AI that explains authoritative calculations over AI that recreates them.
- **External providers** — never hard-code vendor facts as timeless truth. Use adapters where replacement is plausible; capability discovery where provider state varies.

## Anti-pattern check before approval

Solving a hypothetical future problem? Component present only because "production apps have one"? Could one service/database/process do this safely? Two sources of truth emerging? Does AI add value or just uncertainty? Is a vendor defining the whole architecture? Is security delegated to network location alone? Is the recovery story credible? Does the test strategy match the architecture?

## Gate

Architecture is sufficient when the next phase can proceed without inventing a new system boundary mid-coding. Phase-local choices may stay open if they do not constrain current foundations.
