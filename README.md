# The Pantomime's Paradox

A workflow for building software with an AI coding assistant, packaged as a plugin. It makes the assistant understand the product before picking a technology, plan in small verifiable slices, prove what it claims with real evidence, get a fresh pair of eyes on risky changes, and end every reply with the one thing you should do next.

It is shared for friends. It is not a product and asks you to sign up for nothing.

## Install (Claude Code)

Inside Claude Code, run these two commands, then start a new session:

```
/plugin marketplace add R-AND-E-Inc/pantomimes-paradox
/plugin install pantomimes-paradox@pantomimes-paradox
```

Then, in the folder of a project (new or existing):

```
/pantomimes-paradox:paradox-setup
```

That checks the install, asks whether you want **guided** (explains each step), **expert** (one-line handoffs) or **terse** (findings only), and hands you the exact next prompt. From there you can just talk normally; the assistant picks the right skill. Commands are shortcuts, not homework.

To try it for one session without installing: `claude --plugin-dir /path/to/pantomimes-paradox`.

Requirements: Claude Code, and `python3` on the machine (macOS and Linux have it; on Windows install Python 3 from python.org or the Microsoft Store). Without Python the skills still work, but they cannot verify the process files' hashes and will say so.

## Install (Codex)

```sh
codex plugin marketplace add R-AND-E-Inc/pantomimes-paradox
codex plugin add pantomimes-paradox@pantomimes-paradox
```

New thread, then `$paradox-setup`. Details and differences: [guide/codex.md](guide/codex.md).

## Chat only (ChatGPT or claude.ai)

Each release carries one zip per skill for chat surfaces that cannot run the resolver: [guide/chatgpt.md](guide/chatgpt.md).

## What you get

| Command | What it does |
| --- | --- |
| `paradox-setup` | First-time check, choose guided, expert or terse, route to a new or existing project |
<!-- On Codex every command is $name instead of /pantomimes-paradox:name -->
| `work-start` | Turn an idea into a product understanding, a plan and a first slice |
| `work-adopt` | Bring an existing codebase under the workflow without restarting it |
| `work-steps` | The prompts to paste next, without executing them |
| `work-plan` | Plan one change against the real files and acceptance criteria |
| `work-resume` | Find out where the project actually is and continue |
| `work-deliver` | Carry an approved slice through implementation, review, corrections and evidence |
| `work-review` | Independent findings on a plan or change |
| `work-evidence` | Does the evidence prove the claim for this exact candidate? |
| `work-flow-check` | Trace one user interaction end to end |
| `work-closeout` | Close a milestone, update the records, name the next action |
| `paradox-mode` | Switch between guided, expert and terse |

Read [guide/guided.md](guide/guided.md) for the long version or [guide/expert.md](guide/expert.md) for the one-page version. [guide/commands.md](guide/commands.md) has one paragraph per command.

## How it is built

- **The process is versioned and pinned per project.** Each project records the exact release it follows in its `docs/OPERATING.md`. Updating the plugin never silently changes a project's rules; a project migrates when it chooses to. Old releases stay byte-identical, with hashes checked on every use.
- **The method lives in `playbooks/`**, one shared core plus one file per stage. **Discovery, planning, risk and release references live in `library/`** and load only when their stage opens. **Project scaffolds live in `templates/`.**
- **Every reply ends with a handoff:** where things stand and the single next action you can take now.
- **Independent review is mechanical, not a promise:** a fresh-context reviewer with no editing tools and instructions to change nothing, given the candidate and the requirements but not the author's verdict.
- **Bulk work is delegated so the session stays clear:** reading, external lookups and long check runs go to bounded helpers that return conclusions and citations rather than material. They run on a smaller model; anything judging correctness does not.

## Lineage and licence

MIT. This package continues *Personal Workflows* (the same process under its former name, whose releases 1.0.0 to 1.2.0 are preserved here unchanged) and absorbs *Project Foundry* v3.2, whose method is the library. Some workflow ideas were informed by *Everything Claude Code* (MIT, Affaan Mustafa); see [NOTICE.md](NOTICE.md).

Maintainers: [docs/maintaining.md](docs/maintaining.md).
