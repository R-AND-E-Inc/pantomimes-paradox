# Evidence · accepted outcome to delivered candidate

## E01 · Identify claims and candidate

Extract the accepted criteria and project's verification rules without inventing requirements. Identify the actual candidate: revision plus relevant dirty changes, or exact artifact version/path and modification state. For deployments identify the immutable deployment and represented revision; a moving alias is insufficient where exact-head proof is required. Inspect existing evidence first, distinguishing direct observations, reported results, and inference.

Map each criterion to the smallest adequate check and inspect the underlying output. Logic tests, rendered appearance, persistence, end-to-end behavior, and real-device behavior prove different claims. Prefer existing specialty tools. A screenshot of an initial screen, DOM presence, a successful build, or a report saying "all passed" is insufficient for unrelated behavior.

## E02 · Verify and invalidate precisely

Run missing checks within authorization and the available environment; a long-output check can go to `work-verifier`, which returns the command, its exact counts and every failure without carrying the output back. Use the project's local/CI split; do not duplicate a complete suite already authoritative for this candidate. Apply the project's full final-revision and correction-matrix requirements when stricter. Where policy permits, preserve unaffected evidence with a specific reason and rerun or invalidate affected evidence after changes. Never certify a new revision with older-head results merely because they are green.

Inspect exact diff, review threads, CI and raw outputs at the depth warranted by project policy, high consequence, suspicious failures, experiential claims, or packet discrepancies. Contradicted evidence is unresolved at every risk class. Investigate failures rather than changing retries/skips/timeouts to manufacture success.

## E03 · Oracles and reporting

A verification helper computes its claim from primary data, fails nonzero on violated assertions, and emits success only after all checks pass. Rejection/absence tests need a positive control proving the detector/path operates. Counts come from raw observations, not the summary being certified. For document migrations compare complete verbatim segments and inspect semantic changes; a surviving heading or distinctive line cannot prove no content was lost.

Record each material criterion with candidate, check, actual status, inspectable evidence, and limitation. Passed requires observed support; failed, not run, blocked, waived, and not applicable remain distinct. Waivers name the proper approver, scope, reason, residual risk, and candidate where relevant. A first-execution gap is untested until run or an explicit exception is accepted; it is not a pass. Do not declare completion while required evidence is unresolved.

Use a concise table only when it improves comparison. Keep sensitive data out of logs and packets; link focused outputs. Store one canonical packet where the project expects it rather than copying it into every status document. Save no extra packet for a trivial edit unless useful. Evidence collection does not itself authorize merge, publication, destructive action, or release.
