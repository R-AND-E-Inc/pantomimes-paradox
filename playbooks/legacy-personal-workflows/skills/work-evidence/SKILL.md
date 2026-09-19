---
name: work-evidence
description: "Use when validating completion, preparing a verification packet, or checking whether existing results actually establish acceptance criteria. Works for software, documents, designs, and data artifacts. Skip ceremonial evidence packets for trivial changes."
---

Make each completion claim traceable to evidence about the artifact actually delivered.

1. Obtain the accepted outcome and applicable project verification rules. Extract concrete criteria from the current request or approved plan; do not invent additional requirements. Identify the candidate: Git revision plus relevant uncommitted changes, or exact artifact path/version and modification state. A HEAD hash alone does not identify a dirty working tree.
2. Inspect existing evidence first. Record what was checked, the result, which candidate it concerns, and where the underlying output can be inspected. Distinguish direct observations, reported results, and inference. Never turn a command that was merely suggested into a successful check.
3. Map each criterion to the smallest adequate evidence. Use the relevant installed specialty skill for browser, document rendering, spreadsheets, or provider tooling when applicable. A unit test can establish logic; it may not establish an end-to-end interaction. A screenshot can establish appearance; it may not establish persistence. For external CI, verify the intended revision rather than accepting the latest green run on an unrelated revision.
4. Run missing checks within the user's authorization and available environment. Follow the project's local/CI split; do not repeat a full suite when current authoritative evidence already covers the candidate. After a change, determine which evidence is affected and rerun or invalidate that evidence. Preserve unaffected evidence with the reason it still applies.
5. Report each material criterion as passed, failed, not run, or blocked, with its evidence reference and candidate identity. "Passed" requires observed supporting evidence. Include limitations such as unavailable browsers, unexecuted migrations, or an external run still pending. Never claim completion when a required check is unresolved.

Use a small table only when multiple criteria benefit from comparison:
`Criterion | Candidate | Check / evidence | Result | Limitation`
A packet is a record of evidence, not itself a test. Keep logs local and focused; do not include credentials or unrelated personal data. Save it only when a project workflow or task length makes persistence useful.
