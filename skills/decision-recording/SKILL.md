---
name: decision-recording
description: Use when a repository should capture a high-impact engineering decision in `docs/records` instead of leaving the reasoning in chat history. Trigger for architecture changes, dependency choices, operating-rule changes, or decisions that would be expensive to reverse later.
---

# Decision Recording

Capture the why behind non-trivial engineering choices so later work does not depend on memory.

## Default flow

1. Confirm the decision is real, accepted, and worth keeping.
2. Record the context that forced the decision.
3. List the main options that were considered.
4. Write the chosen direction and its consequences.
5. Link evidence such as issue docs, incidents, experiments, or benchmarks.
6. Prefer `docs/records/` for the note and update the records index when the decision matters beyond one task.

## Good fit

- selecting or removing a dependency
- changing architecture boundaries
- introducing a strong guardrail or operating rule
- choosing a workflow that other contributors must follow

## Avoid for

- obvious implementation details
- temporary experiments that are not yet accepted
- one-off edits with no lasting downstream effect

## Resources

- See `references/decision-checklist.md` for the minimum record contents.
