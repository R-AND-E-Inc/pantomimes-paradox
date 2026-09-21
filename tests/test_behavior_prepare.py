"""Fixture preparation verifies real pin selection; never launches a paid model."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'scripts'))
from prepare_behavior import prepare
from resolve_workflow import BOOTSTRAP


class BehaviorPreparationTests(unittest.TestCase):
    def test_each_case_has_a_real_selected_pin_and_clean_initial_candidate(self):
        cases = json.loads((ROOT / 'tests/behavior/scenarios.json').read_text())['scenarios']
        self.assertEqual(len({s['id'] for s in cases}), len(cases))
        with tempfile.TemporaryDirectory() as tmp:
            for scenario in cases:
                output = Path(tmp) / scenario['id']
                receipt, prompt = prepare(ROOT, output, scenario['id'], BOOTSTRAP, 'a' * 40)
                self.assertEqual(receipt['resolution']['release'], BOOTSTRAP)
                self.assertTrue(receipt['resolution']['identity_verified'])
                self.assertIn(scenario['request'], prompt)
                self.assertNotIn(scenario['oracle']['judgment'], prompt)
                self.assertEqual(subprocess.check_output(['git', '-C', str(output), 'status', '--porcelain']), b'')
                self.assertNotIn('{{BASE_SHA}}', ''.join(p.read_text() for p in output.rglob('*.md')))

    def test_fixture_never_overwrites_an_existing_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'existing'
            output.mkdir()
            (output / 'owner.txt').write_text('preserve')
            with self.assertRaises(FileExistsError):
                prepare(ROOT, output, 'plan-only', BOOTSTRAP, 'a' * 40)
            self.assertEqual((output / 'owner.txt').read_text(), 'preserve')

    def test_output_inside_plugin_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'outside'):
            prepare(ROOT, ROOT / 'generated-case', 'plan-only', BOOTSTRAP, 'a' * 40)


if __name__ == '__main__':
    unittest.main()
