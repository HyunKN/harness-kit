# Guardrails

Use this document for rules that should be read before coding in risky or historically fragile areas.

These are not just “good ideas”.
They are preventive guardrails intended to stop repeated mistakes, ignored user preferences, or expensive regressions before they happen again.

## What Belongs Here

- explicit user constraints
- forbidden implementation patterns
- required technology choices
- required validation gates
- rules promoted from repeated incidents

## What Does Not Belong Here

- general advice
- broad architecture background
- study-oriented technical explanation
- one-off bug details without reusable policy value

Those belong in:

- `learning/` for generalized technical understanding
- `troubleshooting/` for concrete incidents
- `issues/` for in-progress scoped work

## Promotion Criteria

Promote something into a guardrail when at least one of these is true:

1. The user explicitly said “do not do this again”.
2. A mistake repeated.
3. The cost of repeating the mistake is high enough that prevention should be explicit.
4. A preferred technique or banned technique should override agent improvisation.

## Suggested Guardrail Shape

For each guardrail, include:

1. the rule
2. why it exists
3. what to do instead
4. how to validate compliance

## Example Guardrail Format

```md
## Rule: Do not duplicate fallback logic

Why:
- Display names diverged across screens and caused inconsistent UI behavior.

Do instead:
- Use the shared helper for display-name resolution.

Validation:
- Search for duplicated fallback chains before finishing the task.
```

## Rule: Do not default to single-agent serial work for non-trivial tasks

Why:
- Complex work is safer and faster when analysis, implementation, review, verification, and docs are split by role.
- Keeping everything in one agent by habit makes it easier to miss evidence, regressions, and completion gaps.

Do instead:
- Prefer the lightest execution mode that preserves quality:
  - local first
  - then bounded delegation
  - then multi-agent team composition when parallel lanes materially improve speed, safety, or coverage
- Default to a small specialist agent team only after scope, affected paths, and validation are clear enough that the split will reduce risk instead of creating guesswork.
- Keep ownership explicit:
  - main agent for planning, integration, and final judgment
  - analysis / research agent for evidence and file mapping
  - implementation agent for bounded code changes
  - review / verification agent for read-only regression and completion checks
  - writer / ops agent when docs or run procedures change
- Parallelize only when write scopes do not overlap and the lanes are behaviorally independent or joined by an agreed interface.
- Delegation does not widen authority. Protected paths, human-approved-only files, and issue-level scope locks still apply to every sub-agent.

Validation:
- Before doing substantial work, state the role split or explicitly justify why the task stays local.
- After delegated work, confirm who changed what, what stayed read-only, and what validation was performed.

## Manual / Automatic Boundary

This document can guide Codex behavior because `AGENTS.md` can tell the agent to read it first.

But this document alone does not enforce compliance automatically.

If a repository wants automatic enforcement, it should add:

- scripts
- lint rules
- CI checks
- static analysis

in addition to this document.
