# Using it with Codex

Codex support is second priority. The skills and process files are the same; the packaging differs, and it has had less testing than the Claude Code path. If something does not work, use Claude Code or tell the maintainer.

## Install

Codex loads plugins from a marketplace file. Clone this repository, then register it as a local marketplace and install the plugin:

```sh
git clone https://github.com/R-AND-E-Inc/pantomimes-paradox.git ~/plugins/pantomimes-paradox
```

Create or edit `~/.agents/plugins/marketplace.json` so it contains an entry for this plugin (keep any entries already there):

```json
{
  "name": "personal",
  "interface": { "displayName": "Personal" },
  "plugins": [
    {
      "name": "pantomimes-paradox",
      "source": { "source": "local", "path": "../../plugins/pantomimes-paradox" },
      "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
      "category": "Productivity"
    }
  ]
}
```

Then, in Codex:

```
codex plugin add pantomimes-paradox@personal
```

Alternative without a marketplace: Codex's built-in skill installer can fetch individual skill folders from this repository, for example `skills/work-plan`. Skills installed that way still need the repository's `playbooks/` and `scripts/` next to them, so clone the whole repository rather than installing skills one at a time.

## Differences from Claude Code

- Commands are `$work-plan`, `$paradox-setup`, and so on, with no plugin prefix.
- The skill files mention `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PROJECT_DIR}`; on Codex the package root is two directories above each `SKILL.md`, and the project root is the folder the session runs in (pass it explicitly as `--project-root` if the session is elsewhere).
- Codex has no subagent definitions, so independent review runs as a separate task or session that receives only the neutral brief; the `agents/` folder is ignored.
- The session-start hook that reminds the assistant of the handoff rule is Claude-only. On Codex, add the rule to your global `AGENTS.md` if you want it outside the skills: "End every reply with where the work stands and the single next action."

## Update

```sh
git -C ~/plugins/pantomimes-paradox pull
```

then reinstall the plugin so Codex reloads the files. An update never changes a project's pinned release.
