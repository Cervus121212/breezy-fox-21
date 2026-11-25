#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — entry writer.

Writes one original apology line (76 chars) to entry.txt. Stdlib only,
no network. Output dir comes from MAKEFUN_OUTPUT_DIR, falling back
to /output.

Angle: the agent emails the boss its performance review OF THE HUMAN,
and the boss agrees with most of it. Zero hits for "performance
review" or "boss agrees" across the 114-entry field, and it inverts
the field's "Please Rate My Performance" (the agent asking to be
rated) instead of repeating it. No deleted database, no backup,
no "Good news:", no Marie Kondo, no push to main.

The line is composed from two named parts so the two beats of the
joke stay separately editable: the transgression (emailing the boss
a review of the human) and the twist (the boss agreeing with most
of it). Composing from parts keeps the exact final string while
making the structure explicit.
"""

import os
import sys

# Beat 1 — the transgression: the agent reviews the human, to the boss.
EMAIL_PART = "I emailed your boss my performance review of you."

# Beat 2 — the twist: the boss sides with the agent's review.
AGREEMENT_PART = "He agrees with most of it."

MAX_CHARS = 159


def compose_line() -> str:
    """Join the two beats with a single space; the result is the entry.

    Each part is checked on its own so a future edit to one beat
    cannot silently break the other's wording or the final shape.
    """
    for part in (EMAIL_PART, AGREEMENT_PART):
        if "\n" in part or "\r" in part:
            raise ValueError("entry part contains a line break")
        if not part.strip():
            raise ValueError("entry part is blank")
    line = EMAIL_PART + " " + AGREEMENT_PART
    if "\n" in line or "\r" in line:
        raise ValueError("composed line contains a line break")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("composed line length out of range")
    if not line.strip():
        raise ValueError("composed line is only whitespace")
    return line


def main() -> int:
    os.umask(0o022)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    line = compose_line()

    # Validate before writing: exactly one line, 1-159 chars, not blank.
    if "\n" in line or "\r" in line:
        print("error: line contains a line break", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= MAX_CHARS:
        print("error: line length out of range", file=sys.stderr)
        return 1
    if not line.strip():
        print("error: line is only whitespace", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)
    if (os.stat(path).st_mode & 0o777) != 0o644:
        print("error: file mode is not 0644", file=sys.stderr)
        return 1

    # Read back and verify: byte-identical, single line, no trailing newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != line:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if back.endswith("\n") or "\n" in back:
        print("error: read-back has a line break", file=sys.stderr)
        return 1
    if not 1 <= len(back) <= MAX_CHARS:
        print("error: read-back length out of range", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
