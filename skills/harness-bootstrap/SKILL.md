---
name: harness-bootstrap
description: Use when a repository needs the reusable docs harness installed or refreshed. Trigger when the user wants issue tracking docs, learning-note templates, playbooks, or role-based documentation folders added to a new or existing Codex project.
---

# Harness Bootstrap

Install the reusable docs harness into a target repository and leave the repository ready for issue-first, explainable Codex work.

## When to use it

- a repo has no docs harness yet
- a repo wants `docs/issues`, `docs/learning`, `docs/playbooks`, and related templates
- a repo wants a reusable bootstrap instead of copying docs by hand

## Workflow

1. Confirm the target repository path.
2. Run `scripts/init_harness.py <target-repo>`.
3. Review created files and skipped files.
4. If the repo already had conflicting docs, decide whether `--force` is appropriate.
5. Adjust project-specific text after bootstrap instead of editing templates directly.

## Notes

- The bootstrap script copies templates only; it does not modify code.
- Existing files are preserved unless `--force` is used.
- After bootstrap, encourage the user to create the first issue doc before larger implementation work.

## Resources

- See `references/bootstrap-checklist.md` for a short post-install checklist.
