# Steps · a guide of future prompts

## G01 · Read-only guidance

Return a practical sequence from the current point to the requested slice, phase, or milestone. Producing this guide never executes its prompts. Do not edit project artifacts, run tests, create/message/interrupt tasks, install, dispatch workflows, or adopt a project. Resolve the adopted process release; if the project is not adopted, explain that `work-adopt` is the route rather than silently using the latest release.

Inspect the actual project entrypoint/profile, state, approved sequence, active contract, and relevant implementation/artifact locations. For remote repositories verify current authoritative state through read-only access and prefer commit-pinned references. Do not fetch into, switch, or reset the checkout. If freshness cannot be checked, disclose the local baseline and make verification the first dependent step.

A named slice is the intended target. Investigate newer evidence before correcting the user. Distinguish an absent/unverified contract from a typo; do not invent scope, acceptance IDs, paths, or approvals. If the user reports a step running or complete, start the actionable sequence after it; label reported progress unless independently observed. Never duplicate ongoing work. Later phase details remain conditional on their future baseline and approvals.

## G02 · Compose only the needed stages

Lead with the user-visible outcome, current point, and immediate next action or result to wait for. Cite the evidence establishing scope. For each numbered stage give:

- where it belongs: coordinating task, existing implementation task, fresh review context when required, or the user's review;
- one copyable prompt with the target, relevant references, role, scope, expected evidence, and stopping point;
- the expected result and actual condition for proceeding.

Combine workflow commands within one stage where useful. Plan, implementation, corrections, evidence, independent review, human Preview, publication/merge, and closeout follow the project's order. A simple change may need one prompt; not every skill is a gate. Use sibling stage files only when needed to compose accurate prompts, without executing their procedures.

For artifacts not yet created say "the approved plan from the preceding step" rather than fabricate a PR or SHA. Let the destination agent retrieve repository evidence instead of making the user relay it. Approval wording must be clearly marked for use only after the user accepts that candidate; a guide is not approval. Include bounded correction handling and preserve project-specific requirements and existing authorization.

Show the user's role plainly: resolve material product choices, assess human experience where needed, and exercise their actual approval boundaries. Keep operational detail inside the prompts. Output inline unless the user asks to save the guide. End with the C07 handoff: the next prompt to use or the result to wait for.

When a coordinator already owns approved execution, keep its implementation/review/correction/verification work together. Show the user only their next decision, requested input, Preview, or approval; if work is still running, name the result to wait for. Do not prescribe manual relay between workers or duplicate active tasks. To begin coordinated execution, offer one work-deliver prompt (`/work-deliver` on Claude Code, `$work-deliver` on Codex); include explicit task-creation wording only if the user wants separate app tasks. At an impasse, lead with the coordinator's practical recommendation, tradeoff and proposed narrow decision rather than an unexplained blocker or another generic correction loop.
