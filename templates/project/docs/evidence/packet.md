# <Card id> — <outcome>

**Gate:** `<AC id>` is <implemented | independently reviewed | corrected | verified at <environments>>, and is **<awaiting the owner checkpoint | accepted on <date>>**. Application source `<commit>`; test or browser coverage `<commit>`; review corrections `<commit>`; based on `<commit>`. No <CI run | preview | deployment> is claimed beyond what is listed below.

## Result and deciding evidence

<Two or three sentences: the defect or outcome in the product's own terms, and what now holds.>

| Acceptance / finding | Deciding oracle and result |
| --- | --- |
| `<AC id>` | **PASS <class>, <environment>.** <what was observed> |

**Evidence class:** <state plainly which claims are structural, mocked, real-dependency, browser, or owner acceptance>.

## Independent review and its disposition

| Finding | Disposition |
| --- | --- |
| **F-A <severity>** — <finding> | **CONFIRMED AND CORRECTED / REJECTED WITH EVIDENCE / ACCEPTED AS STATED / DEFERRED (trigger)** — <why> |

## Verification

- Focused checks: <counts, from raw output, and the files they came from>.
- Positive controls: <what fails when the change is reverted>.
- Required CI: <run and head, or "not run" with the reason>.

## Disclosed observations and limitations

- <pre-existing issues found, recorded as discoveries rather than folded in>
- <what could not be verified and who carries the residual risk>

## Owner checkpoint

<The one thing the owner does by hand, and the questions the packet asks them.>
