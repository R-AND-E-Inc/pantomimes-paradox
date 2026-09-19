# Process 2.0.0 — The Pantomime's Paradox

`2.0.0` is `1.2.0` (the last Personal Workflows release) carried into the new package. `1.0.0`, `1.1.0`, `1.2.0` and the legacy payload are preserved byte for byte with their original manifest digests, so any project pinned to them keeps its exact behavior. Migration is optional and is an ordinary adoption change.

## What changed, and why

| Location | Change | Reason |
| --- | --- | --- |
| `core.md` title and intro | New name; the sentence recording the lineage | Package rename |
| `core.md` C03 | "Foundry L1–L4 labels" → "consequence labels such as L1–L4 from the library's classification reference" | Foundry is now a library inside the package, not an external project |
| `core.md` C04 | Platform-neutral capability wording (Claude and Codex); a sentence on loading `library/` files once, when their stage opens | The package targets both assistants and now carries the references |
| `core.md` C05 | "Subagents, or internal delegation where subagents do not exist" | Codex has no subagent definitions |
| `core.md` C06 | Added: the five evidence classes; not-run is not a pass; reuse receipt requirements; changed-expectation rule; default correction limits (one round expected, two failed attempts → fresh context, three rounds → owner decision) | Rules proven on a real project over eleven phases, generalized as defaults a project may tighten |
| `core.md` C07 (new) | The handoff rule: every response ends with position and one next action, in the project's guidance mode (`Guidance mode: guided|expert` in the profile) | The owner's standing communication rules, made part of the method |
| `stages/start.md` | Names the library files to load at each discovery step; scaffolds from `templates/project/` proportionate to consequence; records the guidance mode | Library and templates now ship in the package |
| `stages/adopt.md` | Profile preparation starts from `templates/project/` and records the guidance mode | Same |
| `stages/plan.md` | Names `phase-workflow.md` for the delta grammar and contract skeleton; register/card/packet as an optional sequential-delivery binding | Same |
| `stages/deliver.md` | PR template as the default completion packet shape; C07 handoff at the decision boundary; names `release-and-operations.md` | Same |
| `stages/review.md` | Names the shipped reviewer agent and the Codex alternative; names the risk and document-package references | Same |
| `stages/steps.md` | Platform-neutral work-deliver prompt wording; ends with the C07 handoff | Same |
| `stages/closeout.md` | Names the phase-tag workflow template | Same |

No gate, authority order, stage routing, or acceptance requirement was removed.
