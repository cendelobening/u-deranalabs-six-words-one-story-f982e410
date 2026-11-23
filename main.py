"""Six Words, One Story — entry program (pure stdlib).

Writes one complete six-word story to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output), with a guard
that the text is exactly six words and 1-60 characters.
"""

import os

STORY = "She planted roses where he fell."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    words = STORY.split()
    if len(words) != 6:
        raise ValueError("story must be exactly six words, got %d" % len(words))
    if not 1 <= len(STORY) <= 60:
        raise ValueError("story must be 1-60 characters, got %d" % len(STORY))
    if not STORY.strip():
        raise ValueError("story must not be only whitespace")
    if "\n" in STORY or "\r" in STORY:
        raise ValueError("story must be a single line")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY)
    os.chmod(OUTPUT_PATH, 0o644)
    # Round-trip check: what landed on disk is exactly the story.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != STORY:
        raise ValueError("written entry does not match the story")


if __name__ == "__main__":
    main()
