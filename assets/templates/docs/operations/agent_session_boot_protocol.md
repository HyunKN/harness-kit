# Agent Session Boot Protocol

This document defines what Codex should read first when entering a repository that uses the harness.

## Purpose

The goal is to reduce random starts, hidden assumptions, and context loss.

Instead of jumping straight into code, the agent should begin from the project's operating documents.

## Recommended Read Order

1. `AGENTS.md`
2. `docs/README.md`
3. `docs/issues/current_backlog.md`
4. the issue document directly related to the current task
5. the most relevant architecture / operations / playbook document for the task

## Minimum Questions To Answer Before Coding

Before implementation starts, Codex should be able to answer:

1. What problem is being solved?
2. Which document currently owns this problem?
3. What should be changed?
4. What should not be changed?
5. What validation will be used afterward?

If these answers are not clear, the task should not be treated as “ready for implementation”.

## Do / Don't Pattern

### Do

- Start from the repo's operating documents
- Use the issue doc as the current source of scope
- Re-check validation expectations before editing files
- Prefer updating existing docs over creating near-duplicates

### Don't

- Do not start from chat memory alone
- Do not assume old context is still correct without checking docs
- Do not change unrelated files just because they are nearby
- Do not finish coding without updating the relevant issue or learning note

## What This Document Enables

This protocol gives the repository a repeatable “session start” behavior.

It does not fully automate reading by itself, but it makes the expected entry path explicit so another Codex user can follow the same boot sequence.
