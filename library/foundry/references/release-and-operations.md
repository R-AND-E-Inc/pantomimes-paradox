# Release (F11) and Operations

Read when F11 opens and at post-launch operating sessions. F11 is the gate between "it works in our environment" and "real users depend on it." Operations is everything after.

**When F11 runs.** Before the first real-user release, and again after any phase that touches persistence, routing, authentication, or asset loading. Production deployments of a product nobody depends on yet are not releases; "release-ready" is undefined until this gate has been run once. Tag `release-<version>` by the mechanism `OPERATING.md` records.

## F11 — Release gate

Run the checklist for the project's level. Every applicable item ends `PASS`, `WAIVED` (owner-approved, with residual risk recorded in `docs/risks.md`), or `N/A` with a one-line reason. Record the result in `docs/PHASE_HISTORY.md` as `RELEASE <version>` and tag `release-<version>` by the mechanism `OPERATING.md` records. Run the cross-document audit (`document-package.md`) first; a CRITICAL finding closes this gate too. For L4, an adversarial fresh-context review of the release candidate precedes the checklist.

### L1 — it runs and destroys nothing

- Runs from a clean checkout following the README.
- Any destructive operation has a dry-run or confirmation, and it was exercised.
- Inputs it will realistically see (empty, malformed, huge) do not corrupt anything.

### L2 — L1 plus

- Persistent data has a backup, and a restore from that backup was actually performed once. If user data lives only in the browser (IndexedDB, localStorage), this item is `N/A` → a recorded risk ("a user who clears storage loses everything") plus a backlog item for export/import.
- Errors are visible somewhere the owner will look (log file, console, error page); silent failure paths are known.
- Secrets are not in the repository; `.env.example` or equivalent documents what is needed.
- The deployed version is identifiable (version string, commit hash, or tag).
- Rollback is possible: the previous version can be redeployed, and the owner knows how.
- **Real-device check for browser-facing products.** Emulated engines (Playwright WebKit, device emulation) do not prove real-device fullscreen, orientation, audio unlock, touch, or media loading. A short checklist run on at least one real phone is a named gate item.

### L3 — L2 plus

- **Restore drill:** a full restore into a fresh environment from backup, timed, documented in `docs/runbook.md`.
- **Alerting drill:** at least one alert per critical failure mode (down, error-rate spike, job failure, disk/quota) was triggered deliberately and reached a human.
- **Rollback drill:** a rollback was rehearsed on the production path, not just described.
- **Real-device drill:** the L2 real-device checklist run on the two most common device/browser pairs for the audience.
- **Secrets:** rotated before launch; no credential used in development is live in production; least-privilege service accounts.
- **Auth and sessions:** session expiry, revocation, and account recovery tested; sensitive operations require reauthentication where the threat model says so.
- **Data lifecycle:** what is collected, why, retention, deletion path, and where it is processed — written down; deletion tested.
- **Legal basics for a public product:** privacy notice, terms, and required disclosures exist; cookie/consent handling where applicable; payment provider terms met if money is involved. Foundry cannot give legal advice — flag what needs a professional.
- **Load sanity:** the expected first-month traffic, times five, does not fall over. No formal load test needed at L3 unless the product is bursty.
- **Supply chain:** lockfile committed; dependency vulnerability scan clean or triaged; CI permissions minimal.
- **Observability:** logs are structured enough to trace one user's failed request; PII is redacted in logs.
- **Support path:** users can reach a human; the owner knows what "on call" means for this product.

### L4 — L3 plus

- Adversarial review of the release candidate by a fresh context, findings dispositioned.
- Mode/environment isolation proven: test and production cannot touch each other's data, credentials, or side-effecting providers.
- High-consequence calculations verified against golden datasets or hand-computed oracles on the exact release head.
- Irreversible actions: confirmation, audit trail, and an owner-verified path to detect and remediate a wrong action.
- Clean-machine recovery exercise completed: the system rebuilt from repository + backups by someone following the runbook.
- Every waiver signed off by the owner individually; a waiver on a safety control is not permitted.
- **A read-only CI token policy is a legitimate L4 choice.** Where it applies, the tag workflow cannot create tags: the owner or a local agent pushes `phase-NN-closed` and `release-<version>` instead, and `OPERATING.md` records that this is the project's mechanism rather than a workaround.

## Operate — the post-launch rhythm

**Incidents.** Detect → contain (rollback, feature flag, disable the path) → fix via the hotfix path (a defect) or the change path (a small capability the incident showed was missing) → write a short incident note in `docs/PHASE_HISTORY.md` (what, impact, cause, fix, what changes). If the cause is a class of problem, open a backlog or risk item; if it changes an invariant, update `CLAUDE.md`.

**Feedback.** User feedback, usage evidence, and support requests are triaged like any idea: current-phase requirement / **change** / next-phase candidate / backlog / research / rejected. After release, *change* is the common answer — small, contracted in its PR, evidenced, and logged. Material findings update the Brief through `docs/decisions.md`. Do not let feedback edit scope without a decision record.

**Reclassification.** Re-run the level check whenever the product gains accounts, payments, public exposure, sensitive data, autonomous actions, or irreversible operations. A level change re-opens F6 and F11 for the affected subsystem.

**Cadence.** For a maintained product, a short operating review at a sensible interval (monthly for L2, weekly for L3+): what broke, what users asked for, what is stale in the docs, what dependency needs updating, whether the runbook still works. Keep it in Phase History under `OPS REVIEW <date>`.

**Sunset.** If the product is retired: export or delete user data per the lifecycle spec, revoke credentials, archive the repository with a final tag, and record the sunset in Phase History.
