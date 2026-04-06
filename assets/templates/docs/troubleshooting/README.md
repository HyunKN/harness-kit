# Troubleshooting

Use this folder for concrete incidents and resolved failures.

Examples:

- runtime errors
- broken user-facing behavior
- misleading UI states
- regressions
- environment-specific failure modes

## What A Troubleshooting Note Should Capture

1. symptom
2. affected path or feature
3. actual root cause
4. fix
5. validation
6. whether the incident should produce a new strong rule

## Boundary With Other Folders

- `learning/`
  - generalized technical explanation
- `troubleshooting/`
  - concrete incident history
- `operations/strong_rules.md`
  - recurring or non-negotiable prevention rules

## Why This Folder Exists

Many projects lose failure history because incidents stay only in chat or commit diffs.

This folder keeps that history durable enough for another Codex user to reuse.
