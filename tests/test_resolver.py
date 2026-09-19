"""Observable resolver and manifest behavior against real isolated filesystem fixtures."""

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(SOURCE / "scripts"))
from resolve_workflow import BOOTSTRAP  # noqa: E402

LEGACY = "legacy-personal-workflows"
SEVEN = ("work-steps", "work-plan", "work-resume", "work-review", "work-evidence", "work-flow-check", "work-closeout")
TEN = SEVEN + ("work-start", "work-adopt", "work-deliver")
BEGIN, END = "<!-- pantomimes-paradox:begin -->", "<!-- pantomimes-paradox:end -->"
OLD_BEGIN, OLD_END = "<!-- personal-workflows:begin -->", "<!-- personal-workflows:end -->"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


class ResolverTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="workflow-resolver-")
        self.root = Path(self.temp.name).resolve()
        self.plugin = self.root / "plugin"
        self.project = self.root / "project"
        self.project.mkdir()
        (self.plugin / "scripts").mkdir(parents=True)
        for name in ("resolve_workflow.py", "build_manifests.py"):
            shutil.copyfile(SOURCE / "scripts" / name, self.plugin / "scripts" / name)
        self.legacy_bytes = {}
        legacy_root = self.plugin / "playbooks" / LEGACY
        for skill in SEVEN:
            path = legacy_root / "skills" / skill / "SKILL.md"
            path.parent.mkdir(parents=True)
            data = ("---\nname: " + skill + "\n---\nOriginal legacy instructions — " + skill + "\n").encode()
            path.write_bytes(data)
            self.legacy_bytes[skill] = data
        self.build(LEGACY)
        self.add_release("1.0.0")
        self.add_release(BOOTSTRAP)

    def tearDown(self):
        self.temp.cleanup()

    def command(self, script, *arguments):
        process = subprocess.run(
            [sys.executable, "-B", str(self.plugin / "scripts" / script), *map(str, arguments)],
            capture_output=True, text=True, cwd=self.root,
        )
        self.assertEqual(process.stderr, "", process.stderr)
        return process.returncode, json.loads(process.stdout)

    def build(self, release, *arguments, success=True):
        code, value = self.command("build_manifests.py", "--release", release, *arguments)
        self.assertEqual(code, 0 if success else 1, value)
        return value

    def add_release(self, release):
        path = self.plugin / "playbooks" / release
        (path / "stages").mkdir(parents=True)
        (path / "core.md").write_text("Core " + release + "\n")
        for skill in TEN:
            (path / "stages" / (skill[5:] + ".md")).write_text(release + " " + skill + "\n")
        self.build(release)

    def profile(self, release="1.0.0", **updates):
        path = self.plugin / "playbooks" / release / "manifest.json"
        value = {"schema": 1, "plugin": "pantomimes-paradox", "release": release,
                 "source": "https://github.com/example/pantomimes-paradox",
                 "source_commit": "a" * 40, "manifest_sha256": digest(path.read_bytes())}
        value.update(updates)
        self.write_profile(BEGIN + "\n" + json.dumps(value) + "\n" + END)
        return value

    def write_profile(self, content):
        path = self.project / "docs/OPERATING.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text(content)

    def resolve(self, skill="work-plan", *arguments, success=True):
        code, value = self.command("resolve_workflow.py", "--project-root", self.project, "--skill", skill, *arguments)
        self.assertEqual(code, 0 if success else 1, value)
        return value

    def rewrite_manifest(self, mutate, release="1.0.0", adopt=True):
        path = self.plugin / "playbooks" / release / "manifest.json"
        value = json.loads(path.read_bytes())
        mutate(value)
        path.write_bytes(json_bytes(value))
        catalog_path = self.plugin / "playbooks/manifest.json"
        catalog = json.loads(catalog_path.read_bytes())
        catalog["releases"][release]["manifest_sha256"] = digest(path.read_bytes())
        catalog_path.write_bytes(json_bytes(catalog))
        if adopt:
            self.profile(release)

    def snapshot(self):
        result = {}
        for root in (self.plugin, self.project):
            for path in root.rglob("*"):
                info = path.lstat()
                result[str(path)] = (info.st_mode, info.st_mtime_ns,
                                     path.read_bytes() if path.is_file() else None)
        return result

    def test_all_legacy_skills_preserve_bytes(self):
        for skill in SEVEN:
            with self.subTest(skill=skill):
                value = self.resolve(skill)
                self.assertEqual(value["mode"], "legacy")
                self.assertEqual(value["release"], LEGACY)
                self.assertEqual(len(value["files"]), 1)
                self.assertEqual(Path(value["files"][0]["path"]).read_bytes(), self.legacy_bytes[skill])

    def test_existing_operating_without_adoption_is_legacy(self):
        self.write_profile("# Operating\nUse the existing project process.\n")
        self.assertEqual(self.resolve()["mode"], "legacy")

    def test_all_adopted_skills_select_only_core_and_stage(self):
        self.profile()
        for skill in TEN:
            with self.subTest(skill=skill):
                value = self.resolve(skill)
                self.assertEqual(value["mode"], "adopted")
                self.assertTrue(value["identity_verified"])
                self.assertFalse(value["source_commit_verified"])
                self.assertEqual([Path(item["path"]).name for item in value["files"]], ["core.md", skill[5:] + ".md"])

    def test_explicit_start_and_adopt_bootstrap_do_not_adopt(self):
        before = self.snapshot()
        for skill in ("work-start", "work-adopt"):
            result = self.resolve(skill, "--bootstrap")
            self.assertEqual(result["mode"], "bootstrap")
            self.assertEqual(result["release"], BOOTSTRAP)
            self.assertEqual(self.resolve(skill, success=False)["code"], "bootstrap_required")
        self.assertEqual(self.snapshot(), before)

    def test_deliver_requires_adoption(self):
        self.assertEqual(self.resolve("work-deliver", success=False)["code"], "adoption_required")

    def test_bootstrap_cannot_bypass_project_pin(self):
        self.profile()
        self.assertEqual(self.resolve("work-adopt", "--bootstrap", success=False)["code"], "invalid_bootstrap")
        self.assertEqual(self.resolve("work-plan", "--bootstrap", success=False)["code"], "invalid_bootstrap")

    def test_unknown_skill_rejected(self):
        self.assertEqual(self.resolve("../work-plan", success=False)["code"], "unknown_skill")

    def test_multiple_projects_keep_distinct_pins_after_package_upgrade(self):
        self.profile()
        first = self.resolve()
        older_project = self.project
        self.add_release("1.3.0")
        self.assertEqual(self.resolve(), first)
        self.project = self.root / "second-project"
        self.project.mkdir()
        self.profile("1.3.0")
        second = self.resolve()
        self.assertEqual(second["release"], "1.3.0")
        self.assertNotEqual(second["manifest_sha256"], first["manifest_sha256"])
        self.project = older_project
        self.assertEqual(self.resolve(), first)

    def test_read_only_resolution_and_check(self):
        self.profile()
        before = self.snapshot()
        self.resolve()
        code, value = self.command("build_manifests.py", "--check")
        self.assertEqual(code, 0, value)
        self.assertEqual(self.snapshot(), before)

    def test_reproducible_and_idempotent_manifests(self):
        before = self.snapshot()
        self.build("1.0.0")
        self.build(LEGACY)
        self.assertEqual(self.snapshot(), before)

    def test_release_builder_refuses_changed_existing_release(self):
        (self.plugin / "playbooks/1.0.0/core.md").write_text("Changed process\n")
        before = self.snapshot()
        self.assertEqual(self.build("1.0.0", success=False)["code"], "immutable_release")
        self.assertEqual(self.snapshot(), before)

    def test_staging_rebuild_invalidates_old_project_pin(self):
        self.profile()
        (self.plugin / "playbooks/1.0.0/core.md").write_text("Unreleased corrected process\n")
        self.build("1.0.0", "--replace-unreleased")
        self.assertEqual(self.resolve(success=False)["code"], "integrity_mismatch")

    def test_check_rejects_uncataloged_release_and_untracked_files(self):
        (self.plugin / "playbooks/9.9.9").mkdir()
        code, value = self.command("build_manifests.py", "--check")
        self.assertEqual((code, value["code"]), (1, "untracked_release"))
        (self.plugin / "playbooks/9.9.9").rmdir()
        (self.plugin / "playbooks/notes.txt").write_text("Untracked\n")
        code, value = self.command("build_manifests.py", "--check")
        self.assertEqual((code, value["code"]), (1, "untracked_payload"))

    def test_check_rejects_missing_cataloged_release(self):
        shutil.rmtree(self.plugin / "playbooks/1.0.0")
        code, value = self.command("build_manifests.py", "--check")
        self.assertEqual((code, value["code"]), (1, "untracked_release"))

    def test_missing_pin_never_uses_latest_or_legacy(self):
        self.profile(release="1.0.0")
        path = self.project / "docs/OPERATING.md"
        path.write_text(path.read_text().replace('"1.0.0"', '"9.0.0"'))
        failure = self.resolve(success=False)
        self.assertEqual(failure["code"], "missing_release")
        self.assertEqual(failure["required_identity"]["release"], "9.0.0")
        self.assertEqual(failure["required_identity"]["source_commit"], "a" * 40)
        self.assertEqual(len(failure["required_identity"]["manifest_sha256"]), 64)

    def test_deleting_manifest_does_not_remove_catalog_immutability(self):
        release = self.plugin / "playbooks/1.0.0"
        original = (release / "core.md").read_bytes()
        (release / "manifest.json").unlink()
        (release / "core.md").write_bytes(original + b"Changed process\n")
        code, value = self.command("build_manifests.py", "--release", "1.0.0")
        self.assertEqual((code, value["code"]), (1, "immutable_release"))
        (release / "core.md").write_bytes(original)
        code, value = self.command("build_manifests.py", "--release", "1.0.0")
        self.assertEqual((code, value["status"]), (0, "built"))

    def test_profile_unknown_fields_bad_types_and_versions(self):
        cases = ({"extra": True}, {"schema": True}, {"schema": 2},
                 {"plugin": "other"}, {"release": "latest"}, {"release": "../1.0.0"},
                 {"manifest_sha256": "z" * 64}, {"source_commit": "main"},
                 {"source": "https://secret@github.com/example/repo"},
                 {"source": "https://github.com/example/repo?token=secret"}, {"source": None})
        for updates in cases:
            with self.subTest(updates=updates):
                value = self.profile()
                value.update(updates)
                self.write_profile(BEGIN + json.dumps(value) + END)
                self.resolve(success=False)

    def test_malformed_and_duplicate_metadata_blocks(self):
        values = (BEGIN, END, END + BEGIN, BEGIN + "{}" + END + BEGIN + "{}" + END,
                  BEGIN + "```json\n{}\n```" + END, BEGIN + "not JSON" + END)
        for content in values:
            with self.subTest(content=content):
                self.write_profile(content)
                self.resolve(success=False)

    def test_duplicate_json_keys_fail_in_profile_catalog_and_manifest(self):
        self.profile()
        path = self.project / "docs/OPERATING.md"
        original = path.read_text()
        path.write_text(original.replace('"schema": 1', '"schema": 1, "schema": 1'))
        self.assertEqual(self.resolve(success=False)["code"], "invalid_json")
        path.write_text(original)
        catalog = self.plugin / "playbooks/manifest.json"
        original_catalog = catalog.read_text()
        catalog.write_text(original_catalog.replace('"schema": 1', '"schema": 1, "schema": 1'))
        self.assertEqual(self.resolve(success=False)["code"], "invalid_json")
        catalog.write_text(original_catalog)
        manifest = self.plugin / "playbooks/1.0.0/manifest.json"
        manifest.write_text(manifest.read_text().replace('"schema": 1', '"schema": 1, "schema": 1'))
        value = json.loads(catalog.read_bytes())
        value["releases"]["1.0.0"]["manifest_sha256"] = digest(manifest.read_bytes())
        catalog.write_bytes(json_bytes(value))
        self.profile()
        self.assertEqual(self.resolve(success=False)["code"], "invalid_json")

    def test_nonfinite_json_is_invalid(self):
        self.write_profile(BEGIN + '{"schema": NaN}' + END)
        self.assertEqual(self.resolve(success=False)["code"], "invalid_json")

    def test_profile_manifest_digest_mismatch(self):
        self.profile(manifest_sha256="0" * 64)
        self.assertEqual(self.resolve(success=False)["code"], "integrity_mismatch")

    def test_package_manifest_digest_mismatch(self):
        self.profile()
        path = self.plugin / "playbooks/1.0.0/manifest.json"
        path.write_bytes(path.read_bytes() + b"\n")
        self.assertEqual(self.resolve(success=False)["code"], "integrity_mismatch")

    def test_modified_unselected_stage_is_detected(self):
        self.profile()
        (self.plugin / "playbooks/1.0.0/stages/closeout.md").write_text("Corruption\n")
        self.assertEqual(self.resolve("work-plan", success=False)["code"], "integrity_mismatch")

    def test_unsafe_manifest_paths_even_with_matching_hash_pins(self):
        for bad in ("../outside.md", "/tmp/outside.md", "stages/../core.md", "./core.md", "stages//plan.md", "stages\\plan.md"):
            with self.subTest(path=bad):
                self.rewrite_manifest(lambda value: value["files"].update({bad: "0" * 64}))
                self.assertEqual(self.resolve(success=False)["code"], "unsafe_path")
                # Restore a clean staging manifest for the next case.
                self.build("1.0.0", "--replace-unreleased")

    def test_unhashed_and_duplicate_skill_file_references(self):
        for paths in (["unlisted.md"], ["core.md", "core.md"]):
            self.rewrite_manifest(lambda value: value["skills"].update({"work-plan": paths}))
            self.assertEqual(self.resolve(success=False)["code"], "invalid_manifest")
            self.build("1.0.0", "--replace-unreleased")

    def test_windows_drive_and_stream_paths_fail_closed(self):
        for bad in ("C:/outside.md", "core.md:stream"):
            self.rewrite_manifest(lambda value: value["files"].update({bad: "0" * 64}))
            self.assertEqual(self.resolve(success=False)["code"], "unsafe_path")
            self.build("1.0.0", "--replace-unreleased")

    def test_manifest_cannot_hash_itself(self):
        self.rewrite_manifest(lambda value: value["files"].update({"manifest.json": "0" * 64}))
        self.assertEqual(self.resolve(success=False)["code"], "invalid_manifest")

    def test_symlink_profile_and_dangling_profile_fail_closed(self):
        outside = self.root / "external.md"
        outside.write_text("No metadata\n")
        directory = self.project / "docs"
        directory.mkdir()
        path = directory / "OPERATING.md"
        path.symlink_to(outside)
        self.assertEqual(self.resolve(success=False)["code"], "unsafe_path")
        outside.unlink()
        self.assertEqual(self.resolve(success=False)["code"], "unsafe_path")

    def test_symlink_profile_directory_fail_closed(self):
        outside = self.root / "other-docs"
        outside.mkdir()
        (self.project / "docs").symlink_to(outside, target_is_directory=True)
        self.assertEqual(self.resolve(success=False)["code"], "unsafe_path")

    def test_symlink_payload_file_rejected_even_if_identical(self):
        self.profile()
        path = self.plugin / "playbooks/1.0.0/core.md"
        outside = self.root / "core.md"
        outside.write_bytes(path.read_bytes())
        path.unlink()
        path.symlink_to(outside)
        self.assertEqual(self.resolve(success=False)["code"], "unsafe_path")
        self.assertEqual(self.build("1.0.0", success=False)["code"], "unsafe_path")

    def test_symlink_release_directory_rejected(self):
        self.profile()
        path = self.plugin / "playbooks/1.0.0"
        outside = self.root / "external-release"
        path.rename(outside)
        path.symlink_to(outside, target_is_directory=True)
        self.assertEqual(self.resolve(success=False)["code"], "unsafe_path")

    def test_symlink_root_rejected(self):
        link = self.root / "project-link"
        link.symlink_to(self.project, target_is_directory=True)
        self.project = link
        self.assertEqual(self.resolve(success=False)["code"], "unsafe_path")

    def test_missing_package_root_reports_valid_adopted_identity(self):
        expected = self.profile()
        before = self.snapshot()
        failure = self.resolve("work-plan", "--plugin-root", self.root / "missing-package", success=False)
        self.assertEqual(failure["code"], "missing_root")
        self.assertEqual(failure["required_identity"], expected)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / "missing-package").exists())

    def test_symlinked_package_root_rejected_with_valid_adopted_identity(self):
        expected = self.profile()
        link = self.root / "package-link"
        link.symlink_to(self.plugin, target_is_directory=True)
        before = self.snapshot()
        failure = self.resolve("work-plan", "--plugin-root", link, success=False)
        self.assertEqual(failure["code"], "unsafe_path")
        self.assertEqual(failure["required_identity"], expected)
        self.assertEqual(self.snapshot(), before)
        self.assertTrue(link.is_symlink())

    def test_invalid_profile_never_supplies_identity_for_missing_package_root(self):
        value = self.profile()
        self.write_profile(BEGIN + json.dumps(value).replace('"schema": 1', '"schema": 1, "schema": 1') + END)
        failure = self.resolve("work-plan", "--plugin-root", self.root / "missing-package", success=False)
        self.assertEqual(failure["code"], "invalid_json")
        self.assertNotIn("required_identity", failure)

    def test_nonadopted_profile_never_supplies_identity_for_missing_package_root(self):
        self.write_profile("# Existing operating instructions\n")
        failure = self.resolve("work-plan", "--plugin-root", self.root / "missing-package", success=False)
        self.assertEqual(failure["code"], "missing_root")
        self.assertNotIn("required_identity", failure)

    def test_explicit_profile_is_only_an_assertion_of_existing_authority(self):
        self.profile()
        expected = self.resolve()
        self.assertEqual(self.resolve("work-plan", "--profile", self.project / "docs/OPERATING.md"), expected)
        unrelated = self.root / "unrelated.md"
        unrelated.write_text((self.project / "docs/OPERATING.md").read_text())
        self.assertEqual(self.resolve("work-plan", "--profile", unrelated, success=False)["code"], "invalid_profile_path")

    def test_personal_workflows_adoption_blocks_still_resolve(self):
        # Projects adopted under the old name keep resolving without editing their profile.
        value = self.profile()
        value["plugin"] = "personal-workflows"
        self.write_profile(OLD_BEGIN + "\n" + json.dumps(value) + "\n" + OLD_END)
        result = self.resolve()
        self.assertEqual((result["mode"], result["plugin"]), ("adopted", "pantomimes-paradox"))
        value["plugin"] = "pantomimes-paradox"
        self.write_profile(OLD_BEGIN + json.dumps(value) + OLD_END)
        self.assertEqual(self.resolve()["mode"], "adopted")

    def test_mixed_or_duplicate_marker_families_fail_closed(self):
        value = self.profile()
        both = BEGIN + json.dumps(value) + END + OLD_BEGIN + json.dumps(value) + OLD_END
        self.write_profile(both)
        self.assertEqual(self.resolve(success=False)["code"], "invalid_profile")
        self.write_profile(BEGIN + json.dumps(value) + OLD_END)
        self.assertEqual(self.resolve(success=False)["code"], "invalid_profile")

    def test_package_catalog_must_carry_the_current_package_name(self):
        catalog_path = self.plugin / "playbooks/manifest.json"
        catalog = json.loads(catalog_path.read_bytes())
        catalog["plugin"] = "personal-workflows"
        catalog_path.write_bytes(json_bytes(catalog))
        self.assertEqual(self.resolve(success=False)["code"], "invalid_schema")

    def test_builder_explicit_mapping_and_check_all_preserve_order(self):
        mappings = []
        for skill in TEN:
            mappings.extend(("--skill", skill + "=stages/" + skill[5:] + ".md,core.md"))
        self.build("1.0.0", "--replace-unreleased", *mappings)
        self.profile()
        self.assertEqual(Path(self.resolve()["files"][0]["path"]).name, "plan.md")
        code, value = self.command("build_manifests.py", "--check")
        self.assertEqual(code, 0, value)


if __name__ == "__main__":
    unittest.main()
