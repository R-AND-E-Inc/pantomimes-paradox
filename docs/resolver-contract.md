# Workflow resolution contract

The package name is `pantomimes-paradox`. Its former name, `personal-workflows`, remains accepted in adoption blocks (both the `plugin` value and the block markers) and in the manifests of the releases published under it, so pinned projects never need editing.

`resolve_workflow.py` is a read-only selector and integrity checker. It does not execute a workflow, create projects, migrate policy, fetch releases, install plugins, invoke tools, or decide approvals and delegation. Those decisions remain in the selected instructions and the user's authorization.

## Project adoption

`docs/OPERATING.md` is the only project workflow-selection authority. An adoption block consists of exactly these markers, with a raw JSON object between them (no Markdown code fence):

```text
<!-- pantomimes-paradox:begin -->
{
  "schema": 1,
  "plugin": "pantomimes-paradox",
  "release": "2.0.0",
  "source": "https://github.com/OWNER/REPOSITORY",
  "source_commit": "FULL_LOWERCASE_GIT_COMMIT",
  "manifest_sha256": "LOWERCASE_SHA256_OF_RELEASE_MANIFEST_BYTES"
}
<!-- pantomimes-paradox:end -->
```

The sample identity values above must be replaced with the actual released identity before adoption. `release` and `manifest_sha256` come from the installed package's `playbooks/manifest.json`. `source_commit` is the Git commit of the installed package, which the package tree itself cannot carry; take it from where the installation recorded it: on Claude Code, the `gitCommitSha` of `pantomimes-paradox@pantomimes-paradox` in `~/.claude/plugins/installed_plugins.json`, or `git -C ~/.claude/plugins/marketplaces/pantomimes-paradox rev-parse HEAD`; for a cloned package (Codex, or `--plugin-dir`), `git -C <package root> rev-parse HEAD`. If none of these is available, stop and ask for the commit; never invent one, because the resolver cannot detect a false value (it reports `source_commit_verified: false`). The resolver requires all six fields and rejects unknown fields, duplicate JSON keys, non-finite numbers, unknown schema versions, ranges, malformed identity values, credentials in the source URL, and incomplete or repeated marker blocks. The source must be an HTTPS repository URL (for this package, `https://github.com/R-AND-E-Inc/pantomimes-paradox`; a trailing `.git` is accepted and not required); Git commits are full 40- or 64-character lowercase hex identities. Releases are exact semantic version strings.

One project selects one workflow release. Change that selection through an explicit migration at a suitable project transition boundary. Updating the global plugin never changes the selection. No adoption block means the project has not adopted the process. A block using the former `personal-workflows` markers is equivalent; a profile may contain only one block of either kind. An unreadable, malformed, or symlinked profile is an error rather than evidence of nonadoption.

## Package and release manifests

The installed package includes `playbooks/manifest.json`:

```json
{
  "schema": 1,
  "plugin": "pantomimes-paradox",
  "bootstrap": "2.0.0",
  "releases": {
    "1.0.0": {"manifest_sha256": "<digest>"},
    "1.1.0": {"manifest_sha256": "<digest>"},
    "1.2.0": {"manifest_sha256": "<digest>"},
    "2.0.0": {"manifest_sha256": "<digest>"},
    "legacy-personal-workflows": {"manifest_sha256": "<digest>"}
  }
}
```

Each `playbooks/<release>/manifest.json` contains `schema`, `plugin`, `release`, `files`, and `skills`. `files` maps relative payload file paths to their SHA-256 values. `skills` maps each supported public skill to an ordered list of payload paths (normally the core and one stage). Every mapped file must be present in `files`. The resolver hashes every listed payload file; it returns only the requested skill's file list for instruction loading.

The legacy release maps exactly the seven existing skills. Unified releases map all ten: the seven existing skills, `work-start`, `work-adopt`, and `work-deliver`. Existing skill names remain stable. The legacy payload preserves the original instructions under `skills/<skill>/SKILL.md`, outside the plugin's public skills-discovery root.

