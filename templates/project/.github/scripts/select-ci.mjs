import { execFileSync } from 'node:child_process';
import { appendFileSync, readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

// Change-based CI selection. Documentation-only changes get repository consistency checks;
// changes under .github/ get workflow checks; anything else, an unknown path, or an unavailable
// comparison selects the complete suite. Adjust the two lists below for your repository.

// Extensions a real check compiles or executes. A file with one of these retained under docs/
// is still type-checked, linted or run, so it stays on the full path.
const COMPILED_OR_EXECUTABLE = /\.(?:[cm]?[jt]sx?|sh|py)$/;

// Documentation paths that another check consumes as input rather than prose.
const CONSUMED_DOCUMENTATION_PATHS = new Set([
  // 'docs/specs/some-contract.md',
]);

export function isDocumentationPath(path) {
  if (/^(AGENTS|CLAUDE|README)\.md$/.test(path)) return true;
  if (!path.startsWith('docs/')) return false;
  if (CONSUMED_DOCUMENTATION_PATHS.has(path)) return false;
  return !COMPILED_OR_EXECUTABLE.test(path);
}

export function needsFullSuite(paths) {
  return paths.some((path) => !isDocumentationPath(path) && !path.startsWith('.github/'));
}

export function needsWorkflowChecks(paths) {
  return paths.some((path) => path.startsWith('.github/'));
}

export function comparisonBase(event, eventName) {
  if (eventName === 'pull_request') {
    return event.action === 'synchronize' ? event.before : event.pull_request?.base?.sha;
  }
  return event.before;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const event = JSON.parse(readFileSync(process.env.GITHUB_EVENT_PATH, 'utf8'));
  const head = process.env.GITHUB_SHA;
  const base = comparisonBase(event, process.env.GITHUB_EVENT_NAME);
  let full = true;
  let workflow = true;
  let paths = [];
  if (process.env.GITHUB_EVENT_NAME !== 'workflow_dispatch'
      && /^[a-f0-9]{40}$/.test(base ?? '') && !/^0+$/.test(base)
      && /^[a-f0-9]{40}$/.test(head ?? '')) {
    try {
      execFileSync('git', ['merge-base', '--is-ancestor', base, head]);
      paths = execFileSync('git', ['diff', '--name-only', '--no-renames', '-z', base, head], { encoding: 'utf8' }).split('\0').filter(Boolean);
      full = needsFullSuite(paths);
      workflow = needsWorkflowChecks(paths);
    } catch {
      full = true;
      workflow = true;
    }
  }
  const report = { head, base, full, workflow, paths };
  console.log(JSON.stringify(report));
  appendFileSync(process.env.GITHUB_OUTPUT, `full=${full}\n`);
  appendFileSync(process.env.GITHUB_OUTPUT, `workflow=${workflow}\n`);
  appendFileSync(process.env.GITHUB_STEP_SUMMARY, `## Selected verification\n\n\`\`\`json\n${JSON.stringify(report, null, 2)}\n\`\`\`\n\nA documentation-only selection runs consistency checks without installing application dependencies. A light selection does not certify application tests; reused results and their source identity belong in the PR packet.\n`);
}
