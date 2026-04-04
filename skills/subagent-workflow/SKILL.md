---
name: subagent-workflow
description: Use when Codex sub-agents should be applied in a disciplined way for analysis, implementation, or review. Trigger when a task is large enough to benefit from role-split work but still needs one main agent to own integration.
---

# Subagent Workflow

Use sub-agents only when work naturally divides into roles and the main agent can still integrate the result safely.

## Good candidates

- analysis -> implementation -> review
- documentation research -> design proposal -> implementation
- large refactors with clearly separated file ownership

## Avoid for

- one small fix
- overlapping write scopes
- unresolved product direction

## Standard roles

### Analysis

- locate causes
- list affected files
- identify risks

### Implementation

- change only approved files
- report validation done

### Review

- look for regressions
- identify missing tests

## Guardrails

1. The main agent decides the plan first.
2. Do not let two sub-agents edit the same files.
3. The main agent integrates and validates.
4. Use sub-agents sparingly; speed matters only when coordination overhead stays low.

## Resources

- See `references/subagent-patterns.md` for recommended split patterns.
