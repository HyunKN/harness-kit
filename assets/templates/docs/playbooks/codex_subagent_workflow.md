# Codex Sub-Agent Workflow

## Purpose

Use sub-agents only when the task naturally splits into separate roles and the work will actually go faster or become safer.

Stay local first until scope, affected paths, and validation are clear enough that delegation will reduce risk instead of creating guesswork.

Different files do not automatically make parallelism safe. Split work only when the lanes are behaviorally independent or joined by an agreed interface.

## Default progression

1. local first
2. bounded delegation
3. small role-based team composition when parallel lanes materially improve speed, safety, or coverage

## Good candidates

- issue analysis -> implementation -> independent review
- document research -> design proposal -> implementation
- multi-file changes with clear write ownership and agreed integration points
- implementation plus independent regression review
- implementation plus separate docs, notes, or run-procedure updates

## Avoid for

- one-file trivial fixes
- tasks with overlapping write scope
- work where direction is still undefined
- lanes that depend on continuous back-and-forth local reasoning
- changes in different files that still share risky behavior or a tight dependency chain

## Roles

### Main agent

- owns the plan and routing
- decides whether delegation is justified
- assigns write ownership and review boundaries
- integrates results
- performs final verification

### Analysis agent

- identify root cause
- list affected files
- note key risks
- gather evidence for the main agent

### Implementation agent

- change only the approved files
- report exact changes
- report validation run inside the assigned scope

### Review / verification agent

- stay read-only and independent
- inspect regression risk
- identify missing tests
- flag structural concerns
- check evidence and completion claims

### Writer / ops agent when relevant

- update docs, notes, playbooks, or run procedures

## Guardrails

1. Prefer the lightest execution mode that preserves quality: local first, then bounded delegation, then role-based team composition.
2. Different files do not automatically make parallel work safe. Check dependency chains, shared behavior, and integration points first.
3. Keep write scopes separate and keep review / verification read-only.
4. Delegation does not widen authority. Protected paths and approval-only boundaries still apply.
5. Do not approve a new direction implicitly during implementation; route that decision back through the main agent.
6. The main agent owns final integration, final judgment, and final verification.
7. Record who changed what, what stayed read-only, and what validation was performed.
