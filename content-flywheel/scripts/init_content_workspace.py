#!/usr/bin/env python3
"""Initialize a small workspace for the content-flywheel Hermes skill."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "creator-profile.md": """# Creator Profile

## Basic Identity
- public name:
- creator role:
- platforms:
- primary format:
- secondary formats:

## Audience
- primary audience:
- what they want:
- what they are stuck on:
- what they misunderstand:

## Content Promise
- audience enters with:
- audience leaves with:
- creator's unfair advantage:
- recurring enemy / false belief:
- recurring method / worldview:

## Content Lanes
| lane | purpose | examples | CTA |
|---|---|---|---|

## Products / Offers
| offer | status | audience | problem | CTA |
|---|---|---|---|---|
""",
    "style-rules.md": """# Style Rules

## Hooks

## Body

## Titles

## CTA

## Forbidden
""",
    "idea-inbox.md": """# Idea Inbox

Paste raw thoughts, user questions, conversations, or drafts here.
""",
    "published-log.csv": "date,platform,title,format,views,likes,comments,saves,shares,follows,leads,notes\n",
    "review-notes.md": """# Review Notes

Use this for performance reviews and reusable lessons.
""",
}


def write_if_missing(path: Path, text: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize content-flywheel workspace.")
    parser.add_argument("--root", default=".", help="Project root. Defaults to current directory.")
    parser.add_argument("--name", default="content-workspace", help="Workspace folder name.")
    args = parser.parse_args()

    workspace = Path(args.root).expanduser().resolve() / args.name
    created = []
    skipped = []
    for filename, body in FILES.items():
        path = workspace / filename
        if write_if_missing(path, body):
            created.append(path)
        else:
            skipped.append(path)

    print(f"workspace={workspace}")
    if created:
        print("created:")
        for path in created:
            print(f"- {path}")
    if skipped:
        print("skipped_existing:")
        for path in skipped:
            print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
