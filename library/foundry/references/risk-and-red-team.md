# Risk Review (F6) and Red-Team Review (F8)

Read once when F6 opens; re-read Part B when F8 opens. Depth scales to level: L1 does not need enterprise IAM; L4 may not rely on "it's on a private network" as its identity model. Security derives from assets, adversaries, actions, and consequences.

---

## Part A — Risk and failure-mode discovery (F6)

### Assets × failure modes

List what must be protected (user data, secrets, money, identity, private content, IP, location, health/safety info, irreplaceable history, automated actions, infrastructure, trust). For each, ask what happens if it is: exposed · corrupted · deleted · stale · unavailable · manipulated · acted on twice · acted on by the wrong person · misinterpreted by AI · lost because a vendor fails.

### Domains — review those that apply

- **Identity** — is auth needed; session creation/revocation; role vs object authorization; reauth for sensitive ops; account recovery.
- **Secrets** — where keys live; log redaction; can secrets reach source control; can test/demo reach production credentials.
- **Data integrity** — which records are authoritative; transactional writes; is destructive mutation necessary; idempotent imports; duplicates; reconstructable history.
- **Privacy** — minimization; what leaves the user's environment; what is logged; what enters AI prompts; retention/deletion.
- **Providers** — API change, pricing change, tightened limits, outage, replaceability; are external facts versioned and dated.
- **Supply chain** — lockfiles, vulnerability scanning, dependency review, automated updates, minimal CI permissions, pinned CI actions, pruning abandoned deps.
- **Availability/operations** — what must stay up; what can wait; what is monitored; degraded mode; which alerts are actionable.
- **Backup/recovery** — what is irreplaceable; where backups live; encrypted; restore tested; full rebuild after provider loss.
- **Concurrency/idempotency** — dedupe keys, idempotency keys, locking/transactions, retry semantics, reconciliation.
- **AI/ML** — hallucination, prompt injection, untrusted retrieved content, eval drift, bias where relevant, unsafe tool invocation, probabilistic output mistaken for truth, provider outage, data leakage to providers.

### Risk register entry

ID · statement · cause · consequence · likelihood (qualitative is more honest than invented numbers) · severity · control · detection · residual risk · owner/phase · status.

### Gate

Every material risk has a control, explicit acceptance, a scheduled research item, or a phase-scoped mitigation. For L3–L4 explicitly examine irreversible actions, sensitive data, mode/environment confusion, supply chain, backup/recovery, auditability, silent stale/corrupt data.

---

## Part B — Red-team review (F8)

Runs after product, architecture, UX, risks, and development program exist, before `PLANNING SUFFICIENT`. Use a fresh context where possible (see `prompts.md`). Assume the plan contains elegant-sounding mistakes. Do not optimize for agreement.

**Run the cross-document audit first** (`document-package.md`). It is the mechanical pass — coverage, duplication, ambiguity, invariant conflicts — and clearing it means the red team spends its attention on judgment rather than bookkeeping. A red team that reports missing IDs and stale cross-references was handed unfinished documents.

### Required challenges

- **Product** — is the problem real and stated concretely; are workflows better than the status quo; features without a user job; incompatible audiences; are non-goals strong enough?
- **Scope** — what to remove; what is built too early; what can stay manual; what advanced capability is holding the core hostage?
- **UX** — home screen trying to show everything; navigation mirrors tables; mobile/desktop confused; empty/error/stale/loading/degraded states unspecified; can the user see confidence and provenance?
- **Architecture** — needless distribution; over-coupled provider; two sources of truth; a current vendor fact frozen in; AI for a deterministic problem; conversational logic replacing a deterministic engine?
- **Security/privacy** — easiest path to sensitive data; after credential/device compromise; are demo/test isolated; can real data leak into logs, prompts, CI, screenshots, repos?
- **Reliability** — which failures look healthy; what goes stale silently; retry behavior; duplicate side effects; can recovery actually be performed?
- **Verification** — claims with no objective oracle; tests of implementation details instead of outcomes; CI evidence tied to the exact candidate; waived vs passed distinguishable?
- **Operations** — who learns it is broken; maintenance cost; which external service can surprise the owner; is observability proportionate?
- **Opportunity** (the red team is not only negative) — what feasible feature would dramatically raise value; what collected data could unlock insight; what could be automated later; what foundation is cheap now and expensive to retrofit?

### Finding format and disposition

Each material finding: severity · evidence/rationale · impact · recommended disposition. When severity is genuinely uncertain, choose the lower one; inflation costs credibility that the next real finding needs. Disposition is one of **ACCEPT** (incorporate now) · **BACKLOG** · **REJECT** (with rationale) · **RESEARCH** (cannot decide without evidence) · **ACCEPT-RISK** (downside consciously retained). Separate pre-implementation blockers from backlog ideas. Never discard a finding silently.

### Gate

No unresolved finding can materially invalidate the product contract, architecture foundation, security model, or development sequence.
