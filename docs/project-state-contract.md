# Optional project state integration, schema 1

Use this only when a project exposes status to a read-only consumer such as a personal dashboard. It is not a required file or service for every project. The adopted workflow release still lives in `docs/OPERATING.md`.

Keep one raw JSON block in the project's existing state document (normally `docs/PROJECT_STATE.md`):

```text
<!-- pantomimes-paradox-state:begin -->
{
  "schema": 1,
  "updated_at": "<actual UTC reconciliation time>",
  "active_work": {
    "id": "<stable current unit>",
    "title": "<current unit title>",
    "contract": {"path": "<repository-relative contract path>", "commit": "<full immutable commit>"},
    "pull_requests": [{"number": 1, "role": "implementation"}]
  },
  "gate": {"label": "<current gate>", "status": "active"},
  "next_action": "<exact current next action>",
  "authorization": "<project-declared authorization boundary>"
}
<!-- pantomimes-paradox-state:end -->
```

The angle-bracket values and example PR number are placeholders, not project state. Blocks written with the former `personal-workflows-state` markers are equivalent. Roles are `plan`, `implementation`, or `workflow`; multiple PRs may be associated. Gate status is `active`, `waiting`, or `blocked`. A contract can point to an approved unmerged plan by immutable commit. An open PR is never permission to implement or merge.

`updated_at` is a valid UTC ISO timestamp ending in `Z`, such as `2026-09-07T00:00:00Z`; fractional seconds are optional. Use the real reconciliation time, not a placeholder or a future forecast.

The block is the editable owner of these state fields. Surrounding prose explains decisions, history, exceptions and evidence without maintaining another current copy of the same fields. Reconcile from the accepted contract, current owner instruction, actual repository/PR state and running work. On closure, record the actual resulting gate and next action; do not infer authorization for the next unit.

Consumers fetch the state document at an observed immutable repository commit, distinguish project declarations from direct check observations and PR-reported claims, and retain field-level source/time/commit. Missing, malformed, stale or conflicting observations must be labelled. Historical phase maps may remain historical; refreshing commit metadata alone never establishes a current whole-project view. A consumer does not authorize or mutate source work.
