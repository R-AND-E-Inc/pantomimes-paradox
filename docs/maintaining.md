# Maintaining the package

## Rules that keep pinned projects safe

1. **Never edit a released playbook.** `playbooks/<release>/` is immutable once its manifest is in `playbooks/manifest.json`. A process change is a new release directory, built from a copy of the previous one.
2. **Never remove a release** while any project may pin it. The former-name releases (`legacy-personal-workflows`, `1.0.0`, `1.1.0`, `1.2.0`) stay forever.
3. **The resolver is read-only.** It selects and verifies; it never installs, fetches, writes, or decides.
4. **The library and templates are not hashed.** They may improve between releases. A stage names the library file to load; keep those names stable or add a release when they change meaning.

## Cutting a process release

```sh
cp -R playbooks/2.0.0 playbooks/2.1.0
rm playbooks/2.1.0/manifest.json
# edit playbooks/2.1.0/core.md and stages/*.md
python3 scripts/build_manifests.py --release 2.1.0
python3 scripts/build_manifests.py --check
```

Then set `BOOTSTRAP` in `scripts/resolve_workflow.py` to the new release (new and adopting projects get it), add a short note under `provenance/` describing what changed and why, bump `version` in both plugin manifests, run the checks below, commit and tag `v<plugin version>`.

## Cutting a plugin release without a process change

Skills, library, templates, guides and scripts can change without a new playbook release. Bump the plugin `version`, run the checks, tag.

## Checks

```sh
python3 -B -m unittest discover -s tests -v
python3 scripts/build_manifests.py --check
python3 scripts/check_package.py
node --test templates/project/.github/scripts/select-ci.test.mjs
claude plugin validate .
```

`verify.yml` runs the first four on every push. `check_package.py` also refuses stray files, oversized files, and project-specific words leaking into shared text.

## Adoption block reference

See `docs/resolver-contract.md`. Blocks written under the former name (`personal-workflows` markers and plugin value) resolve unchanged.

## Migrating an adopted project to a newer release

Change only `release` and `manifest_sha256` in the project's adoption block to the entry in `playbooks/manifest.json`, through the project's own branch, checks and approval. Re-resolve in a fresh session and confirm `mode: adopted` at the new release. Do not migrate a project in the middle of a unit.
