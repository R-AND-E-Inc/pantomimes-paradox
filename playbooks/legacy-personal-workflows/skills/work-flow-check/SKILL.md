---
name: work-flow-check
description: "Use when implementing or debugging a multi-step user interaction, a dead control, state that does not persist, navigation, or an end-to-end workflow. Can also check interactive documents or forms. Not a substitute for a visual design skill or a generic code review."
---

Trace a representative interaction from entry point to observable result.

1. Define the user's starting state, action, and expected result from the request and project requirements. Identify the actual environment under test. Prefer existing fixtures, test accounts, and safe local previews when available.
2. Inspect the complete path: visible control or entry point, event/command handling, validation, state or API transition, persistence if relevant, and the rendered response. Map only the path relevant to this task. A handler existing in code does not prove the user can reach it.
3. Exercise that path with the appropriate browser or artifact tool when available. Check the meaningful boundary or failure case implicated by the change, not every hypothetical permutation. If persistence is required, revisit or reload; if access is changed, exercise the specified roles; if visual behavior is changed, inspect rendered output at relevant sizes. Use project-mandated environments.
4. Keep external effects within the user's authorization. If the real path sends a message, purchases, deletes, or publishes and that action is not authorized, use a test environment or stop that step and report the remaining gap. Never represent simulation or static inspection as a live end-to-end pass.
5. Record starting state, action, expected and observed result, candidate/environment, and concise evidence. If the path fails, identify the first demonstrated break and fix it when authorized. Recheck the affected path after the fix.

If execution tooling is unavailable, provide an honest static trace and a concrete unexecuted check, with the limitation explicit. Avoid declaring success from build output, a visible button, or a screenshot of only the initial state.
