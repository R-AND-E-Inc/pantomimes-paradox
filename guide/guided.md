# The guided tour

This is the long version. If you have run software projects with an assistant before, read [expert.md](expert.md) instead.

## What this actually is

An AI coding assistant will happily build the wrong thing quickly. It will pick a database before it knows what you are making, tell you a test passed when it never ran, review its own work and find nothing, and leave you wondering what to type next.

The Pantomime's Paradox is a set of rules the assistant follows so that none of that happens. The rules are written for the assistant, not for you; you never have to read them. What you see is the behaviour:

1. **It understands the product before it chooses technology.** It asks a few questions at a time, proposes answers you only have to correct, and does not write code until the plan is sufficient.
2. **It works in small slices you can check.** Each slice names one thing you will be able to do at the end that you could not do before.
3. **It proves what it claims.** "Tests pass" comes with which tests, at which exact version, in which environment. A test that did not run is never a pass.
4. **Risky changes get a second, fresh pair of eyes.** A separate reviewer that did not write the code and is not told what to conclude.
5. **Every reply ends with the next step.** One thing you can do right now.

## Installing it

Open Claude Code and run:

```
/plugin marketplace add R-AND-E-Inc/pantomimes-paradox
/plugin install pantomimes-paradox@pantomimes-paradox
```

Start a new session so the plugin loads. That is the whole installation.

## Your first ten minutes

Open Claude Code in a folder. It can be empty (a new idea) or an existing project. Type:

```
/pantomimes-paradox:paradox-setup
```

It will check that the plugin is intact, ask whether you want guided or expert mode, ask whether this is a new idea or an existing codebase, and give you the one prompt to paste next. Guided mode means every reply explains what just happened, why the next step matters, what you will see, and how to tell it worked. You can switch any time with `/pantomimes-paradox:paradox-mode expert`.

### A new idea

Paste the prompt it gave you, something like:

```
/pantomimes-paradox:work-start a small tool that helps me sort my reference photos by project
```

The assistant restates your idea in its own words, separates what it knows from what it is assuming, and asks its first small batch of questions. Each question comes with a recommended answer; correct only what is wrong. When it has enough, it says so and proposes a plan with a first slice. **Planning never starts building.** When you are ready to build, you say so, and it will tell you the exact words.

### An existing project

```
/pantomimes-paradox:work-adopt this project; inspect it and propose the migration first
```

It reads the code, tests and any notes before asking you anything, tells you what already exists, what is documented, what has drifted, and proposes how to bring the project under the workflow without restarting it. Nothing is changed until you approve.

## The daily loop

Most days you use three prompts.

**Where am I?**

```
/pantomimes-paradox:work-resume
```

It reads the project's own records and the repository, tells you what is done, what is in progress, what is waiting on you, and continues the already-approved work.

**What do I do next?**

```
/pantomimes-paradox:work-steps for the next slice
```

It returns the prompts to paste, in order, with what to expect from each. It does not run them.

**Build the approved slice.**

```
/pantomimes-paradox:work-deliver the approved slice
```

It implements, gets the required review, makes justified corrections, gathers evidence, and stops at the next point where your decision or approval is needed. It does not merge or publish.

Plain language also works. "Where were we?", "what's next?", and "build it" reach the same skills; the commands are the reliable spelling.

## What the project looks like on disk

The assistant keeps its memory in the repository, not in the conversation, so a new session picks up exactly where the last one ended. For anything bigger than a single-session utility you will see:

| File | What it holds |
| --- | --- |
| `CLAUDE.md` (and an identical `AGENTS.md`) | The permanent rules of this project |
| `docs/OPERATING.md` | Which process release the project follows, your guidance mode, and the project's own checks and approval rules |
| `docs/PROJECT_STATE.md` | What exists, what is in progress, what is waiting on you, and the next action |
| `docs/plans/` | Approved contracts and plans |
| `docs/PHASE_HISTORY.md` | What was decided and closed, with evidence |

You do not need to edit these. You will be asked to read `PROJECT_STATE.md` occasionally, and it is written for you.

## Your role

You decide what the product should do, resolve the tradeoffs that matter, judge how it feels to use, and give the approvals: to start building, to merge, to release. The assistant does the inspecting, building, checking and record-keeping. When it asks you something, it is because the answer changes what gets built; it should not ask you to relay messages between its own steps or to repeat yourself.

## Words you will see

- **Slice, card, unit:** one bounded piece of work with one observable result.
- **Contract:** what a slice must achieve, written down before building, with acceptance criteria you can check.
- **Candidate:** the exact version being judged (a commit), never "the latest".
- **Evidence:** what was actually observed, at which candidate, in which environment, and what that observation can and cannot prove.
- **PASS / FAIL / BLOCKED / WAIVED / NOT APPLICABLE:** the only allowed results. Waived means you accepted the gap on purpose; it is never a pass.
- **Independent review:** a fresh context that did not write the code and is not told what to find.
- **Handoff:** the last lines of every reply: where things stand and what to do next.
- **Guidance mode:** guided or expert; how much the handoff explains.

## When something goes wrong

- **It keeps failing the same fix.** After two failed attempts on one defect the workflow requires a fresh context, and after three rounds it stops and asks you to split, defer or replan. That is the rule working, not the tool failing.
- **It says something cannot be verified.** That is a real answer. Ask what would make it verifiable, or accept the gap on record.
- **It says the process release cannot be resolved.** The project pins an exact release and the installed plugin does not carry it, or the files do not match their hashes. Reinstall the plugin; never edit the pin to make the error go away.
- **You want less explanation.** `/pantomimes-paradox:paradox-mode expert`.

## Updating

```
/plugin update pantomimes-paradox
```

Updating the plugin never changes an existing project's process. A project keeps the release it pinned until you ask it to migrate, which is an ordinary reviewed change.
