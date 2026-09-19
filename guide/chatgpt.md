# Using it in ChatGPT or claude.ai chat (no Codex, no Claude Code)

A plain chat cannot run the package's resolver, read your repository on its own, or execute tests. It can still follow the process, and it is told to say plainly what it could not verify. Use this path for planning, reviewing documents, and getting the next prompts; use Codex or Claude Code for building.

## Get the exports

Every release on GitHub carries one zip per skill named `<skill>-chat-<release>.zip` (for example `work-plan-chat-2.0.0.zip`): https://github.com/R-AND-E-Inc/pantomimes-paradox/releases

Each zip holds a loader `SKILL.md`, the exact process files that skill needs, and `identity.json` recording the release and its manifest hash.

## Add a skill

- **ChatGPT:** open the skills or plugins area of your ChatGPT settings, upload the zip for the skill you want (`work-start` for a new idea, `work-steps` for "what next", `work-review` for a review), and start a new conversation. Invoke it by name when the conversation starts.
- **claude.ai:** Customize → Skills, upload the same zip, start a new conversation.

The exact menu names change; the zip is the same for both.

## What to expect

- The assistant reads `identity.json` and the process files, then works from what you paste or attach. Give it the project's `docs/OPERATING.md` and `docs/PROJECT_STATE.md` when you have them.
- Anything it cannot do in chat (run tests, open a pull request, dispatch a reviewer) is named as a gap in its reply rather than claimed. Copy its prompts into Codex or Claude Code for the parts that need a machine.
- Every reply still ends with where the work stands and your next action.

## Building the exports yourself

```sh
python3 scripts/build_exports.py --output /path/outside/the/checkout
```

The output is deterministic for a given commit; `exports-receipt.json` lists each file's hash.
