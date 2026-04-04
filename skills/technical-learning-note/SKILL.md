---
name: technical-learning-note
description: Use when a repository keeps technical learning notes and the output should explain implementation mechanisms, key code, and tradeoffs instead of just listing completed features. Trigger after meaningful engineering work or when the user asks for a study-oriented explanation.
---

# Technical Learning Note

Write learning notes that help a future reader understand how something works technically.

## Required qualities

- explain the mechanism, not just the user-visible feature
- mention the key code paths
- describe state, events, processing flow, or rendering flow when relevant
- explain why this approach was chosen
- note tradeoffs and remaining risks

## Reject these patterns

- feature list only
- release-note style summary only
- no file references
- no explanation of why the code works

## Suggested structure

1. problem
2. mechanism
3. key code
4. why this approach
5. alternatives considered
6. remaining risks
7. validation

## Resources

- See `references/note-rubric.md` for the quality bar.
