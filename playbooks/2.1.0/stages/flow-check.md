# Flow check · entry to final observed result

## F01 · Trace the user's path

Define the starting state, action, expected outcome, actual environment, and candidate from accepted requirements. Trace the reachable control/entrypoint through handling, validation, state/API transition, persistence where applicable, and final visible result. Include later operations that can overwrite or undo success. Inspect only relevant paths; a handler's existence does not prove reachability.

Exercise the path using the available browser/artifact tool and appropriate safe fixtures. Check the meaningful boundary case implicated by the change: retry/late response, cancellation, unchanged input, navigation, inaccessible control, permission, empty/error/stale state, or recovery. For persistence reload/revisit; for changed access exercise specified roles; for appearance inspect required rendered sizes and states. Follow project-mandated environments and human/device obligations rather than a universal browser matrix.

## F02 · Effects and evidence

Keep external effects within authorization. If the real path sends a message, purchases, deletes, publishes, or changes live data without authorization, use a suitable test environment or stop that step and identify the gap. Static trace, simulation, local preview, and live end-to-end execution are distinct evidence types.

Record starting state, action, expected and observed outcome, candidate/environment, and focused evidence. Identify the first demonstrated failure, fix when authorized, and recheck the affected path. If execution tooling is unavailable, return a useful static trace and concrete unexecuted check with its limitation. Do not call build success or a visible initial button a complete interaction pass. This complements domain/visual review rather than replacing it.
