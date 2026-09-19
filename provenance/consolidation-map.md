# Consolidation map · process 1.1.0

This is an implementation audit artifact, not routine agent context. The runtime loads `core.md` and the selected stage, not this map or the source ledger. The build preserves useful Foundry capabilities while replacing duplicated commands and inherited harness assumptions. Existing project adoption and substantive policy changes remain separate from this build.

The owner-requested [process 1.1 amendment](process-1.1-amendment.md) adds practical judgment before correction loops and coordinator-owned execution through the user’s next steps. Earlier process payloads remain intact.

## Sources and evidence

- Project Foundry v3.2 supplied bundle: `skills/project-foundry/` core, references, prompts, registries and document templates, plus the 16 `foundry-*` mode skills.
- Installed Personal Workflows `0.1.0+codex.20260906054402`: all seven current skill bodies.
- `source-obligations.json` records raw source file hashes; 663 non-heading source segments across 37 Markdown files; complete segment text, source line locations, segment hashes, treatment/rationale, and destination rule IDs. The destination registry contains the full text/hash of each referenced rule section.

The segment ledger accounts for source material rather than pretending that one mapped heading proves semantic preservation. Some source paragraphs/code examples contain related obligations. The curated changes below explain consequential adaptations; independent behavioral review is still needed to establish how the integrated system performs. Syntax validation and matching hashes alone do not establish semantic equivalence or productivity gain.

Historical changelog narrative and the gardening example are excluded as current process authority. The executable GitHub tag template is not copied: tagging remains an existing project capability and permission choice. Its behavioral requirements (immutable identity, no silent retargeting, appropriate closeout target, truthful verification) are represented in X02.

## Public capability consolidation

| Existing Foundry mode | Consolidated entrypoint and rule |
|---|---|
| `foundry-new` | `work-start`: S01–S04 |
| `foundry-adopt` | `work-adopt`: A01–A04 |
| `foundry-bootstrap` | `work-start`: S04 |
| `foundry-continue` | `work-resume`: N01–N02 |
| `foundry-phase` | `work-plan`: P02/P04; `work-deliver`: D01 |
| `foundry-slice` | `work-plan`: P04; `work-deliver`: D01 |
| `foundry-change` | `work-plan`: P01; `work-deliver`: D03 |
| `foundry-hotfix` | `work-deliver`: D03 |
| `foundry-review` | `work-review`: R01/R02/R04 |
| `foundry-redteam` | `work-review`: R01/R02/R04 |
| `foundry-audit` | `work-review`: R03/R04 |
| `foundry-reconcile` | `work-review`: R03 |
| `foundry-m1` | `work-closeout`: X03 |
| `foundry-close` | `work-closeout`: X01/X02 |
| `foundry-release` | `work-deliver`: D04 |
| `foundry-operate` | `work-deliver`: D05 |

The seven Personal Workflows names retain their functional roles. Their detailed instructions now live in `stages/steps.md`, `plan.md`, `resume.md`, `review.md`, `evidence.md`, `flow-check.md`, and `closeout.md`. Start, adoption, and delivery fill lifecycle gaps; they do not require a separate command per Foundry stage.

## Consequential obligation treatment

