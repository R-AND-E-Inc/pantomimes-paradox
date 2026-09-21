#!/usr/bin/env python3
"""Read-only local tag/source/export alignment. Does not fetch, publish or install."""
import argparse
from pathlib import Path
import subprocess
import sys
import zipfile

sys.dont_write_bytecode = True
from build_exports import SOURCE_URL, skill_files
from package_inventory import check_inventory
from resolve_workflow import WorkflowError, canonical_json, parse_json, safe_file, sha256


def check(root, tag, exports):
    root, exports = Path(root).resolve(), Path(exports).resolve()
    package = check_inventory(root)
    expected_tag = 'v' + package['package_version']
    if tag != expected_tag:
        raise ValueError('Release tag must be ' + expected_tag)
    def git(*args):
        return subprocess.check_output(['git', '-C', str(root), *args], stderr=subprocess.PIPE).decode().strip()
    if git('status', '--porcelain'):
        raise ValueError('Release alignment requires a clean committed source tree')
    commit = git('rev-parse', 'HEAD')
    if git('rev-parse', '--verify', 'refs/tags/' + tag + '^{commit}') != commit:
        raise ValueError('Release tag does not identify the checked source commit')
    release = package['process_release']
    manifest_bytes = (root / 'playbooks' / release / 'manifest.json').read_bytes()
    manifest = parse_json(manifest_bytes, 'release manifest')
    identity = {'schema': 1, 'plugin': 'pantomimes-paradox', 'release': release,
                'source': SOURCE_URL, 'source_commit': commit, 'manifest_sha256': sha256(manifest_bytes)}
    receipt = parse_json(safe_file(exports, 'exports-receipt.json').read_bytes(), 'export receipt')
    for field, expected in [('source_commit', commit), ('package_version', package['package_version']),
                            ('identity', identity), ('package_inventory_sha256', package['inventory_sha256'])]:
        if receipt.get(field) != expected:
            raise ValueError('Export receipt differs: ' + field)
    records = receipt.get('artifacts')
    if not isinstance(records, list):
        raise ValueError('Export artifacts must be a list')
    expected_names = {skill + '-chat-' + release + '.zip': skill for skill in manifest['skills']}
    names = [record.get('file') for record in records if isinstance(record, dict)]
    if len(names) != len(records) or len(names) != len(set(names)) or set(names) != set(expected_names):
        raise ValueError('Missing, extra or duplicate export artifacts')
    if {p.name for p in exports.iterdir()} != set(expected_names) | {'exports-receipt.json'}:
        raise ValueError('Export directory contains missing or extra files')
    for record in records:
        path = safe_file(exports, record['file'])
        if sha256(path.read_bytes()) != record.get('sha256'):
            raise ValueError('Export archive digest differs: ' + path.name)
        expected = skill_files(root, release, expected_names[path.name], identity)
        with zipfile.ZipFile(path) as z:
            if len(z.namelist()) != len(set(z.namelist())) or set(z.namelist()) != set(expected):
                raise ValueError('Export archive membership differs: ' + path.name)
            if record.get('entries') != len(expected):
                raise ValueError('Export entry count differs: ' + path.name)
            for name, data in expected.items():
                if z.read(name) != data:
                    raise ValueError('Export content differs: ' + name)
    return {'status': 'local-release-aligned', 'tag': tag, 'source_commit': commit,
            **{k: v for k, v in package.items() if k not in {'status', 'scope'}},
            'exports': len(records),
            'scope': 'local source/tag/export bytes; publication and client invocation need separate observations'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plugin-root', default=str(Path(__file__).resolve().parents[1]))
    p.add_argument('--tag', required=True)
    p.add_argument('--exports', required=True)
    a = p.parse_args()
    try:
        print(canonical_json(check(a.plugin_root, a.tag, a.exports)).decode(), end='')
    except (WorkflowError, ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError, zipfile.BadZipFile) as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
