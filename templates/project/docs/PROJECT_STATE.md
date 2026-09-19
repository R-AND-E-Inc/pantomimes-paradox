# <Project> — Project State

**This file owns current work, authorization, holds and the next action, and nothing else.** Permanent constraints live in the root instructions; workflow policy in `docs/OPERATING.md`; contracts in `docs/plans/`; evidence in `docs/evidence/` and pull request bodies; history in `docs/PHASE_HISTORY.md`. Keep this file small: status only, no rationale, no locked behavior.

<!--
The block below is optional. Keep it only if a tool reads it (see docs/project-state-contract.md in
the package). Otherwise delete the block and keep the prose sections. Delete this comment.
-->

<!-- pantomimes-paradox-state:begin -->
{
  "schema": 1,
  "updated_at": "2026-01-01T00:00:00Z",
  "active_work": {
    "id": "<stable id of the current unit>",
    "title": "<current unit title>",
    "contract": {"path": "docs/plans/<contract>.md", "commit": "<full commit>"},
    "pull_requests": []
  },
  "gate": {"label": "<current gate>", "status": "active"},
  "next_action": "<exact next action>",
  "authorization": "<what is authorized right now, and what is not>"
}
<!-- pantomimes-paradox-state:end -->

## Exists now

## Does not exist yet

## Blockers and known issues

## Deploy, runtime and migration state

## Holds and waivers

<!-- Explicit owner exclusions, each with its reason and the trigger that reopens it. -->

## Next exact action

<!-- One line. The next session starts here. -->
