---
name: planning-workflow
description: Use when work is already clear enough to execute but still too large to implement safely without a written plan. Trigger for multi-step features, refactors, risky bug fixes, or coordinated agent work that should be broken into bounded tasks with validation checkpoints. Do not use to clarify vague goals; start with `spec-writing` when the request itself is still underspecified.
---

# Planning Workflow

Break a spec or issue into small tasks that another Codex user can execute without re-scoping the problem.

This skill is for implementation sequencing, not initial problem discovery.

## Default flow

1. Read the current issue or spec before changing code.
2. Identify dependencies, risky areas, and blockers.
3. Split the work into small validated steps.
4. Prefer vertical slices over layer-by-layer work when possible.
5. Put acceptance and validation beside each task, not only at the end.
6. Use the issue doc's `Plan` and `Validation` sections unless the plan is large enough to deserve its own note.
7. Stop once the next implementation steps are explicit enough to execute and track in the issue doc.

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
- Pair with `issue-driven-workflow` to keep the plan attached to the real execution record.
