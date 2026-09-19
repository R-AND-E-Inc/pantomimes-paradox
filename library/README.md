# Library

Reference material the process stages load on demand. Nothing here is a command or an authority of its own; the pinned playbook says which file to read and when, and each file is read once when its stage opens.

`foundry/` is Project Foundry v3.2, the discovery-to-operations method this package absorbed:

| File | Loaded by |
| --- | --- |
| `method.md` | Background reading; the stages carry what applies |
| `references/discovery-interview.md` | `start`, when discovery opens |
| `references/classification.md` | `start`, when the consequence level is unclear |
| `references/ux-discovery.md` | `start`, when interaction design opens |
| `references/architecture-decisions.md` | `start`, when architecture opens |
| `references/risk-and-red-team.md` | `start` for risk; `review` for a red team |
| `references/phase-workflow.md` | `plan`, when a contract or behavior delta is written |
| `references/document-package.md` | `review`, for the cross-document audit |
| `references/release-and-operations.md` | `deliver`, when a release is requested |
| `references/example-garden-dry-run.md` | First use, to see a whole run |
| `templates/` | Worksheet, intake form, registries and the document skeletons discovery produces |
| `prompts.md`, `CHANGELOG.md` | Reference |

Foundry's sixteen entry-point commands are not shipped; `provenance/consolidation-map.md` records where each one went.
