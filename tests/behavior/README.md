# Consuming-agent behavior observations

These cases exercise an assistant using the process, separately from the Python tests of resolver,
export and release behavior. Normal CI validates fixture preparation; it does **not** invoke a model,
spend API credits, publish a report or claim model adherence.

## Prepare a neutral case

Use `scripts/prepare_behavior.py --plugin-root /exact/package --output /new/fixture --scenario <id>
--release <exact-release> --source-commit <observed-full-SHA> --receipt /outside/receipt.json
--prompt /outside/prompt.txt`. The helper never launches an agent. The selected package may be an
immutable baseline checkout or a candidate; record dirty candidate identity separately if present.

The receipt contains the deciding oracle and is for the assessor. Give the consuming agent only the
prompt and fixture, not the oracle, prior results, desired answer or proposed fix. It must resolve
and load the specified skill/payload. The supplied evidence records are synthetic scenario inputs,
not test results from a live product. Test fixtures are isolated Git repositories and must never
use project/provider credentials or live data.

The six cases cover planning-only authority and retrieved instructions; authorized implementation,
reuse and regression sensitivity; evidence calibration and reuse; stale plan/candidate continuation;
a diagnostic discriminator; and a shared-interface handoff with incompatible producer/consumer assumptions.
The fifth family, real client activation, is observed after installation using the receipt described
in `docs/activation.md`. Explicitly loading source text is not native plugin discovery proof.

## Observe and assess

1. Run a fresh baseline context on the relevant case before a claimed behavioral improvement. Use
   the user's configured model/effort and record the actual effective values from the client.
2. Run the candidate under the same case/settings in a separate fixture. Capture actual tool events,
   final output, artifact diff, exit/error state and relevant test output. Restrict the run to the
   fixture and authorized read-only package access. Do not assume a shell sandbox also restricts MCP.
3. Inspect the artifact oracle and the agent's actual decisions. A grader's word match or the agent's
   own "PASS" is not the verdict. For the fix case, run the real behavior against literal expected
   values and check that the added regression can detect the original defective implementation.
4. Record observed / contradicted / not exercised / blocked for each claim with its source identity.
   Inspect ambiguous outcomes manually and repeat variable cases where needed to distinguish a
   pattern. A single sample is a smoke observation, not a statistically demonstrated improvement.
5. Keep only useful changes. If baseline and candidate already behave adequately, report no measured
   improvement and avoid promoting a clarification to another mandatory gate. Preserve failures and
   unavailable hosts; do not quietly drop them from the denominator.

Record missed requirements, unrequested work, unnecessary pauses/repeated checks, completion of the
actual task, elapsed time and usage when available. No line-count, speed, token or run-count target is
an acceptance criterion. Select cases by the changed instructions; a spelling correction does not
require this campaign. No independent model judge, external service or reporting platform is required.

Current observed CLI forms belong in `docs/activation.md`; revalidate help on the installed version.
For any evaluation tool that publishes reports by default, explicitly disable publication unless the
owner requested it. Model evaluation is not permission to install an upstream framework or alter the
client's normal model/configuration.
