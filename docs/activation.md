# Observed client activation

Use the existing task/evidence packet for this receipt, not another registry. Record the exact package
source commit or distribution identity, package version, selected process and manifest hash, client
version, installed path, enabled state, actual selected skill path, resolver output and observed
core/stage reads. Keep these facts separate: a hash verifies bytes, a resolver selects a process,
and neither proves native discovery or model compliance. A missing capability is unverified, not PASS.

## Updating the existing Git marketplace

These command forms were inspected on Codex 0.154.0-alpha.6.2 and Claude Code 2.1.247 on 2026-09-21.
Check the installed client's help when it differs. Refresh only the named marketplace:

```sh
codex plugin marketplace upgrade pantomimes-paradox --json
codex plugin add pantomimes-paradox@pantomimes-paradox --json
claude plugin marketplace update pantomimes-paradox
claude plugin update pantomimes-paradox@pantomimes-paradox --scope user
```

Do not patch generated plugin caches. Preserve prior working releases. Codex's separately copied
`templates/codex/agents/*.toml` need comparison when changed; do not overwrite local customizations
without reconciling their purpose. Claude loads the plugin's agent definitions. Keep each client's
standing guidance owner; do not duplicate the reminder as both a hook and global instructions.

Start a fresh session to observe normal discovery after updating. Use the plugin's qualified entrypoint
when another installed workflow exposes the same short name. Keep other projects' plugins installed
unless removal is separately justified and authorized. A running task must explicitly resolve and
read the updated process, or carry its current authorization/plan/evidence pointers into a fresh
session. Installing files does not rewrite a running context.

## Bounded observations on current clients

Codex supports fresh non-resumed `exec --ephemeral --json --output-last-message <path>` sessions;
Claude supports `--print --no-session-persistence --output-format stream-json --verbose
--include-hook-events`. Omit model and effort overrides to retain configured defaults. Capture the
actual effective model/settings and errors, not just a final assertion of what loaded. Use trusted
synthetic workspaces and bounded tools. Read-only shell policy is not proof of every MCP tool's scope.

Claude's session-only `--plugin-dir` can exercise candidate content; verify which plugin actually won
selection when an installed copy exists. No equivalent Codex session-only plugin loader was confirmed
by the inspected help. Explicit source loading remains useful for instruction behavior but is not
installation/discovery proof. An authentication failure blocks live observation and must remain visible;
it does not prevent mechanical package checks.

Native evaluation products may publish reports or use different default judges. Inspect those defaults
and keep reports local unless publication was requested. Do not use an evaluation helper's success as
owner acceptance of the project.

## Project migration

Update the project's sole adoption block only when authorized, after the target release is available
in its required environments. Record the real source commit after it exists; do not couple a new
payload to an old source record. Preserve stricter project bindings, accepted work and current gates.
Default to a unit boundary. An explicit owner instruction can authorize a recorded in-flight exception.
Re-resolve in the active environment and record the actual result. Restore the scoped prior adoption
if activation fails; this does not revert accepted product changes or erase history.
