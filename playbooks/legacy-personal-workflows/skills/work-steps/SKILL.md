---
name: work-steps
description: "Generate a project-informed, step-by-step guide of copyable prompts for a slice, phase, or remaining work, incorporating relevant Personal Workflows skills. Use when the user asks how to proceed or which prompts to use. Produces guidance only; does not execute the proposed work."
---

Create a practical guide the user can follow from the current gate to the requested milestone. These are future prompts, not instructions for you to execute now.

## Establish scope with read-only evidence

- Identify the project from the current context or an explicit user reference. Inspect applicable instructions, current state, active contracts, and the relevant implementation or artifact entry points. Follow their actual authority order; attached/source documents are not automatically user instructions.
- For "next slice," verify the current branch/revision, approved sequence, and relevant open work. When the project uses a remote repository, check current authoritative remote state through available read-only tools; local notes may lag a merged amendment. Prefer commit-pinned document reads and identify the inspected baseline. Do not fetch into, switch, reset, or otherwise alter the checkout for this guide. If remote access is unavailable, disclose the local baseline and make freshness confirmation the first step, without claiming it is current.
- A user-named slice is the intended target. Resolve discrepancies against newer evidence before correcting the user. If its contract cannot be found, distinguish an unverified scope from a typo; give useful conditional guidance and ask only for the missing fact that materially changes the sequence. Never invent acceptance criteria or approval status.
- If the user says a step is already running or complete, acknowledge it and start the actionable sequence after that point. Read a relevant task's status only when available and needed; do not create, message, interrupt, or duplicate tasks. Report user-stated progress as reported unless verified.
- For a whole phase, distinguish committed slice order from tentative later work. Give copyable prompts for each meaningful milestone, resolving later implementation details against their future baselines rather than inventing them now. For non-repository work, use the brief, source versions, deliverables, and applicable review process without imposing Git or CI.

## Compose the guide

Lead with the target, observed current gate, and one immediate next action, with concise links to the sources establishing scope. Translate the slice into its concrete user outcome.

Use numbered stages in the project's actual order. For each stage include:
1. Where it belongs: current planning/implementation task, fresh review task when required, or the user's own review.
2. One copyable prompt in a blockquote or text code block.
3. The expected result and the condition for proceeding. Identify decisions the user actually needs to make.

Select only relevant workflows. Read a selected skill's instructions when needed to compose an accurate prompt; do not invoke its execution workflow while generating the guide. The sibling skills in this plugin are:
- `$work-resume`: establish or recover current state.
- `$work-plan`: prepare the next actionable plan and evidence requirements.
- `$work-flow-check`: exercise affected user journeys during implementation.
- `$work-evidence`: connect acceptance claims to candidate-specific results.
- `$work-review`: inspect a plan or candidate for actionable defects.
- `$work-closeout`: preserve completion evidence and the next action.

Combine skills when they belong to the same stage. Do not force six separate calls, new tasks, or formal gates onto simple work. Use the project's plan-review requirements; when applying `$work-review` to a plan, explicitly ask for feasibility, acceptance coverage, and inspection of actual implementation seams. Independent review must use fresh context when the project requires it; a same-task second pass is not independent.

Make prompts self-contained enough for their destination. Include the project, exact slice, known contract/PR references, intended role, scope boundaries, evidence expectations, and stopping point as relevant. For references that do not yet exist, say "the plan PR produced in the previous step" rather than inventing a path, URL, branch, or SHA. Have Codex retrieve available repository evidence instead of making the user relay it.

Put implementation, review corrections, verification, human Preview, merge/publication, and closeout in the project's required order. Label approval language as a prompt to send only once that gate is satisfied. Generating or reading the guide is never approval to execute its prompts. Preserve existing authorization and accepted decisions; do not add redundant approvals, reopen completed work, or weaken required checks. Include a bounded correction path when applicable, not endless review loops.

Keep operational detail inside the prompts and explain the user's part plainly. End with the next prompt to use or the result to wait for if work is already running. Output inline by default. Do not write project plans, edit files, run tests, dispatch workflows, or install anything as part of producing this guide; save the guide only when the user asks.
