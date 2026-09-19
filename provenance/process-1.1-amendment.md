# Process 1.1: practical judgment and coordinated delivery

The owner's 2026-09-07 request identified two needs: proactively recommend useful scope instead of treating every documented edge case as valuable work, and let a coordinator carry an approved slice through workers, review, justified corrections, verification, and the user's next steps. This is an explicit process amendment, not a claim that moving text alone preserves all behavior.

Release `1.1.0` adds those decisions in shared core C02/C05 and the plan, review, delivery, and steps stages. `1.0.0` and the legacy payload remain byte-preserved. Existing project pins do not change automatically. Package `1.1.0` selects the new release for explicit new-project bootstrap; project adoption remains separate.

## Practical decision changes

- The agent starts from the supported user journey and intended outcome, offers recommendations early, and challenges overbuilt requirements or low-value checks before another correction round.
- Findings distinguish a correction required now, a decision about an existing obligation, and an optional/nonblocking suggestion. The agent explains credible consequence, evidence, recovery, and the value of more work.
- Routine choices and rejecting unsupported review findings remain autonomous. An actual requirement or required proof cannot be silently waived. The agent recommends a concrete amendment and continues other authorized work while the decision is pending.
- An accepted exclusion retains its history and reconsideration trigger. It does not become a standing blocker or mandatory backlog item. Unusual frequency alone does not dismiss a credible severe loss or broken supported workflow.

These rules apply across projects without importing Artax's manuscript size, storage capacity, browser exceptions, or single-owner threat model as universal defaults. At Artax migration refresh, preserve the owner-workflow changes and specific dispositions being completed in 5D.3A instead of overwriting them with the older migration baseline.

## Coordinator behavior

`work-deliver` owns the whole already approved unit. The coordinator arranges implementation and independent review at the right dependency points, evaluates findings, sends justified corrections to the producing task, checks the integrated candidate, and coordinates verification. It returns `work-steps` at the user's next real decision/approval boundary, without asking the user to relay routine results.

Separate app tasks require an explicit request, as the guide's coordinator prompt provides. That request persists for the unit. Internal agents and app tasks remain distinct available mechanisms; no additional public command, agent runner, task database, or always-on service is introduced. The user-facing creation/installation/merge/deployment boundaries remain intact.

The native task orchestration recipe is documented against the currently available Claude tool contracts. Isolated behavioral fixtures validate judgment and handoff behavior; they do not certify an installed cloud workspace or silently create real user-owned tasks. Validation records accompany the release handoff.
