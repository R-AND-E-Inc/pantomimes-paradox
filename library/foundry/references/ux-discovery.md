# UX and Design Discovery — F4 playbook

Read once when F4 opens. Goal: define the intended experience before implementation turns backend structure into the interface.

## Context before colors

Establish first: where the user physically is; device; how much attention they have; frequency of use; beginner vs expert behavior; the most common task; the most consequential task; what must be visible together; what should stay hidden until needed.

## Four journeys per major user type

1. **First use** — how they reach first value.
2. **Returning routine** — what they do repeatedly.
3. **High-consequence** — the action needing the clearest confirmation, context, auditability.
4. **Recovery** — what happens when something fails, is missing, or is wrong.

## Information architecture

Primary and secondary navigation; object hierarchy; global search / command palette if useful; breadcrumbs/history; the dashboard's actual purpose; where settings and help live. Navigation follows user jobs, never database tables.

## Screen specification

For each major screen: purpose; primary action; primary and secondary information; empty, loading, error/degraded, stale-data, and permission states; desktop/mobile behavior; accessibility notes; provenance/explanation needs.

## Design language

Emotional tone; visual references; color and typography roles; density; border/elevation philosophy; motion; iconography and imagery; chart/table conventions; semantic status colors. "Premium" means clarity, precision, consistency, speed, and confident detail — not decoration.

## Responsive strategy — choose deliberately

- **Responsive equivalent** — same tasks, rearranged.
- **Mobile-priority subset** — mobile for field/quick actions, desktop for deep work.
- **Separate interaction model** — only when device context changes the job.

Do not build native unless responsive web fails a real requirement.

## Data-rich interfaces

Default view; sort/filter; hover/tap detail; zoom/pan; comparison; synchronized cursors; time range; missing/stale representation; uncertainty; export/drilldown; accessible text equivalents.

## Trust UX (analytical, AI, financial, health, operational systems)

Show source/provenance, freshness, assumptions, confidence, observed-vs-modeled, warnings/degraded state, audit history. **Unknown and stale must look different from zero and healthy.**

## AI UX

Distinguish generated explanation from authoritative data; link claims to sources/tool outputs; show uncertainty when material; allow correction; make side-effect actions explicit; never let fluency read as certainty.

## Accessibility baseline

Keyboard navigation, focus states, screen-reader semantics, contrast, reduced motion, touch targets, non-color status cues, chart alternatives, form labels/errors, responsive text. Scale formal testing to level and audience.

## Human preview gate (for visible phases)

A short checklist of what automation cannot judge: hierarchy, readability, interaction feel, responsive behavior, important edge states, design intent. Never ask the user to re-run automated checks by hand.
