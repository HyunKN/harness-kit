---
name: planning-workflow
description: Use when work is clear enough to start but still too large to implement safely without a written plan. Trigger for multi-step features, refactors, risky bug fixes, or coordinated agent work that should be broken into bounded tasks with validation checkpoints.
---

# Planning Workflow

Break a spec or issue into small tasks that another Codex user can execute without re-scoping the problem.

## Default flow

1. Read the current issue or spec before changing code.
2. Identify dependencies, risky areas, and blockers.
3. Split the work into small validated steps.
4. Prefer vertical slices over layer-by-layer work when possible.
5. Put acceptance and validation beside each task, not only at the end.
6. Use the issue doc's `Plan` and `Validation` sections unless the plan is large enough to deserve its own note.

## Good fit

- features that touch multiple files
- work that will span more than one session
- tasks that may involve sub-agents
- fixes where implementation order matters

## Avoid for

- tiny edits with obvious scope
- tasks where the issue doc already has a solid task list

## Resources

- See `references/plan-checklist.md` for a short planning rubric.
