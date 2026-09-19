import assert from 'node:assert/strict';
import test from 'node:test';
import { comparisonBase, isDocumentationPath, needsFullSuite, needsWorkflowChecks } from './select-ci.mjs';

test('documentation and retained review artifacts select documentation verification only', () => {
  for (const path of ['docs/OPERATING.md', 'docs/PROJECT_STATE.md', 'docs/evidence/review.png', 'docs/evidence/prototype.html', 'docs/evidence/observations.json', 'AGENTS.md', 'CLAUDE.md', 'README.md']) {
    assert.equal(isDocumentationPath(path), true, path);
    assert.equal(needsFullSuite([path]), false, path);
    assert.equal(needsWorkflowChecks([path]), false, path);
  }
});

test('workflow changes select operator checks without the application suite', () => {
  assert.equal(needsFullSuite(['.github/workflows/ci.yml']), false);
  assert.equal(needsWorkflowChecks(['.github/workflows/ci.yml']), true);
});

test('application, dependency, migration and unknown paths retain full coverage', () => {
  for (const path of ['src/app/page.tsx', 'package-lock.json', 'migrations/0006.sql', 'unknown.config', 'tests/e2e/save.spec.ts']) {
    assert.equal(needsFullSuite(['docs/PROJECT_STATE.md', path]), true, path);
  }
});

test('a compiled or executable file retained under docs selects the checks that consume it', () => {
  for (const path of ['docs/evidence/diagnostic/probe.mjs', 'docs/evidence/diagnostic/helper.tsx', 'docs/evidence/diagnostic/reproduce.sh', 'docs/tools/check.py']) {
    assert.equal(isDocumentationPath(path), false, path);
    assert.equal(needsFullSuite([path]), true, path);
  }
});

test('an empty change set selects nothing beyond consistency checks', () => {
  assert.equal(needsFullSuite([]), false);
  assert.equal(needsWorkflowChecks([]), false);
});

test('comparison base follows the event type', () => {
  assert.equal(comparisonBase({ action: 'synchronize', before: 'b'.repeat(40) }, 'pull_request'), 'b'.repeat(40));
  assert.equal(comparisonBase({ action: 'opened', pull_request: { base: { sha: 'c'.repeat(40) } } }, 'pull_request'), 'c'.repeat(40));
  assert.equal(comparisonBase({ before: 'd'.repeat(40) }, 'push'), 'd'.repeat(40));
});
