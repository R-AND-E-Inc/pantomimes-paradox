import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "scripts"))
from build_exports import build  # noqa: E402


def fixture(tmp):
    root = Path(tmp) / "package"
    shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "dist"))
    git = lambda *a: subprocess.check_output(["git", "-C", str(root), *a], stderr=subprocess.STDOUT)  # noqa: E731
    git("init", "-b", "fixture")
    git("add", ".")
    git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", "Fixture")
    return root


class ExportTests(unittest.TestCase):
    def test_exports_are_reproducible_and_byte_identical_to_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = fixture(tmp)
            first = build(root, Path(tmp) / "one")
            second = build(root, Path(tmp) / "two")
            self.assertEqual(first, second)
            release = first["identity"]["release"]
            manifest = json.loads((root / "playbooks" / release / "manifest.json").read_text())
            self.assertEqual(len(first["artifacts"]), len(manifest["skills"]))
            for record in first["artifacts"]:
                archive = Path(tmp) / "one" / record["file"]
                self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), record["sha256"])
                skill = archive.name.split("-chat-")[0]
                with zipfile.ZipFile(archive) as z:
                    self.assertEqual(json.loads(z.read(skill + "/identity.json")), first["identity"])
                    loader = z.read(skill + "/SKILL.md").decode()
                    self.assertTrue(loader.startswith("---\nname: " + skill + "\n"))
                    for name in manifest["skills"][skill]:
                        content = z.read(skill + "/payload/" + name)
                        self.assertEqual(content, (root / "playbooks" / release / name).read_bytes())
                        self.assertEqual(hashlib.sha256(content).hexdigest(), manifest["files"][name])
                        self.assertIn("`payload/" + name + "`", loader)
                    if skill == "work-deliver":
                        self.assertIn(skill + "/payload/stages/steps.md", z.namelist())
            with self.assertRaisesRegex(ValueError, "outside"):
                build(root, root / "dist")
            (root / "README.md").write_text("uncommitted")
            with self.assertRaisesRegex(ValueError, "clean"):
                build(root, Path(tmp) / "dirty")


if __name__ == "__main__":
    unittest.main()
