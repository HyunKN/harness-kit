# Codex Sub-Agent Workflow

## Purpose

Use sub-agents only when the task naturally splits into separate roles and the work will actually go faster or become safer.

## Good candidates

- issue analysis -> implementation -> review
- document research -> design proposal -> implementation
- implementation plus independent regression review

## Avoid for

- one-file trivial fixes
- tasks with overlapping write scope
- work where direction is still undefined

## Roles

### Analysis agent

- identify root cause
- list affected files
- note key risks

### Implementation agent

- change only the approved files
- report what changed
- report validation run

### Review agent

- inspect regression risk
- identify missing tests
- flag structural concerns

## Guardrails

1. Keep write scopes separate.
2. The main agent owns final integration.
3. Do not approve a new direction implicitly during implementation.
4. Always validate after integration.
