---
name: issue-driven-workflow
description: Use when a project follows an issue-first workflow and implementation should be tracked through docs/issues before, during, and after coding. Trigger for non-trivial bug fixes, features, refactors, or reliability work.
---

# Issue Driven Workflow

Run non-trivial implementation through an issue document so problem, scope, risks, validation, and next steps stay explicit.

## Default flow

1. Create or update an issue doc before coding.
2. Keep the issue state in sync with actual work.
3. Record affected files and validation commands.
4. After completion, update:
   - `docs/issues/current_backlog.md`
   - `docs/status/implemented_features.md` when real functionality changed
5. Always remind what was just completed and what remains.

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
