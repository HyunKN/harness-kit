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

## Manual / Automatic Boundary

This document can guide Codex behavior because `AGENTS.md` can tell the agent to read it first.

But this document alone does not enforce compliance automatically.

If a repository wants automatic enforcement, it should add:

- scripts
- lint rules
- CI checks
- static analysis

in addition to this document.
