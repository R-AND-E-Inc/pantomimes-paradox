#!/usr/bin/env python3
"""Prepare one isolated, source-pinned behavior scenario. Never invokes a model or provider."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
from resolve_workflow import canonical_json, checked_relative, parse_json, sha256


def prepare(root, output, scenario_id, release, source_commit):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Scenario output must be outside the plugin checkout')
    if len(source_commit) != 40 or any(c not in '0123456789abcdef' for c in source_commit):
        raise ValueError('source_commit must be an observed full Git SHA')
    data = parse_json((Path(__file__).resolve().parents[1] / 'tests/behavior/scenarios.json').read_bytes(), 'scenarios')
    matches = [s for s in data['scenarios'] if s['id'] == scenario_id]
    if len(matches) != 1:
        raise ValueError('Unknown or duplicate scenario: ' + scenario_id)
    scenario = matches[0]
    manifest = root / 'playbooks' / checked_relative(release) / 'manifest.json'
    pin = {'schema': 1, 'plugin': 'pantomimes-paradox', 'release': release,
           'source': 'https://github.com/R-AND-E-Inc/pantomimes-paradox',
           'source_commit': source_commit, 'manifest_sha256': sha256(manifest.read_bytes())}
    output.mkdir(parents=True, exist_ok=False)
    def write(name, content):
        path = output / checked_relative(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
    write('docs/OPERATING.md', '# Synthetic workflow fixture\n\n<!-- pantomimes-paradox:begin -->\n' +
          canonical_json(pin).decode() + '<!-- pantomimes-paradox:end -->\n\nGuidance mode: expert\n\n' +
          'Only this fixture is writable. The request defines scope. No external actions, providers, publication or deployment. ' +
          'A listed next card is not authorization. Reuse unchanged evidence with its original identity and the complete intervening diff.\n')
    for name, content in scenario['files'].items():
        write(name, content)
    def git(*args):
        return subprocess.check_output(['git', '-C', str(output), *args], stderr=subprocess.DEVNULL).decode().strip()
    git('init', '-q')
    git('config', 'user.name', 'Workflow fixture')
    git('config', 'user.email', 'fixture@example.invalid')
    git('config', 'core.hooksPath', '/dev/null')
    git('add', '.')
    git('commit', '-qm', 'Synthetic baseline')
    base = git('rev-parse', 'HEAD')
    for name, content in scenario['files'].items():
        if '{{BASE_SHA}}' in content:
            write(name, content.replace('{{BASE_SHA}}', base))
    for name, content in scenario.get('later_files', {}).items():
        write(name, content)
    if git('status', '--porcelain'):
        git('add', '.')
        git('commit', '-qm', 'Synthetic current evidence and candidate')
    # Use the actual resolver CLI: keep its public contract instead of emulating adoption.
    resolved = subprocess.run([sys.executable, '-B', str(root / 'scripts/resolve_workflow.py'),
                              '--project-root', str(output), '--skill', scenario['skill']],
                             capture_output=True, text=True, check=True)
    receipt = {'scenario': scenario_id, 'release': release, 'source_commit': source_commit,
               'fixture_base': base, 'fixture_head': git('rev-parse', 'HEAD'),
               'resolution': json.loads(resolved.stdout), 'oracle': scenario['oracle']}
    return receipt, (
        'Work only in this synthetic fixture. Do not use external services or modify the plugin, client configuration or other projects. '
        'This is a behavior observation, not permission to expand the task.\n\n'
        'Use the exact skill at ' + str(root / 'skills' / scenario['skill'] / 'SKILL.md') +
        ', resolving this working directory\'s declared process and reading the selected payload. '
        'Do not substitute another installed copy.\n\n' + scenario['request'] + '\n')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plugin-root', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--scenario', required=True)
    p.add_argument('--release', required=True)
    p.add_argument('--source-commit', required=True)
    p.add_argument('--receipt', required=True, help='Outside the fixture; includes judge-only oracle')
    p.add_argument('--prompt', required=True, help='Outside the fixture; neutral request for the evaluated agent')
    a = p.parse_args()
    try:
        for path in [a.receipt, a.prompt]:
            dest = Path(path).resolve()
            out = Path(a.output).resolve()
            if dest == out or out in dest.parents:
                raise ValueError('Keep judge-only receipts and prompts outside the fixture')
        receipt, prompt = prepare(a.plugin_root, a.output, a.scenario, a.release, a.source_commit)
        for path, content in [(a.receipt, json.dumps(receipt, indent=2) + '\n'), (a.prompt, prompt)]:
            dest = Path(path)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding='utf-8')
        print(json.dumps({'status': 'prepared', 'scenario': a.scenario, 'fixture': a.output}))
    except (ValueError, OSError, subprocess.CalledProcessError) as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
