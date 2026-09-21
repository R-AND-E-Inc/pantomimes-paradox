"""Package/release checks against real temporary trees, tags and tampered archives."""
from contextlib import redirect_stdout
import io
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
sys.path.insert(0, str(ROOT / 'scripts'))
import check_package
from build_exports import build
from check_release import check
from package_inventory import check_inventory, write_inventory
from resolve_workflow import WorkflowError, sha256


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'package'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', 'dist'))
        write_inventory(self.root)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.git('config', 'core.hooksPath', '/dev/null')
        self.commit()
        self.version = json.loads((self.root / '.claude-plugin/plugin.json').read_text())['version']
        self.tag = 'v' + self.version
        self.exports = Path(self.tmp.name) / 'exports'

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.root), *args], stderr=subprocess.PIPE).decode().strip()

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'Fixture candidate')

    def release(self, annotated=False):
        self.git('tag', *(['-a', self.tag, '-m', 'Fixture release'] if annotated else [self.tag]))
        build(self.root, self.exports)

    def test_candidate_check_is_read_only_and_detects_support_change(self):
        before = {p.relative_to(self.root).as_posix(): (p.read_bytes(), p.stat().st_mtime_ns)
                  for p in self.root.rglob('*') if p.is_file() and '.git' not in p.parts}
        self.assertEqual(check_inventory(self.root)['status'], 'candidate-verified')
        after = {p.relative_to(self.root).as_posix(): (p.read_bytes(), p.stat().st_mtime_ns)
                 for p in self.root.rglob('*') if p.is_file() and '.git' not in p.parts}
        self.assertEqual(before, after)
        (self.root / 'library/README.md').write_text('altered support material')
        with self.assertRaisesRegex(ValueError, 'library/README.md'):
            check_inventory(self.root)

    def test_unknown_path_and_symlink_are_not_silently_excluded(self):
        extra = self.root / 'new-runtime'
        extra.mkdir()
        with self.assertRaisesRegex(ValueError, 'Unclassified'):
            write_inventory(self.root)
        extra.rmdir()
        (self.root / 'guide/alias.md').symlink_to(self.root / 'README.md')
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            write_inventory(self.root)

    def test_manifest_versions_must_agree(self):
        p = self.root / '.codex-plugin/plugin.json'
        value = json.loads(p.read_text())
        value['version'] = '0.0.0'
        p.write_text(json.dumps(value))
        with self.assertRaisesRegex(ValueError, 'versions differ'):
            write_inventory(self.root)

    def test_inventory_itself_cannot_be_a_symlink(self):
        path = self.root / 'package-inventory.json'
        outside = Path(self.tmp.name) / 'inventory.json'
        path.rename(outside)
        path.symlink_to(outside)
        with self.assertRaises(WorkflowError):
            check_inventory(self.root)

    def test_text_scan_covers_current_catalog_release(self):
        path = self.root / 'playbooks/2.2.0/core.md'
        path.write_text(path.read_text() + '\nArtax is an unintended project leak.\n')
        original = check_package.ROOT
        check_package.ROOT = self.root
        try:
            output = io.StringIO()
            with redirect_stdout(output):
                result = check_package.main()
            self.assertEqual(result, 1)
            self.assertIn('playbooks/2.2.0/core.md:', output.getvalue())
        finally:
            check_package.ROOT = original

    def test_exact_and_annotated_tags_align(self):
        self.release(annotated=True)
        result = check(self.root, self.tag, self.exports)
        self.assertEqual(result['source_commit'], self.git('rev-parse', 'HEAD'))
        self.assertEqual(result['exports'], 10)
        self.assertEqual(result['status'], 'local-release-aligned')

    def test_same_stale_versions_do_not_match_another_release_tag(self):
        self.release()
        with self.assertRaisesRegex(ValueError, 'Release tag must be'):
            check(self.root, 'v99.0.0', self.exports)

    def test_missing_tag_is_not_a_candidate_success(self):
        build(self.root, self.exports)
        with self.assertRaises(subprocess.CalledProcessError):
            check(self.root, self.tag, self.exports)

    def test_old_tag_does_not_certify_new_head(self):
        self.release()
        (self.root / 'README.md').write_text('new candidate')
        write_inventory(self.root)
        self.commit()
        with self.assertRaisesRegex(ValueError, 'tag does not identify'):
            check(self.root, self.tag, self.exports)

    def test_receipt_cannot_substitute_another_source(self):
        self.release()
        p = self.exports / 'exports-receipt.json'
        value = json.loads(p.read_text())
        value['source_commit'] = 'a' * 40
        p.write_text(json.dumps(value))
        with self.assertRaisesRegex(ValueError, 'source_commit'):
            check(self.root, self.tag, self.exports)

    def test_rehashed_tampered_archive_fails_source_comparison(self):
        self.release()
        p = self.exports / 'exports-receipt.json'
        receipt = json.loads(p.read_text())
        record = receipt['artifacts'][0]
        archive = self.exports / record['file']
        with zipfile.ZipFile(archive) as z:
            entries = {name: z.read(name) for name in z.namelist()}
        loader = next(name for name in entries if name.endswith('/SKILL.md'))
        entries[loader] = b'Invented instructions'
        with zipfile.ZipFile(archive, 'w') as z:
            for name, content in entries.items():
                z.writestr(name, content)
        record['sha256'] = sha256(archive.read_bytes())
        p.write_text(json.dumps(receipt))
        with self.assertRaisesRegex(ValueError, 'content differs'):
            check(self.root, self.tag, self.exports)

    def test_duplicate_artifacts_fail_even_when_identical(self):
        self.release()
        p = self.exports / 'exports-receipt.json'
        value = json.loads(p.read_text())
        value['artifacts'].append(value['artifacts'][0])
        p.write_text(json.dumps(value))
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            check(self.root, self.tag, self.exports)

    def test_extra_archive_or_uncommitted_source_cannot_pass(self):
        self.release()
        (self.exports / 'extra.zip').write_bytes(b'extra')
        with self.assertRaisesRegex(ValueError, 'extra files'):
            check(self.root, self.tag, self.exports)
        (self.exports / 'extra.zip').unlink()
        (self.root / 'README.md').write_text('dirty')
        write_inventory(self.root)
        with self.assertRaisesRegex(ValueError, 'clean committed'):
            check(self.root, self.tag, self.exports)


if __name__ == '__main__':
    unittest.main()
