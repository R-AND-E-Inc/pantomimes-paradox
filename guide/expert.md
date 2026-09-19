# The one-page version

Install: `/plugin marketplace add R-AND-E-Inc/pantomimes-paradox` then `/plugin install pantomimes-paradox@pantomimes-paradox`. New session. Skills are namespaced: `/pantomimes-paradox:<skill>`.

**Model.** One shared process (`playbooks/<release>/core.md` + one stage file per skill), pinned per project by an adoption block in `docs/OPERATING.md` with the release, source commit and manifest SHA-256. A read-only resolver (`scripts/resolve_workflow.py`, stdlib Python) verifies hashes and returns the two files to load. Package updates append releases; they never mutate one or change a project's pin. No adoption block: the seven original skills run on the frozen legacy payload; `work-start`/`work-adopt` bootstrap with the package's current release; `work-deliver` refuses.

**Skills.** `work-start` discovery → contract → architecture → risk → program → bootstrap docs (planning only, always). `work-adopt` F0-R style reconciliation, obligation map, prepare and activate separately. `work-steps` guide-only prompts. `work-plan` contract with stable AC IDs and behavior delta. `work-resume` reconcile state vs repo vs remote, continue authorized work. `work-deliver` coordinator: implement → review → corrections → evidence → stop at approval boundary; hotfix/change/release/operate modes. `work-review` independent findings, red team, cross-document audit, code-vs-intent reconcile. `work-evidence` claim → candidate → oracle → class. `work-flow-check` one interaction end to end. `work-closeout` merge ≠ close; update owners, history, tag, next action. `paradox-setup` / `paradox-mode` orientation and verbosity.

**Defaults that matter.** Authority: current owner instruction → approved contract → locked specs → root rules and profile; history is evidence, never authority. One editable owner per fact. Evidence classes: structural / mocked unit / real dependency / browser / owner acceptance; not interchangeable. Not-run ≠ pass. Reuse needs original SHA, full intervening diff, invalidation reasoning. Corrections: one round expected; two failed attempts → fresh context; three rounds → owner decision. Independent review = fresh context, neutral brief, no seeded verdict (`agents/work-independent-reviewer.md`, no editing tools, changes nothing). Planning authorizes planning only. Optional suggestions never become blockers. Every reply ends with position + one next action (C07); `Guidance mode: guided|expert` in the profile.

**Library.** `library/foundry/` = discovery interview, classification (L1–L4), UX, architecture decisions, risk and red team, phase workflow (behavior deltas, change path, reconcile), document package and audit, release and operations, prompts, worked example. Stages name the file to load; load once.

**Templates.** `templates/project/`: root instructions with the information-ownership table, operating profile, project state (optional JSON block), phase history, PR completion packet, change-based CI selector + starter workflow, phase-tag workflow, register/card/packet trio, tool-procedure file.

**Codex.** Same tree carries `.codex-plugin/plugin.json` and per-skill `agents/openai.yaml`; commands are `$work-*`. Less tested; see `guide/codex.md`.

**Maintaining.** `docs/maintaining.md`. Never edit a released playbook; add a release, build its manifest, bump the plugin version, tag.
