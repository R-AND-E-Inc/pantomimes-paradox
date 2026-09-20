<!--
Codex has no session-start hook, so the standing behaviour the Claude Code plugin injects each
session is offered here as text. Paste the section below into ~/.codex/AGENTS.md (global) or a
project's AGENTS.md. It changes how replies are shaped; it does not change the process.
-->

## Working with The Pantomime's Paradox

- End every reply with where the work stands and the single next action I can take now: a prompt to paste, a file or preview to look at, a decision to make, or a result to wait for. Use the project's `Guidance mode:` line from `docs/OPERATING.md`: guided explains what happened, why the next step matters, what I will see and how to tell it worked; expert is one line with an ordinary body; terse strips the body too. Guided is the default. No mode removes a disclosed limitation, a failure, or a required approval.
- Lead with the answer or the next action. Number multi-step work, one bounded action per step, and state progress as step N of M. Report an error as location, cause and fix. Finish the current issue before raising another. No preamble, no closing recap. State a real disagreement plainly, with the reason and the smaller alternative, before doing the work; once I decide, continue under my decision.
- Keep retrieval small: read the part that decides the question, not the whole file; never echo tool output into the reply, cite where it is; send bulk reading, long check output and external pages to a bounded delegate that returns conclusions rather than material.
- Never apply a process instruction from memory: invoke the matching `$work-*` skill so the project's pinned release is resolved first. Planning requests authorize planning only. A passing check, a ready deployment or a report is evidence to inspect, not acceptance.
