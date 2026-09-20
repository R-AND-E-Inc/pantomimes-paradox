"""The Codex delegate roster must stay readable by the oldest supported Python.

check_package.py inspects the Codex `.toml` delegates. `tomllib` only exists from Python 3.11,
so the check carries a line scanner for older interpreters. A scanner that disagreed with the real
parser would let the roster drift while still reporting success, which is the failure this guards.
"""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "scripts"))
import check_package  # noqa: E402

AGENT_FILES = sorted((ROOT / "templates/codex/agents").glob("*.toml"))


class CodexAgentTests(unittest.TestCase):
    def test_roster_is_not_empty(self):
        self.assertEqual(len(AGENT_FILES), len(check_package.AGENTS))

    def test_scanner_matches_tomllib_on_every_delegate(self):
        try:
            import tomllib
        except ModuleNotFoundError:
            self.skipTest("tomllib needs Python 3.11; the scanner is the only path here")
        for path in AGENT_FILES:
            with self.subTest(agent=path.stem):
                text = path.read_text()
                parsed = tomllib.loads(text)
                check_package.tomllib = None
                try:
                    scanned, how = check_package.read_agent_toml(text)
                finally:
                    check_package.tomllib = tomllib
                self.assertEqual(how, "scanned")
                self.assertEqual(set(parsed), set(scanned))
                for key in parsed:
                    self.assertEqual(parsed[key].strip(), scanned[key].strip(), key)

    def test_check_passes_on_both_paths(self):
        try:
            import tomllib
        except ModuleNotFoundError:
            tomllib = None
        for forced in (tomllib, None):
            with self.subTest(parser="tomllib" if forced else "scanner"):
                original = check_package.tomllib
                check_package.tomllib = forced
                try:
                    self.assertEqual(check_package.main(), 0)
                finally:
                    check_package.tomllib = original


if __name__ == "__main__":
    unittest.main()
