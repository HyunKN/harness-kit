# AGENTS.md

This repository is a reusable documentation-first harness for Codex projects.

If you are working in this repository, treat this file as the first operating document to read before changing anything else.

## What This Repository Is

- A reusable workflow kit for Codex-based development
- A documentation harness that can be copied into other repositories
- A source of operating rules, issue-first workflow, learning-note rules, and repo hygiene loops

## What This Repository Is Not

- Not a build framework
- Not a runtime package manager
- Not an automatic enforcement engine by itself

This repository mainly defines the workflow in Markdown.  
If a team wants real automatic enforcement, they must add code, scripts, CI, or lint rules in the target repository.

## Read Order

When starting work here, use this order:

1. `AGENTS.md`
2. `README.md`
3. `README.ko.md` when Korean context matters
4. `assets/templates/docs/README.md`
5. `assets/templates/docs/operations/agent_session_boot_protocol.md`
6. `assets/templates/docs/operations/strong_rules.md`
7. `assets/templates/docs/troubleshooting/README.md`
8. `assets/templates/docs/playbooks/repo_hygiene_gc_loop.md`

Then open only the specific template or README that matches the task.

## Default Working Rules

### Do

- Keep this repository Markdown-first
- Prefer reusable operating guidance over one-off chat-only advice
- Write documents so another Codex user can apply them without project-specific context
- Explain where work is automatic, semi-automatic, or manual
- When adding a new rule, say who follows it, when it runs, and how it is validated

### Don't

- Do not add code here unless the user explicitly changes the repository scope
- Do not assume every repository has the same stack, folder layout, or CI setup
- Do not promise automatic enforcement if the mechanism is only documented
- Do not mix project-specific product rules into generic harness documents

## Core Operating Model

This repository supports four layers:

1. `Session boot`
   - What Codex should read first
   - What should be checked before implementation

2. `Strong rules`
   - What must not be repeated
   - Which implementation patterns are non-negotiable

3. `Troubleshooting`
   - How to record mistakes, regressions, symptoms, and fixes
   - How to leave behind incident history that another agent can reuse

4. `Repo hygiene / garbage collection loop`
   - How to review drift between docs and code
   - How to inspect rule violations, dead code, stale docs, and unused assets

## Strong Rule Boundary

Use `learning` for generalized technical understanding.

Use `troubleshooting` for concrete incidents:

- user-reported breakage
- regression symptoms
- runtime errors
- confusing or misleading UX states

Use `strong rules` when either of these is true:

- the user explicitly says “do not do this again”
- a mistake has already repeated or is expensive enough that repetition is unacceptable

## Important Constraint

Markdown can define the loop, but Markdown cannot enforce the loop alone.

That means:

- `AGENTS.md` can tell Codex what to read first
- playbooks can define repeatable review steps
- issue docs can capture findings

But fully automatic checks such as:

- dead code detection
- drift checks
- lint enforcement
- unused file scanning
- failing build gates

need executable tooling in the target repository.

## Goal of Changes Here

Any new document added to this repository should help another project answer:

- What should Codex read first?
- What should be documented before coding?
- How are failures recorded?
- How do we detect drift and cleanup needs?
- Which parts are manual vs automatic?
