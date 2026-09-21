# <Card id> — <outcome>

**Gate:** `<AC id>` is <implemented | independently reviewed | corrected | verified at <environments>>, and is **<awaiting the owner checkpoint | accepted on <date>>**. Application source `<commit>`; test or browser coverage `<commit>`; review corrections `<commit>`; based on `<commit>`. No <CI run | preview | deployment> is claimed beyond what is listed below.

**Task identity:** <accepted plan revision; full task base/head range and relevant dirty changes; use existing pointers>. A path or the latest single commit alone does not identify the complete task.

**Activation, when changed:** <source provenance; payload hash; installed/enabled client; observed skill path, selected release and invocation; limitations>. Reuse a valid prior receipt instead of repeating it.

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

## Diagnosis, when a failure remains

<Exact observation/candidate/environment; requirement; event order; rejected hypotheses; next discriminating observation; actual result. Omit if no unresolved diagnosis.>

## Disclosed observations and limitations

- <pre-existing issues found, recorded as discoveries rather than folded in>
- <what could not be verified and who carries the residual risk>

## Owner checkpoint

<The one thing the owner does by hand, and the questions the packet asks them.>
