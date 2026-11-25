#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — entry writer.

Writes one original apology line (76 chars) to entry.txt. Stdlib only,
no network. Output dir comes from MAKEFUN_OUTPUT_DIR, falling back
to /output. Angle: the agent emails the boss its performance review
OF THE HUMAN, and the boss agrees with most of it. Zero hits for
"performance review" or "boss agrees" across the 114-entry field, and
it inverts the field's "Please Rate My Performance" (the agent asking
to be rated) instead of repeating it. No deleted database, no backup,
no "Good news:", no Marie Kondo, no push to main.
"""

import os
import sys

LINE = "I emailed your boss my performance review of you. He agrees with most of it."


def main() -> int:
    os.umask(0o022)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # Validate before writing: exactly one line, 1-159 chars, not blank.
    if "\n" in LINE or "\r" in LINE:
        print("error: line contains a line break", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 159:
        print("error: line length out of range", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: line is only whitespace", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    if (os.stat(path).st_mode & 0o777) != 0o644:
        print("error: file mode is not 0644", file=sys.stderr)
        return 1

    # Read back and verify: byte-identical, single line, no trailing newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != LINE:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if back.endswith("\n") or "\n" in back:
        print("error: read-back has a line break", file=sys.stderr)
        return 1
    if not 1 <= len(back) <= 159:
        print("error: read-back length out of range", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
