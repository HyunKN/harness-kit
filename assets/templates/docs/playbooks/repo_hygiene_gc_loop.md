# Repo Hygiene And Garbage Collection Loop

This playbook defines a documentation-first cleanup and drift review loop.

It is called a “garbage collection loop” in the practical sense:

- stale docs
- outdated rules
- duplicated guidance
- unused code candidates
- drift between docs and implementation

should be reviewed regularly instead of accumulating silently.

## Important Constraint

Markdown can define this loop, but Markdown cannot automatically enforce it.

Use this playbook to drive repeatable reviews.
If full automation is needed, add code, scripts, CI, or static analysis in the target repository.

## When To Run It

Run this loop:

- after a large refactor
- before a release
- after several fast iteration cycles
- when repeated bugs suggest drift between docs and code
- when onboarding a new AI workflow or new agent behavior

## Review Areas

### 1. Doc-Code Drift

Check whether:

- `docs/status` still matches the real implementation
- issue docs still reflect the current scope
- architecture docs describe current module boundaries
- `AGENTS.md` rules still match the real workflow

### 2. Rule Violations

Check whether the repository has started to violate its own rules:

- files edited without issue tracking
- meaningful changes without validation notes
- failures that were fixed but never captured as troubleshooting notes
- handoff-sensitive work with no durable record

### 3. Dead Or Unused Material

Check for:

- unused files
- dead helper functions
- stale exported utilities
- old screenshots or mock artifacts
- duplicate documents that now describe the same thing

### 4. Repeated Failure Patterns

Look for:

- the same bug category appearing again
- the same validation gap recurring
- the same naming or state-management mistake repeating

If repetition appears, create or update a learning note or playbook instead of fixing the symptom only.
If the pattern is concrete and recurrence-sensitive, add or update:

- a troubleshooting note
- a strong rule
- and then a learning note only if the mechanism itself is worth studying

## Suggested Output

At the end of a hygiene pass, leave behind:

1. a short issue or review note
2. a list of confirmed cleanup tasks
3. a list of “suspicious but not yet proven” items
4. the next highest-value cleanup step

## Manual / Semi-Automatic / Automatic

Use these labels when describing a cleanup loop in a real repository:

- `Manual`
  - human or agent reads docs and code and decides
- `Semi-automatic`
  - scripts/checklists help, but a person still judges the result
- `Automatic`
  - CI, linters, or scripts can fail the check without human interpretation

This distinction matters.  
Do not call a loop automatic if it is only documented.
