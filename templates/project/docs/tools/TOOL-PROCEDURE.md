# <Tool>: procedure

## Authority

Follow the current owner request, the repository's root instructions, and the workflow profile in `docs/OPERATING.md`. Those outrank this file. This file describes an optional tool procedure and **grants no authority of its own**: not to install or update packages, edit application source or build configuration, start or stop processes, write credentials, or send anything outside this machine. Where a step below needs one of those, prepare the exact bounded change and its effect and obtain the applicable authorization first.

A missing tool is a **disclosed capability gap**, not a task to fix by installing something. Do not substitute another workflow for it, and do not treat a stop condition as an obstacle to work around.

## Before acting

Inspect the existing configuration: <config files, package entries, wiring>. Steps written for a fresh install usually do not apply to a project where the tool is already wired in.

## Procedure

1. <check that the tool is reachable; what a healthy state looks like>
2. <the bounded action, with what it proves and what it does not>
3. <how to read the result; which outputs are evidence and which are noise>

## Guards

1. Never run two instances at once.
2. Never guess a command; take it from the project's own scripts or say so and stop.
3. Never start, stop or kill a process you do not own.
4. The permission prompt belongs to the host; never bypass or auto-approve it.

## Report

- What you did, step by step, and what each step produced.
- Anything broken, with the location the tool gave you.
- What could not be verified, stated plainly. "Unknown" is a real answer; a green verdict you cannot back is not.

## Credentials and external transmission

Do not handle credential values; ask the owner to place them in the ignored environment file themselves. Sending anything outside this machine (feedback, issue reports, telemetry) requires the owner's explicit authorization for that specific transmission.
