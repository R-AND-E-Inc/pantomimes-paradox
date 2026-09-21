#!/usr/bin/env python3
"""Build/check package byte identity separately from immutable project process pins."""
import argparse
from pathlib import Path
import stat
import sys

sys.dont_write_bytecode = True
from build_manifests import atomic_write, check_all
from resolve_workflow import WorkflowError, canonical_json, checked_root, parse_json, safe_file, sha256

INVENTORY = 'package-inventory.json'
DIRECTORIES = {'.agents', '.claude-plugin', '.codex-plugin', '.github', 'agents', 'docs',
               'guide', 'hooks', 'library', 'playbooks', 'provenance', 'scripts', 'skills',
               'templates', 'tests'}
ROOT_FILES = {'.gitignore', 'LICENSE', 'NOTICE.md', 'README.md'}
DEVELOPMENT = {'.git', '.venv', 'dist', '__pycache__'}


def package_version(root):
    versions = []
    for name in ('.claude-plugin/plugin.json', '.codex-plugin/plugin.json'):
        data = parse_json((root / name).read_bytes(), name)
        if data['name'] != 'pantomimes-paradox':
            raise ValueError('Unexpected package name: ' + name)
        versions.append(data['version'])
    if len(set(versions)) != 1:
        raise ValueError('Plugin versions differ between Claude and Codex')
    return versions[0]


def inventory(root):
    root = checked_root(root, 'Package root')
    check_all(root)
    files = {}
    def visit(path):
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise ValueError('Symlink in package: ' + str(path.relative_to(root)))
        if stat.S_ISDIR(mode):
            for child in sorted(path.iterdir()):
                if child.name == '__pycache__':
                    continue
                visit(child)
        elif stat.S_ISREG(mode):
            data = path.read_bytes()
            files[path.relative_to(root).as_posix()] = {'bytes': len(data), 'sha256': sha256(data)}
        else:
            raise ValueError('Non-regular package file: ' + str(path))
    for path in sorted(root.iterdir()):
        if path.name in DEVELOPMENT or path.name == INVENTORY:
            continue
        if path.name not in DIRECTORIES | ROOT_FILES:
            raise ValueError('Unclassified package path: ' + path.name)
        visit(path)
    catalog = parse_json((root / 'playbooks/manifest.json').read_bytes(), 'catalog')
    return {'schema': 1, 'plugin': 'pantomimes-paradox', 'package_version': package_version(root),
            'bootstrap': catalog['bootstrap'], 'files': files}


def write_inventory(root):
    value = inventory(root)
    atomic_write(Path(root) / INVENTORY, canonical_json(value))
    return value


def check_inventory(root):
    root = checked_root(root, 'Package root')
    value = inventory(root)
    recorded_bytes = safe_file(root, INVENTORY).read_bytes()
    recorded = parse_json(recorded_bytes, INVENTORY)
    if recorded != value:
        old = recorded.get('files', {}) if isinstance(recorded, dict) else {}
        changed = sorted(p for p in set(old) | set(value['files']) if old.get(p) != value['files'].get(p))
        raise ValueError('Package inventory differs: ' + (', '.join(changed[:8]) or 'metadata'))
    return {'status': 'candidate-verified', 'package_version': value['package_version'],
            'process_release': value['bootstrap'], 'files': len(value['files']),
            'inventory_sha256': sha256(recorded_bytes),
            'scope': 'package bytes; not Git provenance, publication, installation or invocation'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plugin-root', default=str(Path(__file__).resolve().parents[1]))
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    a = p.parse_args()
    try:
        if a.write:
            write_inventory(a.plugin_root)
        print(canonical_json(check_inventory(a.plugin_root)).decode(), end='')
    except (WorkflowError, ValueError, OSError, KeyError) as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
