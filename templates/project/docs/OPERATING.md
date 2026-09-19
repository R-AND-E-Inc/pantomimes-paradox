# <Project> — Workflow Profile

<!--
This is the project's ONLY workflow profile. It pins the process release and records the project's own
bindings. work-start / work-adopt fill the adoption block below from the installed package's
playbooks/manifest.json (see docs/resolver-contract.md in the package); the resolver rejects the
placeholder values, so the profile is not effective until they are replaced. Delete this comment.
-->

Guidance mode: guided

<!-- pantomimes-paradox:begin -->
{
  "schema": 1,
  "plugin": "pantomimes-paradox",
  "release": "RELEASE",
  "source": "https://github.com/R-AND-E-Inc/pantomimes-paradox",
  "source_commit": "FULL_LOWERCASE_GIT_COMMIT",
  "manifest_sha256": "LOWERCASE_SHA256_OF_THE_RELEASE_MANIFEST"
}
<!-- pantomimes-paradox:end -->

After adoption, use the pinned `playbooks/<release>/core.md` and only the stage the task needs. The bindings below override the process defaults where they are stricter or more specific; they never loosen an evidence rule. A package update cannot change this pin or an in-flight unit's contract.

## Authority and roles

The owner decides product scope, resolves tradeoffs, judges the experience where human judgment matters, and gives every approval this profile requires. The assistant inspects the repository, prepares coherent changes, runs the applicable checks, gathers evidence, handles corrections and updates the handoff. Independent review uses a fresh context that did not author the candidate.

## Commands

<!-- The exact commands that establish implementation reality here. Delete rows that do not apply. -->

| Purpose | Command |
| --- | --- |
| Install | |
| Run locally | |
| Targeted tests | |
| Full suite | |
| Lint and typecheck | |
| Build | |

## Risk tiers and review

<!-- Classify each unit by realistic failure consequence, not by size. -->

- **Low:** documentation, copy, isolated styling, deterministic test maintenance, narrow fixes without state or lifecycle impact. Short contract; no independent review; targeted checks and required CI.
- **Medium:** new user interactions, routing, bounded components, responsive behavior. A concise repository-informed plan; independent review when the diff, the uncertainty or the affected system warrants it; targeted checks and required CI; owner preview when the change is visible.
- **High (list this codebase's high-risk areas):** persistence, migrations, state machines, security boundaries, async lifecycle, anything that can destroy user data. Plan plus one fresh-context independent review; regression evidence and required CI.

Correction limits: one correction round per affected system is expected; two failed attempts on one defect require a fresh implementation context; three meaningful correction rounds in one unit stop for the owner's split, defer or replan decision.

## Branches, pull requests and merge

- One approved branch and one draft pull request per unit. No direct edits to the default branch.
- The pull request body is the completion packet, in the shape of `.github/pull_request_template.md`.
- Merge requires the owner's explicit approval. Deployment and publication require their own authorization.
- Required status check: <name> · branch protection: yes/no · who authorizes merges: <owner>

## Verification and evidence

Name the evidence class of every consequential claim (structural, mocked unit, real database or dependency, browser or rendered observation, owner acceptance). Keep PASS, FAIL, BLOCKED, WAIVED and NOT APPLICABLE distinct. Reuse passing evidence for unchanged systems only with the original candidate identity, the complete intervening diff and the reason it still holds. Run the complete required suite at most once for a final candidate, after corrections settle; repeat only the failed or affected scope afterwards.

<!-- Project-specific rules: which browsers or devices matter, what "rendered evidence" means here, which environment is authoritative (CI, a preview deployment, a local run). -->

## Closeout and phase tags

After the owner authorizes a merge: merge, verify the merge commit, update `docs/PROJECT_STATE.md` (current truth only), append `docs/PHASE_HISTORY.md`, update locked behavior when it changed, and write the next exact action. Tagging mechanism: <`.github/workflows/create-phase-tags.yml` dispatched by the owner | local push by the owner | none>. The tag goes on the commit carrying the closing record.

## Environment and tools

<!-- Where verification is authoritative; what the owner does and does not do locally; tool additions deferred by default. -->

Add no new framework, orchestration platform, model API or tool to this project without a separate owner decision. A tool file under `docs/tools/` describes an optional procedure and grants no authority of its own.
