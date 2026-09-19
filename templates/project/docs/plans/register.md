# <Program> — slice register

**CURRENT STEP: <n> OF 7 — <one line on the active card and its gate>.**

**Last accepted slice:** <card id and link to its packet>. **Active card:** <id>, authorized <date>. **Next planned cards:** <ids>.

## How to read and maintain this register

This file alone owns slice status, the active card and the accepted source and evidence pointers. Cards (`cards.md`) own implementation scope; the contract owns acceptance IDs; review records own findings. Do not copy mutable status into cards.

State flow: `PLANNED → IN PROGRESS → EVIDENCE REVIEW → OWNER CHECK (when applicable) → ACCEPTED`; `BLOCKED` records a specific unresolved prerequisite. At most one implementation card is IN PROGRESS. Evidence vocabulary stays PASS / FAIL / BLOCKED / WAIVED / NOT APPLICABLE.

Each accepted row records the exact source commit, the evidence packet link, the applicable CI run, the immutable preview identity when one was used, the owner's judgment where needed, and limitations. Nothing here implies automatic progression: a card starts only when the owner names it.

## Ordered queue

| Slice / outcome | Findings | Risk / hours | Hard dependencies | Status | Accepted source / evidence |
| --- | --- | --- | --- | --- | --- |
| [S-01 — <outcome>](cards.md#s-01) | | | Plan approval | PLANNED | |
| [S-02 — <outcome>](cards.md#s-02) | | | S-01 | PLANNED | |
