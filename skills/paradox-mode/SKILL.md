---
name: paradox-mode
description: Show or switch The Pantomime's Paradox guidance mode for this project — guided (explains every step) or expert (one-line handoffs). Use for "switch to expert", "explain more", "less detail", "what mode am I in".
argument-hint: "[guided|expert]"
allowed-tools: Read, Glob, Grep, Edit
---

The guidance mode changes how much each handoff explains; it never changes the process, its gates, or the evidence required.

1. Look for a line beginning `Guidance mode:` in `docs/OPERATING.md` at the project root. Report the current mode, or that none is recorded (guided is then the default).
2. If the user asked for a change and the file exists, edit only that line, or add it directly above the adoption block when absent. This one-line edit is the whole authorized change; touch nothing else in the profile. If no `docs/OPERATING.md` exists, apply the mode for this session and say that it will be recorded when the project documents are created.
3. Describe the difference in two sentences: guided says what happened, why the next step matters, what the user will see, and how to tell it worked; expert gives the position and the next action in one line.
4. End with the current mode and the single next action the user was already on, in the newly selected mode.
