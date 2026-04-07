---
name: review-workflow
description: Use when a change should receive a structured review before merge, handoff, or closure and the findings should be captured in `docs/reviews` or the issue doc. Trigger for non-trivial code changes, architecture changes, risky bug fixes, or external-tool evaluations. This skill defines review content and findings, not whether sub-agents should be used to perform the review.
---

# Review Workflow

Run meaningful changes through a repeatable review instead of relying on scattered comments.

## Default flow

1. Confirm what changed and why it was done.
2. Read validation evidence before commenting on style.
3. Check:
   - correctness
   - readability
   - boundary fit
   - operational risk
   - follow-up work
4. Separate blockers from suggestions.
5. Record the result where the next contributor will see it:
   - issue doc for small reviews
   - `docs/reviews/` for broader analysis or reusable findings

## Good fit

- multi-file implementation work
- high-risk fixes
- architecture or tooling changes
- external package or service evaluation

## Avoid for

- obvious typo fixes
- tiny changes with no real behavioral risk

## Resources

- See `references/review-lenses.md` for a short review checklist.
- Use `subagent-workflow` only if the review should be delegated or split across roles.
