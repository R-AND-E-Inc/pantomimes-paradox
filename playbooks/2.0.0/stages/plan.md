# Plan · outcome, contract, and smallest coherent work

## P01 · Ground the plan

Inspect current instructions, state, existing accepted plan, and actual files. Preserve approved decisions and current authorization. For software trace the affected entrypoint, behavior, interfaces, data, and visible result; for authored artifacts trace sources, transformation, audience, and delivery format. Cite inspected locations; filenames alone do not prove behavior. Separate assumptions from facts. Resolve answerable unknowns before asking about material preferences or decisions.

Choose the smallest unit under C03 and the project's policy. A trivial edit can proceed directly. A bounded change can use an outcome, reason, behavior delta, ordered tasks with checks, and relevant risk in one existing artifact. A hotfix uses the observed released defect and proof of correction. New boundaries, conflicting approved decisions, materially changed consequence, or dependent multi-slice work need a coherent contract or phase. Do not use small-change labeling to hide changed scope.

## P02 · Contract and behavior delta

State one observable outcome, exact scope, exclusions that actually bound it, dependencies, consequential risks, the checkpoint the user can perform, affected ownership, review/evidence requirements, and remaining decisions. Each acceptance criterion names an observable scenario and adequate oracle, tracing to the requirement, control, or user request it serves. Every slice names the criteria it covers; check coverage in both directions where a program has multiple artifacts. Preserve existing identifiers; do not introduce an ID bureaucracy for a one-off edit.

Before adding criteria or a test matrix, judge what each protects in the actual use case. Recommend removing proposed low-value combinations and simplifying overbuilt approaches. Challenge an existing obligation with a concrete alternative and tradeoff when warranted; use its amendment path rather than turning the document into an unquestionable goal. Keep credible severe failures covered without inventing unsupported audiences or operating conditions.

Describe behavior added, modified, removed, or renamed, or explicitly state there is no behavior change with a reason; `library/foundry/references/phase-workflow.md` carries the delta grammar and the contract skeleton, loaded once when a contract is written. Stable requirement IDs survive rewrites and renames and are never reused. A modified requirement carries its complete surviving scenarios; omitted scenarios are not implicitly removed. At close, merge the accepted delta into its existing behavioral owner rather than rewriting the whole specification. For a small or nonsoftware project use its existing content/source-change convention.

Check mechanical acceptance criteria against measured inputs and the contract's own required outputs. Do not invent thresholds for unmeasured files or require absence of a string the scope mandates. A coverage percentage needs an explicit denominator and inspected sources; do not fabricate certainty from a heading count. Breakage, compatibility, data migration, and rollback/forward repair belong in the plan when they affect the outcome.

## P03 · Architecture, experience, and risk only as needed

For unresolved architecture use current constraints, credible alternatives, dated provider facts, cost/operations, and reconsideration triggers. Prefer existing boundaries and authoritative schemas/types where adequate. Multiple independent consumers may justify a shared contract; an atomic single-module change may not. Keep deterministic truth out of probabilistic generation where correctness requires it. Avoid speculative scale and duplicating installed platform capabilities.

For visible work define concrete interaction and visual expectations, relevant devices, loading/empty/error/stale/recovery states, keyboard/accessibility, and provenance. Include rendered review where appearance matters. A screenshot may prove appearance but not saved state; a build proves neither. Use `flow-check` for the affected journey.

For each material risk identify mechanism, impact, control, detection, owner/resolution point, and residual risk without invented numerical precision. Reassess affected subsystem classification for new users, sensitive data, autonomy, irreversible operations, authentication, or boundaries. High-consequence seams receive the project's required fresh review and meaningful oracle even in a small diff.

## P04 · Sequence and stop

Order independently reviewable slices toward the first useful checkpoint, proving untested boundaries early. Each slice states what action demonstrates its result. A project that delivers one card at a time may keep a register, cards and per-card evidence packets from `templates/project/docs/plans/` and `templates/project/docs/evidence/`; the register alone owns status, cards own scope, packets own evidence. Plan the active unit from repository reality; reference the program instead of replanning it. Preserve contract amendment conventions and distinguish changed intent from a narrow amendment. If the existing contract can honestly close without a new idea, that idea is generally separate work.

Return a compact but complete plan in the project's established location or in chat when no persistence is needed. Use `review` for required feasibility/coverage and independent risk review; avoid a generic new approval loop. When scope explicitly authorizes implementation, continue after material uncertainties and applicable gates are resolved. For plan-only requests, stop with the plan. Further ideation is unnecessary when the outcome, boundaries, checks, and next action are coherent.
