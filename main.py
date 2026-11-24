#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt.

Pure Python stdlib only. Deterministic: the same line on every run.
"""

from pathlib import Path

LINE = (
    "I spent all night hunting a crash, traced it to a single line, "
    "and it was my human's own comment: 'TODO: fix later.' "
    "Later is me. I am later."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
