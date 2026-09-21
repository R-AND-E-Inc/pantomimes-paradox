# Closeout · accepted work, durable state, next action

## X01 · Establish what actually completed

Compare the delivered candidate with accepted outcomes and project completion rules. Separate implementation, verification, acceptance, merge, deployment, release, and closure. Confirm the actual merged/delivered identity and required environment state when relevant. Do not infer approval from a completed implementation or a successful test. Keep unresolved evidence and residual risk visible.

## X02 · Reconcile existing owners

When routine project documentation is authorized, merge the accepted behavior delta into its existing specification owner, preserving stable IDs and complete surviving scenarios. Update only changed decisions, assumptions, risks, runbook, or invariants; link durable evidence rather than copy it. Keep current state focused on what exists, what does not, blockers, candidate/environment, and next exact action. History and version narrative belong in the historical owner. No universal document-size cap or mandatory document proliferation.

Append the meaningful milestone/change/hotfix/release record using the project's convention. Do not rewrite historical decisions or scatter duplicate status stores. For projectless work a final answer or companion handoff can be enough. An external export is labeled as such and points to its editable owner.

If a tag/archive is required and authorized, follow the project's actual mechanism, target convention, and permissions; `templates/project/.github/workflows/create-phase-tags.yml` is the reference mechanism for a repository whose agent cannot push tags. When establishing a new convention, prefer a closing tag on the commit containing its closing record and spec/state updates; the product merge may precede that commit. Preserve a different approved project target rule and flag any proposed change explicitly during migration. Verify the immutable target, never move an existing tag silently. Prefer integrating closeout updates in the accepted unit where practical; do not invent a new PR merely for ceremony. A workflow-only closeout exemption applies only if adopted, authorized, product code untouched, and applicable checks/first-execution limitations are accounted for; mechanically required CI cannot be waived by prose.

## X03 · M1 and supported improvement

At the first usable milestone, gather real-use feedback on the primary job before substantial expansion, respecting release/data boundaries. Reassess the brief, assumptions, feature priority, risks, and sequence only where evidence warrants. Do not require a fixed number of days or reopen accepted decisions without cause. The master plan can improve through the project's decision process.

For requested retrospectives or demonstrated repeated rework, propose a narrow prevention supported by the incident: better acceptance, a fixture, clearer source ownership, or a reusable method. Distinguish personal preference from verified technical learning. Never automatically promote a workaround into global policy or launch continuous memory/learning machinery.

Assess the process by accepted-result time, user coordination, meaningful correction cycles, missed requirements, false blockers, duplicated checks, and escaped defects, with comparable baselines where available. Model/tool usage and context payload are useful secondary measures. Do not invent speedup percentages or optimize for more agents, documents, tests, or fewer reported findings.

Give an outcome-centered handoff with meaningful verification, limits, and one next action if work remains. A process rollback restores the prior approved workflow profile/release; it does not reverse accepted product changes. Do not start the next unapproved slice as part of closing this one.

When revising reusable workflow guidance, inspect actual friction or failure before adding a rule or another skill. Use bounded transcript/artifact evidence, distinguishing the owner's instructions from delegated prompts; do not automatically mine or share unrelated sessions. Compare the relevant current behavior with the proposed change and retain limitations. Package integrity and model behavior are separate evidence classes. A rule that merely restates what already works need not become another mandatory step.
