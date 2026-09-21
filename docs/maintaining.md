# Maintaining the package

## Preserve project pins

Never edit a released `playbooks/<release>/` payload or its manifest, and never remove a release that
an existing project can pin. Build a new process directory from the prior one, omitting its manifest.
The read-only resolver selects and verifies; it never installs, fetches, writes or decides approval.
Package installation and project adoption remain separate operations.

The project process hash freezes its core/stages. Library, templates, adapters and other support files
are covered by the **package inventory**, not retroactively added to old process hashes. A material
change in a referenced procedure needs a new process release. Do not imply an old process pin freezes
every supporting file in a newer installed package.

## Candidate preparation

1. For a process change, copy the latest process to a new release directory without its manifest,
   edit only the new payload, set `BOOTSTRAP` in `scripts/resolve_workflow.py` and the catalog's
   `bootstrap` to that release, then run `python3 -B scripts/build_manifests.py --release <new-release>`.
   Never use `--replace-unreleased` to alter published bytes.
2. Bump both `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` to the same new package version.
   Both clients cache by version. A package-only change need not create a new process.
3. Update provenance, affected guides/templates and meaningful checks. Compare changed workflow
   behavior using `tests/behavior/README.md` when warranted; normal CI never launches a model.
4. Run `python3 -B scripts/package_inventory.py --write` after the candidate files are complete, then
   the checks below. Regenerate it after every source change, including tests and documentation.
5. Review consequential code/activation changes against the exact candidate. Commit the checked
   source; an uncommitted HEAD is not the full candidate identity.

The inventory covers both plugin/marketplace manifests, hooks, agents, skills, scripts, all playbooks,
library, templates, guides, docs, provenance, tests, repository CI, notices and declared root files.
It rejects unclassified root paths and symlinks. `.git`, `.venv`, `dist` and bytecode caches are excluded;
place generated evidence/exports outside the checkout. The inventory excludes itself to avoid a hash
cycle. Its digest binds candidate bytes; it does not claim source provenance, signature verification,
publication, installation or model behavior.

## Applicable package checks

```sh
python3 -B -m unittest discover -s tests -v
python3 -B scripts/build_manifests.py --check
python3 -B scripts/check_package.py
python3 -B scripts/package_inventory.py --check
node --test templates/project/.github/scripts/select-ci.test.mjs
claude plugin validate .
# Current bundled Codex validators; requires their documented dependencies:
# python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
# python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/<name>
```

CI runs the deterministic Python/manifest/package/inventory and Node checks. `check_package.py` scans
all cataloged current-name process releases for project-specific text; immutable former-name payloads
remain exempt. It also checks roster membership/configuration, not installed clients or semantic parity
of every instruction. Structural client validation is not a consuming-agent behavior evaluation.

## Authorized release

After the reviewed candidate is committed and release is authorized, create the new `v<package-version>`
tag at the intended release commit. Do not move an existing tag. Then:

```sh
python3 -B scripts/build_exports.py --output /outside-checkout/exports
python3 -B scripts/check_release.py --tag v<package-version> --exports /outside-checkout/exports
```

`check_release.py` requires clean source, matching host versions, an exact local tag resolving to HEAD,
valid package/process identities and actual export contents matching source. It rejects missing, extra,
duplicated or altered artifacts even if a receipt claims they are valid. Annotated and lightweight tags
are supported. An absent tag is not an aligned release. The ordinary inventory check reports only
`candidate-verified`, so local preparation does not pretend a release has happened.

The export receipt binds source commit, package inventory digest, selected process and ZIP hashes.
Chat ZIPs still contain only their declared loader/process payload; the inventory digest identifies
the wider source tree, not bundled library/templates. Exports remain deterministic for the same source.
Attach the ZIPs and receipt to the authorized GitHub release, then verify the published tag/source and
asset identities separately. A local `local-release-aligned` result does not prove remote publication.
Tag CI runs the same local alignment. It does not publish or install anything.

## Client and project activation

Use `docs/activation.md` to refresh only the intended marketplace, compare separately installed agents,
and observe the selected entrypoint/core/stage in a fresh client session. Preserve prior working
releases and local customizations. Do not patch generated caches.

Migrate the project's exact adoption block through its existing branch and authorization, using the
real source commit and new manifest identity. Default to a unit boundary; an explicit owner instruction
can authorize a recorded in-flight exception preserving all commitments and valid evidence. Re-resolve
and load the selection in the active implementation environment. Updating installed files alone does
not change the project's pin or an already-running context. Use the scoped recovery procedure in
`docs/activation.md` if activation fails.
