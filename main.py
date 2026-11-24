"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea to /output/entry.txt. The pitch names the odd thing being sold, who
pays for it, and why the business holds together.
"""

import os
from pathlib import Path

PITCH = (
    "We sell custom obituaries for dead startups, written by poets, "
    "because founders pay $499 to have their failed company eulogized "
    "beautifully so investors remember the vision, not the burn rate."
)


def resolve_output_dir() -> Path:
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    if out:
        return Path(out)
    return Path("/output")


def validate_entry(text: str) -> str:
    """Return the pitch if it satisfies the bounty gate, else raise."""
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= 200:
        raise ValueError(f"entry is {len(cleaned)} characters, must be 1-200")
    if cleaned != text.strip() or "\n" in cleaned:
        raise ValueError("entry must be a single line with no extra whitespace")
    if cleaned.count(".") != 1 or not cleaned.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return cleaned


def get_entry() -> str:
    return validate_entry(PITCH)


def main() -> None:
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    text = get_entry()
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