Manifests hash UTF-8 file bytes, including line endings. The release manifest never hashes itself. The package manifest pins its hash; the project independently pins the adopted release-manifest hash. The immutable source Git commit is recorded externally in the project profile, avoiding a self-referential source-SHA cycle.

The package manifest is the trust root for nonadopted legacy/bootstrap use, supplied by the installed package's distribution. It is not authenticated by a new signature system. For adopted projects the project pin must also match. The resolver verifies bytes against manifests, not the Git origin: it returns `source_commit_verified: false` because it performs no network or Git provenance verification. Installation/release validation establishes source provenance separately.

## Invocation and selection

```sh
python3 scripts/resolve_workflow.py --project-root /absolute/project --skill work-plan
python3 scripts/resolve_workflow.py --project-root /absolute/project --skill work-start --bootstrap
```

The default plugin root is the parent of the script's directory. `--plugin-root` overrides it for fixture testing or inspection. Optional `--profile` is an assertion that must identify this project's canonical `docs/OPERATING.md`; it cannot introduce a second profile authority. Project roots must already be directories; a bootstrap request can use an existing empty or projectless directory without creating anything. Platform directory aliases such as `/tmp` may resolve to their real directory, but a symlink supplied as the root or inside a profile/payload path is rejected. Payload paths cannot be absolute, normalized aliases, escaping paths, or symlinks.

| State | Result |
|---|---|
| No adoption block; one of the existing seven skills | `legacy` mode with the verified legacy payload. |
| No adoption block; `work-start` or `work-adopt` with explicit `--bootstrap` | `bootstrap` mode using the verified bootstrap release declared by this package and supported by its resolver (currently `2.2.0`); no adoption is performed. |
| No adoption block; start/adopt without the flag | `bootstrap_required` error. |
| No adoption block; `work-deliver` | `adoption_required` error. |
| Adopted project; any known skill without bootstrap | `adopted` mode using that exact release. |
| Adopted project with bootstrap flag, or another skill with that flag | `invalid_bootstrap` error. |
| Missing selected release, corrupt manifest/payload, unsupported metadata | Compatibility error; never silently latest or legacy. |

Success exits 0 and prints one JSON object containing `status: ready`, mode, release, identity basis, and the ordered absolute file paths plus hashes. Failure exits 1 and prints one JSON object with `status: error`, `code`, and a concise message. When a valid adopted payload cannot be loaded or verified, `required_identity` includes its exact release, source commit and manifest digest for restoration. Invalid CLI syntax uses argparse's normal exit 2. The caller must inspect status/exit code before reading instructions. Errors never grant permission to mutate a project or installation. Restore the exact required release through an authorized installation path rather than substituting another version.

## Generating manifests

```sh
python3 scripts/build_manifests.py --release legacy-personal-workflows
python3 scripts/build_manifests.py --release 1.1.0
python3 scripts/build_manifests.py --release 1.1.0 --check
python3 scripts/build_manifests.py --check
```

The default legacy mappings use `skills/<skill>/SKILL.md`. Unified mappings use `core.md` followed by `stages/<skill-without-work-prefix>.md`. Supply a complete set of repeated `--skill name=path[,path]` arguments when a release uses another arrangement.

The builder includes every file below the selected release except its root `manifest.json`, rejects symlinks/special files, generates deterministic JSON, and updates the package manifest without removing older releases. It refuses to rewrite an existing release manifest when payload bytes changed. `--replace-unreleased` is only for preparing an unreleased staging payload; never use it to revise a published release. `--check` compares manifests without writing. Bare `--check` validates every cataloged release using its recorded skill mappings, requires release directories to match the catalog exactly, and requires both legacy and bootstrap payloads. A release build initially containing only the legacy payload may name its forthcoming bootstrap release; the completed distributable must contain that release and legacy before activation. Python 3.9 or later is required.

Older release retention plus exact project selection preserves workflow instructions across package updates. For example, a project pinned to `1.0.0` continues using `1.0.0` even though this package bootstraps new projects with `2.2.0`. Dispatch remains deliberately small; it must not acquire a second process-policy implementation. Read-only resolution and payload identity checks do not guarantee perfect model adherence, protect against a compromised installation root, or establish native per-project plugin isolation.
