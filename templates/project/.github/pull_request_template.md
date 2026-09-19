# Summary

<!-- One coherent outcome. Implementation detail goes below. -->

## Scope

- Risk: <!-- low | medium | high -->
- Contract: <!-- `docs/plans/<plan>.md` section, or a concise reference -->
- Material systems changed:
- Non-goals preserved:

## Acceptance evidence

Exact proposed merge head: `FULL_SHA`

<!--
Use the stable acceptance IDs assigned before implementation.
Status values: PASS, FAIL, BLOCKED, WAIVED, NOT APPLICABLE. Keep them distinct; a skipped, failed,
cancelled or never-selected required case is not a PASS.
Class names what the evidence can establish: structural (shape only), mocked unit (the unit's decisions
only), real database or dependency (names its effective target and migration state), browser or rendered
observation (names engine and device profile), owner acceptance (the owner's own report, never inferred
from a passing check or a ready deployment).
Mode is NEW (executed at the full SHA named) or REUSED (original SHA and run named, receipt below).
-->

| AC ID | Status | Oracle | Class | Environment | Mode | Evidence and executed full SHA | Manual owner | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## Verification

### Targeted checks

| Check | Result | Class | Mode | Evidence and executed full SHA |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Required CI

- Run: <!-- exact run URL -->
- Head: `FULL_SHA`
- Event or dispatched mode: <!-- a focused mode is not a complete suite -->
- Jobs: <!-- one line per required job: passed / skipped / flaky / failed, with independently calculated counts -->
- Intentional skips: <!-- count, delta and explanation -->

### Verification integrity

- Custom verification scripts cited: <!-- path, self-calculated measurement, success-only marker, exit code; or none -->
- Absence checks and positive controls: <!-- or why no practical control exists and the claim's limit -->
- Independent count calculation: <!-- from raw output, not this packet's own summary -->
- Required cases that did not execute: <!-- skipped, filtered, cancelled or unselected; reason; who carries the residual risk; or none -->
- Changed test expectations: <!-- previous assertion, why it was wrong against the accepted requirement, what the replacement still detects; or none -->

### Reuse validity

<!-- One receipt per reused result. Delete only if nothing is reused. Reuse never converts an earlier FAIL, cancellation or skip into a PASS. -->

- Reused IDs, original full source SHA and run:
- Current candidate full SHA:
- Complete intervening diff reviewed: <!-- compare range covering the whole interval -->
- Why each reused result is not invalidated:
- Targeted new results covering the changes:

## Review and preview

- Independent review: <!-- result, not required, or pending, with rationale -->
- Owner preview: <!-- approved, waived, not required, or pending -->
- Manual or real-device checks: <!-- owner and status -->

## Known compromises and unverified claims

- Known compromises:
- Not verified:
- Product decisions proposed but not implemented:
- Lifecycle states, stated separately: <!-- implementation / verification / owner acceptance / merge / deployment -->

## Final checklist

- [ ] The diff contains only approved scope.
- [ ] Every acceptance criterion has a stable ID and a direct evidence row.
- [ ] Every PASS is valid for the exact proposed merge head, by new execution or by reuse with a complete receipt.
- [ ] Failures, cancellations, skips and waivers remain visible and are not recorded as passes.
- [ ] Waivers name the approver, scope, reason and residual risk.
- [ ] The PR is not merged without the owner's explicit approval.
