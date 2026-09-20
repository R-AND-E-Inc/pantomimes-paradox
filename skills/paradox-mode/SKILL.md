---
name: paradox-mode
description: "Show or switch The Pantomime's Paradox guidance mode for this project: guided explains every step, expert gives one-line handoffs, terse strips the body too. Use for 'switch to expert', 'explain more', 'less detail', 'what mode am I in'."
allowed-tools: Read, Glob, Grep, Edit
---

The guidance mode changes how much is explained; it never changes the process, its gates, or the evidence required. It never removes a disclosed limitation, an unverified claim, a failure, or a required approval.

1. Look for a line beginning `Guidance mode:` in `docs/OPERATING.md` at the project root. Report the current mode, or that none is recorded (guided is then the default).
2. If the user asked for a change and the file exists, edit only that line, or add it directly above the adoption block when absent. This one-line edit is the whole authorized change; touch nothing else in the profile. If no `docs/OPERATING.md` exists, apply the mode for this session and say that it will be recorded when the project documents are created.
3. Name the three modes in one line each. **Guided** says what happened, why the next step matters, what the user will see, and how to tell it worked. **Expert** keeps an ordinary body and gives the position and next action in one line. **Terse** strips the body as well, to findings, decisions and what the user must act on, with evidence named rather than described. Recommend guided to anyone new to running a software project with an assistant, and terse only to someone who wants to read as little as possible.
4. End with the current mode and the single next action the user was already on, in the newly selected mode.
