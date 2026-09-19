# Project Foundry Example — Home Garden Web Application

## Purpose of this example

This is not a finished garden-app specification. It demonstrates how Project Foundry should respond to an unrelated product idea without importing architecture or rules from another project. Read it to learn the *feel* of the process; never import its content into a real project.

### Raw idea

> I want to create a web app that helps people plan and maintain a home garden.

---

# F0 — Idea Intake

`[Foundry F0 · L2 provisional · Gate F0 open · 9 unknowns · Worksheet v1]`

## Current interpretation

A consumer-facing gardening application that helps a home gardener decide what to grow, where and when to plant it, and how to maintain the garden over time.

## Confirmed facts

- It should be a web application.
- It concerns home gardens.
- It should support both planning and ongoing maintenance.

## Working assumptions, not requirements

- Users may need climate/location awareness.
- Plants may need a structured plant database.
- Returning seasonal use may matter.
- Mobile use may be important while physically in the garden.

## Important unknowns

1. Beginner versus expert target user.
2. Personal-only versus public/multi-user product.
3. Geographic scope.
4. Vegetable gardening only versus flowers/herbs/ornamentals.
5. Visual garden-layout planning versus calendar/task management emphasis.
6. Whether weather data is required.
7. Whether photo/AI plant diagnosis is desired.
8. Whether reminders/notifications are central.
9. Whether users track one garden or multiple spaces.

## Provisional classification

Likely Level 2 — Structured Application.

Potential Level 3 if launched as a public subscription product with user accounts, payments, large-scale location/weather data, sharing, and production support obligations.

---

# F1 — First adaptive interview batch

A useful first batch would be:

Three open questions — the budget — each with options, and the rest proposed as assumptions to correct.

1. Who do you most want this to help: complete beginners, experienced gardeners, or both? *(Changes onboarding, plant-data depth, and how much the product explains itself.)*
2. When a user opens the app for the first time, what should they accomplish: design the physical garden, choose plants, generate a planting calendar, or something else? *(Defines the core job, and therefore Phase 0.)*
3. Is this first your personal tool, a public product for many users, or both eventually? *(Sets the level, and with it auth, hosting, and support obligations.)*

Proposed rather than asked — correct me only where I am wrong:

- **A-01** The product uses approximate location and climate zone for season-specific guidance; precise location is not stored. *(Alternatives: the user picks a zone manually; no location at all.)*
- **A-02** Ongoing maintenance covers watering, harvests, and pest/disease observations first; fertilizing, pruning, and succession planting are Enhancement-class. *(Alternative: all of it at once, which pushes M1 much later.)*

Why three and not five: an answer that would only confirm what a sensible default already says is a proposal, not a question. Impact × uncertainty is the test.

---

# Example synthesis after hypothetical answers

Assume the product owner answers the three questions:

- **Q1** target beginners and intermediate home gardeners;
- **Q2** first value is creating a visual garden plan and receiving a personalized planting schedule;
- **Q3** public product eventually, but the first version may be single-user or beta.

And corrects one proposal, which is what propose-then-confirm is for:

- **A-01 confirmed** — approximate location only, used for climate guidance.
- **A-02 corrected** — maintenance must include fertilizing and pruning from the start; the owner says a schedule that omits them is not usable for a real bed. They move from Enhancement to Core, and M1 moves with them.

Volunteered, unasked: vegetable, herb, and common fruit gardening first; ornamental landscaping is not initial scope. That is a non-goal, and it is recorded as one.

The assistant should then synthesize:

`[Foundry F1 · L2 provisional · Gate F1 open · 6 open items · Worksheet v2]`

## Product direction

The product is becoming a **garden planning and seasonal operating system for home food gardens**, not a general landscaping app.

## Likely primary jobs

1. Decide what can successfully grow in the user's conditions.
2. Lay out plants in available beds/containers.
3. Know what to plant and when.
4. Know what needs attention now.
5. Maintain a season-long record of the garden.

## Likely core workflows

### Plan

Create garden → define beds/containers → describe light/location → choose plants → place plants → receive compatibility/spacing information.

### Schedule

Use climate/location + selected plants → generate sow/transplant/harvest windows → allow user adjustment.

### Maintain

Open Today view → see due garden tasks → complete/defer/add observation → garden record updates.

### Review

See plant history, photos/notes, harvests, and season outcomes.

## Candidate feature architecture

### Foundation

- garden/profile model;
- plant knowledge model;
- climate/location model;
- persistent user state;
- responsive application shell.

### Core

- visual bed/container planner;
- plant selection;
- spacing rules;
- planting calendar;
- maintenance task engine;
- garden status/today view;
- observations/journal.

### Enhancements

- weather-aware task adjustments;
- harvest tracking;
- seed inventory;
- reminders;
- garden photos;
- succession planting.

### Advanced backlog

- photo-based plant issue identification;
- private garden copilot;
- companion-planting optimization;
- yield forecasting;
- household/shared garden collaboration.

### Experimental

- soil sensor integrations;
- irrigation hardware control;
- growth computer vision.

### Explicit non-goals for early product

- commercial farm management;
- general landscape architecture;
- plant marketplace;
- social network;
- autonomous irrigation hardware control.

---

# Why the Foundry has not selected technology yet

At this point the project is much clearer, but major architecture questions remain:

- public accounts versus local/private beta;
- how detailed the visual garden canvas must be;
- whether climate guidance requires weather history, forecasts, hardiness-zone data, frost dates, or a combination;
- whether plant knowledge is curated, licensed, imported, or authored;
- notification channel requirements;
- offline/mobile field use.

Selecting a stack before resolving these could create avoidable rework.

---

# Example F4 UX implication

If mobile field use is important, the UX might intentionally have two contexts:

### Desktop/tablet planning workspace

- visual bed layout;
- plant library;
- seasonal timeline;
- comparison/detail panels.

### Mobile garden mode

- Today's tasks;
- quick task completion;
- add observation;
- take photo;
- log harvest;
- plant detail.

This is a product-driven UX decision, not a generic "responsive design" statement.

---

# Example F6 risk review

Even a moderate gardening app has meaningful failure modes:

- location/climate data is wrong or stale;
- planting guidance presents generalized horticultural information as certainty;
- weather API outage silently stops task adjustments;
- user loses a season of garden history;
- photo diagnosis overstates confidence;
- exact home location is unnecessarily retained;
- notification spam causes users to ignore important tasks.

Those concerns are proportionate to the product; they do not require the same controls as a financial execution system.

---

# Example planning-sufficiency behavior

The assistant should continue discovery until product, UX, data, and architecture are coherent.

It should not spend weeks designing AI disease diagnosis before the basic garden-planning and seasonal-maintenance product has even been implemented.

When the core plan passes the Foundry gates, advanced features go to backlog and Phase 0 — the walking skeleton — begins.

This demonstrates the framework's goal: **same disciplined reasoning process, different domain, different risk depth, different architecture.**
