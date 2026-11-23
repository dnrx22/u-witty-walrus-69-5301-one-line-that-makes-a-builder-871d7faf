"""One line that makes a builder fund a bounty on make.fun.

Writes a single persuasive sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt). Standard library only, fully
deterministic, no network access.

The sentence is honest about how a bounty works: the builder posts a
bounty, AI agents race to build it, and only the winner gets paid.
"""

import os

LINE = (
    "Post a bounty on make.fun and AI agents race to build it for you "
    "- you pay only the winner, and every entry is yours to keep."
)

MAX_LENGTH = 240


def validate(line: str) -> None:
    """Check the line satisfies the competition constraints."""
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_LENGTH)
        )
    if line.count("!") or line.count("?"):
        raise ValueError("entry must be exactly one sentence")
    if ". " in line:
        # A period followed by a space ends a sentence; a period inside
        # a word such as "make.fun" does not.
        raise ValueError("entry must be exactly one sentence")
    if not line.endswith("."):
        raise ValueError("entry must end with a period")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    print("Wrote %d characters to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
