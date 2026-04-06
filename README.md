# Harness Kit

[한국어](./README.ko.md)

Harness Kit is a reusable Codex workflow layer for repositories that want a clean operating system around implementation work.

It gives you:

- issue-first execution
- a role-based `docs/` structure
- a repo-local `AGENTS.md` entrypoint pattern
- technical learning notes that explain how something was built
- a failure / troubleshooting capture loop
- a repo hygiene and garbage collection review loop
- reusable Codex skills for bootstrap, issue workflow, learning notes, and sub-agent usage

## Why use it

Most repos have code, but no consistent way to run work.

Harness Kit adds a lightweight workflow on top of any project so you can:

- start new work with an issue doc instead of ad hoc notes
- keep decisions, learning notes, and backlog in predictable places
- make Codex usage more repeatable across projects
- hand off work without losing context

## Quick Start

Clone the repo:

```powershell
git clone https://github.com/HyunKN/harness-kit.git
cd harness-kit
```

Bootstrap a target repository:

```powershell
python .\scripts\init_harness.py "C:\path\to\target-repo"
```

Create the first issue:

```powershell
python .\scripts\new_issue.py "C:\path\to\target-repo" renderall-partial-refresh "Reduce full rerenders"
```

After that, open the target repository in Codex and use the installed docs structure and skills as your default workflow.

If you are already inside Codex, just hand it off to Codex!

Recommended prompts:

- `Install harness-kit into this repository.`
- `Install https://github.com/HyunKN/harness-kit into this repository and set it up for me.`
- `Create a new issue doc for this repository. Title: Reduce full rerenders.`

## Core Flow

1. Bootstrap a repository with the standard `docs/` harness.
2. Open a new issue before implementation starts.
3. Implement against that issue instead of working from chat history alone.
4. Capture technical learning notes for anything worth reusing or studying later.
5. Use sub-agents only for bounded analysis, implementation, or review tasks.
6. Run a repeatable hygiene pass so drift, stale docs, and dead material do not silently accumulate.

## What You Get

### 1. Reusable docs structure

The bootstrap script installs a pre-organized `docs/` tree with sections for:

- architecture
- product
- design
- reviews
- status
- issues
- records
- learning
- playbooks
- operations

It can also be paired with a repo-local `AGENTS.md` so Codex has a clear “read this first” project entrypoint.

### 2. Codex skills

Included skills:

- `harness-bootstrap`
- `issue-driven-workflow`
- `technical-learning-note`
- `subagent-workflow`

These are designed to make the workflow reusable across projects, not tied to one codebase.

### 3. Small helper scripts

- `scripts/init_harness.py`
  - installs the docs harness into a target repo
- `scripts/new_issue.py`
  - creates a new issue document and updates the backlog

## Repository Layout

```text
.codex-plugin/           Codex plugin metadata
skills/                  Reusable Codex skills
scripts/                 Bootstrap and issue helpers
assets/templates/docs/   Docs templates copied into target repos
```

## Best Fit

Harness Kit works best when:

- you are using Codex regularly
- you want the same workflow across multiple repositories
- you care about explainability, handoff quality, and durable notes
- you want repo hygiene and self-correction loops to be explicit instead of tribal knowledge

It is not a build system, framework, or package manager. It is a workflow kit.

## Manual vs Automatic

Harness Kit defines the workflow in Markdown.

That means it is very good at standardizing:

- what to read first
- how to open and track issues
- how to record failures and learning
- how to review drift and cleanup needs

But fully automatic enforcement still requires executable tooling in the target repository.

Use Harness Kit to define the loop first.  
Then add scripts, lint, CI, or validators in the target repo if you want hard enforcement.
