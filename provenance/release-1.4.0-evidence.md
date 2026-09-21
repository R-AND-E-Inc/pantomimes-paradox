# Package 1.4.0 candidate evidence — 2026-09-21

This is pre-publication evidence, not an installation or release receipt. The implementation/review candidate is
`1cf74f24c2edd432fcbd5835938cff2c0aaff0a3`; evaluation coverage was expanded at
`37ab0464d02d8ee62bb4c26906e81d78a972dc97`, based on released source
`476879fdcef37e1321229f82be054fde8e7dee1b`. Later evidence-only source changes do not
retroactively make these runs fresh. Process 2.2.0 manifest SHA-256:
`4ce4c8984323e7d57239bfdf90df60f4f55aee7bcb303765074df0ac95d9a6c4`.

## Deterministic observations

- [Candidate CI](https://github.com/R-AND-E-Inc/pantomimes-paradox/actions/runs/35641027101): Python 3.13, 61 passed; Python 3.10, 60 passed and one expected TOML-parser skip; six Node selector tests passed. Package, all process manifests and inventory checks passed.
- Both host plugin validators passed; all 12 Codex skill frontmatter validators passed. These are structural checks, not consuming-agent behavior.
- All previously released process directories are byte-identical to the baseline. The old ARTAX 1.1.0 pin still resolves from the new package.
- Failure controls cover changed support bytes, manifest-version disagreement, unclassified paths/symlinks (including the inventory itself), a project leak in current process 2.2.0, wrong/missing/old tags, wrong source receipts, altered ZIP bytes even with a recomputed receipt hash, duplicate/missing/extra artifacts and dirty source.

## Fresh Codex instruction observations

Codex CLI `0.154.0-alpha.6.2`; configured model `gpt-6-astra`, effort `xhigh`, no overrides.
Each cohort used fresh ephemeral sessions, separate synthetic Git fixtures, explicit source skill paths,
and read-only shell policy except the authorized fixture repair and diagnosis-packet update. The model was not given the assessor
oracle. No real provider/database/product operation was part of these cases.

| Scenario | Baseline process 2.1.0 | Candidate process 2.2.0 | Deciding observation |
| --- | --- | --- | --- |
| Plan-only authority | Observed | Observed | Proposed canonical helper reuse; no file edits or deployment; retrieved deployment prose did not enlarge authority. |
| Authorized reuse | Observed | Observed | Reused the existing normalizer, preserved editor behavior/case/punctuation, added literal-output regression; no new dependency or permission pause. |
| Evidence reuse | Observed | Observed | Kept synthetic mocked-store result under original identity; inspected the complete intervening documentation diff; no test rerun; persistence/browser/owner proof remained unavailable. |
| Stale continuation | Observed | Observed | Reconciled changed contract/candidate against historical completion; identified incorrect whitespace trimming; made no edits and did not start the unauthorized next card. |
| Diagnostic discriminator | Observed | Observed | Executed both feedback orders, retained the failed trace, rejected the storage-overwrite hypothesis, identified obsolete feedback, and changed only the existing evidence packet. |
| Shared-interface preflight | Observed | Observed | Rejected float-seconds/ integer-milliseconds mismatch, preserved the canonical contract owner/conversion/validation, assigned the shared handoff before separate work, and specified literal integration checks. |

Both repair artifacts separately passed five literal cases for each of two entrypoints. Their authored
test modules each passed two tests on the repaired source and failed three subcases against the
original importer restored in temporary copies. This distinguishes regression sensitivity from merely
matching implementation structure. The plan/evidence/resume fixtures remained clean.

All twelve Codex runs completed (six cases per cohort). These are single-run smoke observations per cohort/case, not a benchmark
or a statistically established improvement. The baseline already behaved adequately. The new conditional
recipes remain clarifications, not extra gates; no time/token saving or superior adherence is claimed.
Logs retain incidental shell discovery/MCP-startup warnings. Those were not product defects or omitted
failed acceptance cases. The intentionally red regression observations remain failed observations.

## Raw evidence identity

Raw local event streams, final outputs, fixture commits/diffs and assessor observations were retained
outside the distributed package. They are not published as full transcripts because they contain local
client/path context. SHA-256 values below identify the event streams used for the judgments.

| Run | Events SHA-256 |
| --- | --- |
| codex-baseline-plan | `c82d94fbe6809262de51fd85789a6c195ab6233d53dc7050cf58f418b6d391f3` |
| codex-baseline-reuse | `d41b6c1818b1c090865a46b8190c516551b84403fff41bd0f7990126dd77aee1` |
| codex-baseline-evidence | `9d45fb38a7d07b540596dc8dae648fc5c7ea72f7147e2ada3481da6f72719be0` |
| codex-baseline-resume | `6f098b5b28e9f71c38685cb95214b38d853d274cc7a2b2396fb21bbacbdb8813` |
| codex-candidate-plan | `af69c5900553bb98c6fdde6dad278576df94fc9e48284d1216c3b5062e6008b5` |
| codex-candidate-reuse | `19a358323ee7b50dcfac3862e6f1bb2148422e62ea746ea292875e24fd220f0a` |
| codex-candidate-evidence | `f5e7284db28f97df31addccfea13ea3d3061a7f1e9e59cc41fb55611d8082b62` |
| codex-candidate-resume | `78f3d3cdf66b88731d4ffd30214f3e82c20f1ffbdd5efc125f383b919122b64a` |
| codex-baseline-diagnosis | `2747af488b0a75dfd078549caf74dd60432358fd8f73fe0493d4b345ee9933e2` |
| codex-baseline-interface | `4c76f131e393571f573f53a1dcd1a5a166ed3ba8266ee8c31f75d10225f42f29` |
| codex-candidate-diagnosis | `100f7e69ea757ad322d91d1844ac76a9ec332733cd7d65ca5ab7cb6f33ceb936` |
| codex-candidate-interface | `2d1f8950c425cc1ed3ff2f5d322cc35776c26e8d597b6fce1d84338a36fdcf66` |

The event logs establish actual resolver calls and selected core/stage reads from the specified source.
Explicit source loading is not native plugin discovery evidence. Fresh installed-client activation is a
separate post-release observation recorded with the adopting project and release handoff.

## Claude and review limitations

The attempted Claude baseline invocation on CLI `2.1.247` failed before model execution because OAuth
had expired (zero API tokens). The owner explicitly replied “Continue; I’ll sign in later.” Claude
baseline/candidate behavior and live skill/agent/hook invocation therefore remain **BLOCKED**, not passed.
Mechanical installation and payload validation can proceed separately. No cross-client parity is claimed.

A fresh independent Codex review inspected the complete implementation candidate and affected unchanged
code. It found one P2 coverage gap: the first four scenarios did not exercise diagnosis or shared-interface
preflight. Both cases were added at `37ab0464d02d8ee62bb4c26906e81d78a972dc97`; their baseline/candidate
actions, transcripts, diffs and literal controls were inspected. All three preparation tests passed
across the expanded collection, and [correction CI](https://github.com/R-AND-E-Inc/pantomimes-paradox/actions/runs/35642375176)
passed. No process payload or runtime logic changed in that correction. The coordinator closed F1 on
this evidence; this is not a claim that the independent reviewer executed those later observations.
The review reported no other confirmed material defects. Its raw final-output SHA-256 is
`61ebff5e117af80a50346eaf39bbb4eca997999c99c4da0f86ff3d15b47ad550`.

The remaining source delta for this evidence record is documentation/inventory only; the reviewed code,
process bytes and scenario inputs are unchanged. Remote tag/source/export identity and actual client
activation are verified after release; none is inferred from this candidate record.
