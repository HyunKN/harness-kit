#!/usr/bin/env python3
"""Copy the docs harness templates into a target repository."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize a target repository with the harness docs templates."
    )
    parser.add_argument("target", help="Target repository root path.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite conflicting files instead of skipping them.",
    )
    return parser.parse_args()


def copy_tree(src: Path, dst: Path, force: bool) -> tuple[list[Path], list[Path]]:
    created: list[Path] = []
    skipped: list[Path] = []

    for source_path in src.rglob("*"):
        relative = source_path.relative_to(src)
        target_path = dst / relative

        if source_path.is_dir():
            target_path.mkdir(parents=True, exist_ok=True)
            continue

        target_path.parent.mkdir(parents=True, exist_ok=True)
        if target_path.exists() and not force:
            skipped.append(target_path)
            continue
        shutil.copy2(source_path, target_path)
        created.append(target_path)

    return created, skipped


def main() -> int:
    args = parse_args()
    target_root = Path(args.target).expanduser().resolve()
    template_root = Path(__file__).resolve().parent.parent / "assets" / "templates"

    if not template_root.is_dir():
        print(f"Template directory not found: {template_root}", file=sys.stderr)
        return 1

    target_root.mkdir(parents=True, exist_ok=True)
    created, skipped = copy_tree(template_root, target_root, args.force)

    print(f"Initialized docs harness in: {target_root}")
    print(f"Created or overwritten: {len(created)} file(s)")
    print(f"Skipped existing: {len(skipped)} file(s)")
    if skipped:
        print("Use --force to overwrite existing files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
