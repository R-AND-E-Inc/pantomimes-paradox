# Process 2.1.0 — delegation, retrieval hygiene, terse mode

`2.1.0` is `2.0.0` plus three additions the owner asked for on 2026-09-19. `2.0.0` and every earlier release stay byte-identical with their original manifest digests, so a project pinned to one keeps its exact behaviour. Migration is optional and is an ordinary adoption change.

## What prompted it

A measurement, taken on a real session of this package's own development: 549,199 tokens of a 1,000,000 window in use, of which the conversation was 481,629 and everything the plugin itself contributes was about 14,300. What fills a working context is tool results, not prose. That ranking decided which of four proposals were worth building and which was not.

## What changed

| Location | Change |
| --- | --- |
| `core.md` C04 | New paragraph on retrieval hygiene: read the deciding part rather than the whole file, never re-read what is in context, prefer targeted search, never echo tool output into the response, route bulk material to a delegate. Names retrieval as the scarce resource and the reply as the cheap one. |
| `core.md` C04 | New paragraph on model routing: route by what the work decides, never by how much of it there is; retrieval and mechanical reporting may run smaller, anything judging correctness or acceptance does not; a switch resets the cached context, so prefer setting the model on a bounded delegate over the user's session. |
| `core.md` C05 | New paragraphs: a three-part test for delegating decided before the work starts, an explicit do-not-delegate list, the statement that delegation buys isolation rather than speed or economy, and the four-role roster with each role's return contract and the fallback where subagents do not exist. |
| `core.md` C07 | Guidance modes become guided, expert and terse; terse strips the body as well as the handoff. No mode may remove a disclosed limitation, an unverified claim, a failure or a required approval. New rule: state a real disagreement plainly with the reason and the smaller alternative, and stop raising it once the user decides. |
| `stages/start.md` | Bounded reading and dated external questions go to the delegates during discovery. |
| `stages/deliver.md` | The coordinator decides its delegation before the work starts. |
| `stages/evidence.md` | A long-output check may go to `work-verifier`. |
| `stages/review.md` | Wording only; the reviewer agent is no longer described as Claude-only. |

No gate, authority order, stage routing, evidence rule or acceptance requirement was removed or weakened.

## What ships alongside it, outside the release

These are package files rather than process payload, so they are not hashed by the release manifest:

- `agents/work-explorer.md`, `agents/work-researcher.md`, `agents/work-verifier.md`: the three new bounded roles, each with a write denylist and `model: sonnet`. `work-independent-reviewer` deliberately keeps no `model` field so it inherits the session's, because it judges correctness.
- `templates/project/docs/OPERATING.md`: a delegation and model routing section with a default routing table and a never-routed-down row.
- `skills/paradox-mode`, `skills/paradox-setup`, `hooks/session-context.md`, and the guides: the third mode.

## Deliberately not done

- **Auto-compaction at a fixed threshold.** Claude Code already auto-compacts, and its trigger is a personal setting (`autoCompactEnabled`, `autoCompactWindow`) that a plugin cannot set. More importantly the process already answers a full context better than compaction does: state lives in the repository and major units start fresh, which is lossless where a summary is not.
- **Hard-coded `model:` in the shipped skills' frontmatter.** The field exists and works, but switching model resets the cached context on every invocation, and for a short skill that costs more than the tier saves. The option is documented in the project template instead, so an owner can make that trade with their own measurements.
- **Runtime generation of agent definitions.** An installed plugin is a read-only cache, and a generated agent carries no review or provenance. The roster is fixed and a project defines its own extras in its own repository.