| Obligation/source | Destination | Treatment and reason |
|---|---|---|
| Understand product before choosing stack; do not assume AI/cloud/auth/native/scale | S01/S02, P03 | Preserved as decision criteria across project types. |
| Facts, assumptions, preferences, constraints, recommendations, delegated decisions remain distinct | C02, S01 | Preserved; delegation does not silently change consequence, cost, audience, or irreversible actions. |
| Planning request always requires a new implementation instruction, even when it asks to build | C02, P04 | Adapted. Plan-only remains plan-only; explicit implementation authorization persists. Project-specific approval gates still apply. |
| Existing approved project operating documents outrank framework | C01 | Preserved and made release-aware. Factual observation does not override normative intent. |
| Repository is mandatory from F0; Drive cannot update files | C04, S04 | Adapted/retired. Use the actual chosen working store and verified capabilities; nonsoftware/chat-only work does not automatically need Git. |
| One editable owner per subject; histories are historical | C01, S04, X02 | Preserved; project facts never enter the global plugin. |
| Foundry L1–L4 and per-phase risk | C03, P03 | Adapted into independent work size and consequence. Preserve adopted labels and subsystem-specific rigor; no automatic global tier inflation. |
| Fixed banners, startup payload targets, question/non-goal counts and 4 KB state cap | C04, G02, N02 | Universal quotas retired. Preserve any explicit project requirement, completeness, measured inputs, and narrow retrieval. |
| Read stage reference once | C04 | Preserved with invalidation when relevant candidate/process/authority changes. |
| Choose modes by vendor, start a fresh session every major phase | C04/C05, R01 | Adapted to actual available capabilities. Preserve meaningful fresh review; avoid automatic background sessions and needless context resets. |
| Propose-then-confirm discovery and narrated user jobs | S01 | Preserved without inventing assumptions merely to avoid unresolved-question counts. |
| Product/capability hierarchy, meaningful non-goals, sufficient discovery | S02/S03 | Preserved, with optional capabilities remaining proposals. |
| UX journeys, empty/error/stale/recovery, accessibility, provenance and uncertainty | S02, P03, F01 | Preserved and applied to actual interfaces/devices. |
| Architecture alternatives, dated provider facts, costs, reconsideration triggers | S02, P03 | Preserved; installed specialty tools supply domain details. |
| Concrete risk mechanisms, controls, residuals, owners and resolution timing | S02, P03 | Preserved. Deferred research cannot clear a risk blocking current work. |
| Phase 0 always starts every program | S03 | Adapted. Prove untested critical boundaries; reuse already proven foundations and use a representative source-to-artifact path outside software. |
| First usable milestone and reality check | S03, X03 | Preserved without a fixed waiting period; reassess from real use before substantial expansion. |
| Planning sufficient; further speculative ideation goes to backlog | S03, P04 | Preserved. |
| Bootstrap document suite and Worksheet decomposition | S04, A02, X02 | Preserve decisions/content and canonical owners; retire mandatory files, hard-coded section numbers and template copying independent of need. |
| Stable criteria and bidirectional requirement/control/slice coverage | P02, R03 | Preserved where traceability matters. Counts need explicit source denominators; no cosmetic completion percentage. |
| Behavior delta with stable IDs and complete modified scenarios | P02, X02 | Preserved in project-owned specification conventions; no rewriting away surviving scenarios. |
| Mechanical contract self-check against measured input and required outputs | P02 | Preserved. |
| Coherent draft-PR slice and verified remote base | D01 | Preserved for projects whose workflow uses Git/PRs; artifact work uses its appropriate version identity. |
| No opportunistic refactors, scope absorption, silent narrowing, or corrupting output to pass a check | C02, D01 | Preserved; record named deviations and resolve affected authority. |
| Exact-candidate packet, immutable deployment, rendered evidence | C06, E01/E02, F01 | Preserved; different evidence types prove different claims. |
| One complete post-review run, changed-head invalidation | C06, D02, E02 | Project strictness preserved. Reuse unaffected evidence only where its adopted policy permits it. |
| Fail-closed scripts, positive controls, raw-data counts | E03 | Preserved; never certify a report using that report's own summary. |
| Inspect packet, scope review by risk, distinguish waivers and passes | C06, E02/E03, R01 | Preserved; project full inspection/correction requirements remain authoritative. |
| Missing/partial/contradicting/unrequested reconciliation | R03 | Preserved; surface unrequested behavior without silently deleting it. Agreement does not prove quality. |
| Independent review, severity discipline, dispositions, related corrections | R01/R04 | Preserved. Neutral bounded briefs and exact candidates; no mandated positive verdict or invented findings. |
| Two failed attempts/three correction rounds | D02, R04 | Preserve explicit project limits. Generic default uses evidence of ineffective work rather than unrequested universal counters. |
| Human Preview after rendered verification; no manual rerun of automation | D02, F01 | Preserved where applicable. |
| Merged is not closed; state/spec/decision/history updates | X01/X02 | Preserved with existing owners and only changed documents. |
| Tag closeout revision, dispatch/local mechanism, immutable tag | X02 | Adopted convention governs. Recommend closing-record identity for new conventions; changing an existing product-merge target is an explicit migration decision. |
| Workflow-only reduced CI closeout and real branch protection | X02, E02 | Preserve only when adopted and authorized; a prose exemption cannot bypass a mechanically required check. |
| Hotfix and small-change paths | P01, D03 | Preserved. High-consequence fixes still get applicable review; no automatic phase/tag for every change. |
| Two adjacent changes necessarily become a phase | C03, P01 | Adapted to a scope reassessment signal rather than universal mechanical ceremony. |
| Release differs from deployment; drills actually performed | D04 | Preserved with consequence/project-specific checks. |
| Real-device proof differs from browser emulation | D04, F01 | Preserved for requirements that need it; no universal invented device matrix. |
| Retention, backup, rollback, deletion, secrets, supply chain, support, load and isolation | D04 | Preserved as applicable release concerns; existing nonwaivable policy controls remain intact. No generic fixed load multiplier or legal-policy invention. |
| Incidents, feedback, reclassification, maintenance cadence and sunset | D05, X03 | Preserved; cadence and external actions require actual user/project authorization. |
| Migration heading map/one distinctive sentence proves zero loss | A02, E03 | Strengthened to complete-content comparison plus obligation-level semantic review; distinguish movement from deliberate policy change. |
| Migrate only between whole product phases | A03 | Adapted to an explicit closed-slice boundary when safe; never alter in-flight commitments silently. |
| Retain prior snapshots and retire old editable location after transition | A02/A03 | Preserved; old tags cannot recover uncommitted historical documents. |
| Automatic cross-document semantic findings must be deterministic | R03 | Claim retired; deterministic mechanical outputs and source-grounded semantic review are different. |
| Automatic ongoing memory/learning/orchestration infrastructure | C04/C05, X03 | Not introduced. Use native capabilities and narrow retrospective changes only when needed and authorized. |
| Personal guide-only steps, candidate-aware resume, truthful evidence, review-only edits | G01/G02, N01/N02, E01–E03, R01 | Preserved with release resolution and actual project requirements. |
| Meaningful speed measurement | X03 | Preserved. Outcome time, coordination, corrections and escaped defects matter; no measured improvement is claimed by packaging checks. |

## Project and environment integration boundary

Profiles own approved release adoption, source locations, exceptions, commands/checks, approval rules, deployment, and target conventions. The playbooks own methods. Existing CI/tests/hooks enforce project behavior; existing provider/browser/document skills perform specialist work. A dashboard may display projected state, not authorize implementation. App tasks, internal subagents, and repository worktrees are different mechanisms with different ownership.

The initial preparation preserved the in-flight Artax 5D.3A slice. Project activation follows its accepted transition and owner authorization. A prepared migration alone is not activation. Missing or incompatible process resolution must be reported; bootstrap preparation is explicit and cannot silently adopt the project. Rollback restores prior process/profile behavior while preserving product commits and history.
