---
name: issue-driven-workflow
description: Use when a project follows an issue-first workflow and implementation should be tracked through docs/issues before, during, and after coding. Trigger for non-trivial bug fixes, features, refactors, or reliability work once the problem is already clear enough to execute. Do not use this skill as a substitute for early problem framing or detailed task decomposition when those are still missing.
---

# Issue Driven Workflow

Run non-trivial implementation through an issue document so problem, scope, risks, validation, and next steps stay explicit.

## Default flow

1. If the request is still vague, hand off to `spec-writing` first.
2. Create or update an issue doc before coding.
3. Keep the issue state in sync with actual work.
4. Record affected files, linked docs, and validation commands.
5. After completion, update:
   - `docs/issues/current_backlog.md`
   - `docs/status/implemented_features.md` when real functionality changed
6. Use troubleshooting notes, decision records, and review notes when the work produces reusable evidence beyond the issue itself.
7. Always remind what was just completed and what remains.

## Good fit

- feature work
- bug fixes with more than one file
- reliability or UX cleanup
- refactors with validation requirements

## Avoid for

- tiny spelling fixes
- trivial one-line changes with no real scope

## Resources

- See `references/issue-lifecycle.md` for the recommended issue lifecycle.
- Pair with `spec-writing` when scope is loose and `planning-workflow` when the issue is too large to execute directly.
- Keep the issue doc focused on execution state; move durable rationale to `decision-recording` and mechanism explanations to `technical-learning-note`.
