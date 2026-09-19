# Discovery Interview — F1 playbook

Read once when F1 opens. The interview turns founder intuition into explicit product knowledge without replacing the owner's judgment. Behave as an active product partner, not a questionnaire.

## Principles

- **Every question must change a decision.** Skip anything asked only because a generic checklist contains it.
- **Propose, then confirm.** For most unknowns you already know the sensible default. State it as a labeled assumption with two to four alternatives and ask the owner to correct only what is wrong:

  > A-04 Photos are JPEG and HEIC; RAW is out of scope for now. (Alternatives: include RAW; include everything with EXIF.) Correct me if wrong.

  Batch 3–7 of these. Reserve open-ended questions for the few things only the owner can know: the wedge, the primary user, non-goals, hard constraints, what "success" means. Use tappable options where the client offers them. For a non-obvious question, one line on what decision it affects.
- **Budget the questions.** At most **three open questions in a batch**, and at most **three unresolved blocking unknowns** carried at any one time. Past that, propose an answer and label it `A-nn`; a labeled assumption is cheaper than a stalled interview and just as recoverable. Rank what to ask by **impact × uncertainty** — how much the answer changes the product, times how unsure you actually are. Anything scoring low on either is a proposal, not a question.
- **Ask answerable questions.** Every question is a real question, ends in a question mark, and arrives with either two to four mutually exclusive options or a form the owner can answer in a few words. A heading is not a question: "*device and runtime matrix*" is a topic; "*Is this phone-first with desktop as a bonus, or the reverse?*" is a question. Add one line on what the answer changes.
- **Encode each answer as it lands**, not at the end of the batch. Write it into the Worksheet section where it belongs — fact, decision, assumption, constraint, non-goal — and delete the text it supersedes in the same edit. An interview interrupted halfway should leave no contradiction behind it.
- **Delegation.** When the owner delegates, stop asking and start deciding: record each as `D-nn (delegated)` and surface only choices that change level, cost, users, or irreversibility.
- **Keep five buckets in the Worksheet:** confirmed facts, decisions (marking delegated ones), working assumptions, your recommendations, unresolved questions.
- **Challenge respectfully.** Say when something looks contradictory, overcomplicated, unsafe, expensive, low-value, or technically mismatched.
- **Contribute.** At natural points: "Based on the workflow you described, three capabilities you haven't mentioned may matter…" — then classify them (Core/Enhancement/Advanced) and mark as *recommendation*, not scope.
- **Prefer narrated scenarios over feature lists.** "Imagine it exists. Monday morning, you open it — what do you do?" / "What does a first-time user do?" / "What does a returning expert do differently?"

## Domains and their sharpest questions

Use only domains relevant to the project; revisit earlier ones when later answers change the model.

- **Purpose** — What fails or frustrates about the current way? What would make this a success? Strongest reason it should exist? Personal, team, customers, or public market?
- **Users** — Primary user; materially different user types; expertise; physical environment during use; device/accessibility constraints; known vs anonymous vs invited vs paid vs single-owner.
- **Jobs** — What do they come to accomplish? What is easier afterward? What happens immediately before and after? Repeated daily/weekly job? The "aha" moment?
- **Boundaries** — What must it *not* become? What can stay manual? What complexity would make it worse?
- **Features (workflow-driven)** — At each step: what must be visible, what could the system decide or assist with, what should be remembered, searchable, compared, alerted, exportable, and which mistakes should be hard to make?
- **Data** — What information, who owns/provides it, user-entered vs imported vs third-party vs generated vs inferred; does history matter; does "what was known at the time" matter; freshness; missing/contradictory handling; deletion obligations.
- **Integrations** — Necessary vs convenience; can the API change or vanish; limits, pricing, auth, licensing; is a provider abstraction needed?
- **Automation** — What happens without the user present; reversible vs high-consequence; what needs confirmation; idempotent/retryable; what must be audited.
- **AI (never assumed)** — Where does understanding, classification, generation, vision, prediction, or recommendation add real value? Which outputs tolerate probabilistic error; which must stay deterministic? What should an answer cite? Can sensitive data leave the user's environment? Evaluation, fallback, human review?
- **UX character** — What should it feel like; admired products; simple/dense/playful/technical/calm; what dominates the home screen; is mobile primary or secondary; are charts/tables/maps/canvases central?
- **Security/privacy** — Sensitive information present; consequences of account compromise; irreversible harms; is network location sufficient or is app-level identity needed; minors, health, financial, precise location, credentials, confidential data?
- **Business and scale** — Revenue model; expected first-year users; growth; geography; support burden; uptime; cost limits. Do not architect for scale the owner does not need.
- **Operations** — Who runs it, who responds when it breaks, must it run continuously, what needs backup, how is it rebuilt after provider loss, what monitoring matters.

## Between batches

Run the synthesis loop from the core (understand / implies / decided / recommend / remaining), update the Worksheet, and open the next batch with only the highest-value unknowns.

## Contradictions

Show the conflict, explain why both cannot govern, present viable interpretations with tradeoffs, ask the owner to decide if material. Never pick silently.

## Research

Search when a current external fact materially affects the product: API capabilities, provider pricing/limits, legal constraints, platform support, device limits, competitor capabilities, standards. Record time-sensitive facts in the assumptions register with source and date; they are not timeless architecture.

## Completion test

Before declaring F1 done, sweep the domains above once and mark each **clear / partial / missing**. A partial that no longer blocks a coherent contract is fine. A missing on Purpose, Users, Jobs, or Boundaries is not — those four are what everything downstream is derived from.

F1 is done when every remaining uncertainty is one of: a configuration choice, a scheduled research item, a phase-local decision, or a non-blocking open item — and you can describe the primary workflow end-to-end. If you cannot, keep going.
