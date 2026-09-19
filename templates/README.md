# Project templates

Scaffolds that `work-start` and `work-adopt` copy into a project, proportionate to its consequence. Fill only what applies; delete headings and rows that do not. Every file is a starting shape, not a checklist to satisfy.

| Template | Use it when | Owner of |
| --- | --- | --- |
| `project/README-contract.md` | A small, low-consequence utility that fits in one or two sessions | The whole contract |
| `project/CLAUDE.md` (copied byte-identical to `AGENTS.md`) | Any project with persistent data, several modules, or more than one session | Permanent constraints |
| `project/docs/OPERATING.md` | Same | Workflow pin, guidance mode, project bindings |
| `project/docs/PROJECT_STATE.md` | Same | Current work, authorization, next action |
| `project/docs/PHASE_HISTORY.md` | Same | Closed units, decisions, waivers |
| `project/.github/pull_request_template.md` | The project uses pull requests | The completion packet |
| `project/.github/scripts/select-ci.mjs` + test, `project/.github/workflows/ci.yml` | The project has CI | Change-based check selection |
| `project/.github/workflows/create-phase-tags.yml` | The assistant cannot push tags itself | Phase-close tagging |
| `project/docs/plans/register.md`, `cards.md`, `project/docs/evidence/packet.md` | The project delivers one card at a time | Status, scope, evidence, in that order |
| `project/docs/tools/TOOL-PROCEDURE.md` | An optional tool needs a written procedure | A procedure that grants no authority |

The product brief, decisions, assumptions, risks and backlog registries come from `library/foundry/templates/` when discovery produces them; those files are not duplicated here.
