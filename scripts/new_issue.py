#!/usr/bin/env python3
"""Create a new issue doc from the issue template and update the backlog."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys


def slugify(text: str) -> str:
    lowered = text.strip().lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = re.sub(r"-{2,}", "-", lowered).strip("-")
    return lowered or "untitled-issue"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new issue doc in docs/issues.")
    parser.add_argument("repo", help="Target repository root.")
    parser.add_argument("slug", help="Short issue slug.")
    parser.add_argument("title", help="Human-readable issue title.")
    return parser.parse_args()


def inject_backlog(backlog_path: Path, display_date: str, title: str) -> None:
    line = f"- [{display_date}] {title}\n"
    text = backlog_path.read_text(encoding="utf-8")
    marker = "## Open\n\n"
    if marker not in text:
        raise RuntimeError("current_backlog.md is missing the '## Open' section.")
    if line in text:
        return
    updated = text.replace(marker, marker + line, 1)
    backlog_path.write_text(updated, encoding="utf-8")


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo).expanduser().resolve()
    issues_dir = repo_root / "docs" / "issues"
    template_path = issues_dir / "issue-template.md"
    backlog_path = issues_dir / "current_backlog.md"

    if not template_path.is_file():
        print(f"Issue template not found: {template_path}", file=sys.stderr)
        return 1
    if not backlog_path.is_file():
        print(f"Backlog file not found: {backlog_path}", file=sys.stderr)
        return 1

    today = date.today().isoformat()
    slug = slugify(args.slug)
    issue_name = f"issue-{today}-{slug}.md"
    issue_path = issues_dir / issue_name
    if issue_path.exists():
        print(f"Issue already exists: {issue_path}", file=sys.stderr)
        return 1

    body = template_path.read_text(encoding="utf-8")
    body = body.replace("{{DATE}}", today)
    body = body.replace("{{TITLE}}", args.title.strip())
    body = body.replace("{{SLUG}}", slug)
    issue_path.write_text(body, encoding="utf-8")
    inject_backlog(backlog_path, today, args.title.strip())

    print(f"Created issue: {issue_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
