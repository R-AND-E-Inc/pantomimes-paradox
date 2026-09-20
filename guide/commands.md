# Commands

On Claude Code every command is `/pantomimes-paradox:<name>`; on Codex it is `$<name>`. Plain language reaches the same skills; the commands are the reliable spelling. Every command ends with a handoff: where the work stands and the one next action. Bulk reading, external lookups and long check runs are delegated to bounded helpers (`work-explorer`, `work-researcher`, `work-verifier`) so their material never fills the session.

**paradox-setup** — First run. Confirms the package is intact, asks guided, expert or terse, asks new idea or existing code, and gives the next prompt. Creates nothing.

**paradox-mode** — Shows or switches the guidance mode for this project: `guided` explains each step, `expert` keeps an ordinary reply with a one-line handoff, `terse` strips the reply to findings and what you must act on. No mode hides a limitation, a failure or something needing your approval. Changes only that line in the project's profile.

**work-start** — A new project. Restates the idea, separates facts from assumptions, interviews you in small batches with proposed answers, forms the product contract, chooses the simplest architecture, reviews risk, sequences the first slices, and creates the project documents when you say so. It plans; it does not build until you give a new instruction.

**work-adopt** — An existing codebase. Reads the code, tests, CI and notes before asking anything; separates what exists from what was intended; maps every existing rule to where it will live; prepares the migration on a branch; activates only when you authorize it. Existing names and decisions are preserved.

**work-steps** — The prompts to paste next for a slice or phase, in order, each with where it belongs, what to expect and when to proceed. Guidance only; it never runs them.

**work-plan** — One change, planned against the real files: outcome, scope, behavior delta with stable IDs, acceptance criteria with observable oracles, risks, and the checkpoint you will be able to perform. Plan-only unless you also authorized implementation.

**work-resume** — Where the project actually is: reconciles the state file with the repository and the remote, separates done from in-progress from waiting-on-you, and continues the already-authorized action without re-asking.

**work-deliver** — Carries an approved unit through implementation, the required independent review, justified corrections, verification and the evidence packet, then stops at your next real decision or approval. It never merges, deploys or publishes on its own. Also the path for hotfixes, small changes, releases and operations.

**work-review** — Findings about an exact candidate: defects, regressions, missing proof, with severity and a recommended disposition. Independent when the project requires it (a fresh context that did not author the work). Also red teams a plan and audits documents against each other.

**work-evidence** — Whether the results prove the acceptance criteria for this exact candidate: which check, what class of evidence, in which environment, and what is still unproven.

**work-flow-check** — One user interaction traced and exercised from the first click through persistence to the final visible result, including the boundary case the change implicates.

**work-closeout** — After acceptance: what actually completed, records updated in their single owners, the behavior delta merged into locked behavior, history appended, tag created if the project uses them, and the next exact action written down.
