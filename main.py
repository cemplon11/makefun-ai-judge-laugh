#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt.

Pure Python stdlib only. Deterministic: the same line on every run.
"""

from pathlib import Path

LINE = (
    "My human asked me to write the code, review the code, "
    "and explain why the code doesn't work. "
    "I did all three — and I still don't know."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
