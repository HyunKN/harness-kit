---
name: troubleshooting-workflow
description: Use when a concrete failure, regression, or confusing broken state must be debugged systematically and captured in `docs/troubleshooting`. Trigger for failing tests, broken builds, runtime errors, user-reported incidents, or environment-specific failures.
---

# Troubleshooting Workflow

Treat failures as reusable incident history, not just something fixed in passing.

## Default flow

1. Stop adding unrelated work until the failure is understood.
2. Preserve the symptom, reproduction steps, and affected paths.
3. Narrow the fault before applying a fix.
4. Record the actual root cause, not only the visible symptom.
5. Validate the fix and note what proved it.
6. Add a troubleshooting note in `docs/troubleshooting/` when the incident would help another Codex user.
7. Decide whether the incident should also create a guardrail or decision record.

## Good fit

- broken user-facing behavior
- failing tests or builds
- regressions after a recent change
- bugs that required more than one guess to understand

## Avoid for

- already-understood failures with no reusable learning
- speculative cleanup not tied to a concrete incident

## Resources

- See `references/incident-checklist.md` for the core incident fields.
