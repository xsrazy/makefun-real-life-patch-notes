"""make.fun entry: Real-Life Patch Notes: The Comedy Changelog.

Writes exactly one line -- a terse software patch note for a bug in
human biology / daily life -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). No trailing newline: the file holds
exactly the entry bytes, nothing else.
"""

import os

ENTRY = "v4.2.0: fixed a bug where crossing a doorway cleared the current task from short-term memory."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
