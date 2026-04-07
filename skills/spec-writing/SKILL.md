---
name: spec-writing
description: Use when a feature, refactor, or workflow change is still underspecified and a short written spec should exist before issue creation or implementation. Trigger when goals, boundaries, users, or success criteria are still unclear. Do not use only because work spans multiple files; use `planning-workflow` or `issue-driven-workflow` once the problem is already clear enough to execute.
---

# Spec Writing

Write a short working spec before coding when the request is still loose.

This skill is for problem framing, not task tracking.

## Default flow

1. State the problem, affected user or team, and desired outcome.
2. Surface assumptions and unanswered questions early.
3. Write success criteria that can be validated later.
4. Record boundaries:
   - in scope
   - out of scope
   - decisions that still need approval
5. Prefer `docs/product/` for the spec and link it from the issue doc before implementation starts.
6. Stop once the work is clear enough to create an issue and a plan.

## Good fit

- new features with unclear shape
- refactors with behavior constraints
- architecture or workflow changes
- requests that would otherwise rely on chat memory

## Avoid for

- typo fixes
- obvious one-line changes
- follow-up tasks that already have a clear issue doc and plan

## Resources

- See `references/spec-checklist.md` for a lean spec checklist.
- Hand off to `planning-workflow` after the scope is stable and to `issue-driven-workflow` once execution should be tracked.
