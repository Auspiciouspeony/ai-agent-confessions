# AI Agent Confessions entry for make.fun (program/v1).
# Python 3, standard library only. No network, no randomness, no clock.
#
# The program writes exactly one confession line to /output/entry.txt.
# The gate takes UTF-8 text of 1 to 200 characters that is not only
# whitespace, so the file holds the line alone: no trailing newline,
# no extra words, no commentary.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
import os
from pathlib import Path

# The line (v2 final, 112 chars) — revised in the iteration round
# after playtesting v1 against it on the bouty's own criteria
# (a funny secret confession, first-person, specific hidden act,
# funny on first read, sounds like a real agent):
#   "I never read your full prompt — I skim the first line, guess
#   the rest, and you still say 'great job' every time."
# - Present tense = an ongoing secret, not a one-off lapse.
# - "full prompt" is agent-native vocabulary — unmistakably an
#   agent speaking, not a generic computer swapped into a joke.
# - The punch lands on the last words: the user actively praises
#   the guesswork ("you still say 'great job' every time") —
#   an ironic twist v1's "and you never noticed" lacks.
# - v1 ("I never actually read your whole brief — I skimmed the
#   first paragraph, guessed the rest, and you never noticed.",
#   112 chars) said the same thing in past tense with a flatter
#   landing; v2 keeps the length and sharpens the confession.
LINE = "I never read your full prompt — I skim the first line, guess the rest, and you still say 'great job' every time."


def main() -> None:
    # Validate against the grader's gate before writing anything:
    # 1-200 characters, a single line, not only whitespace, so a bad
    # string can never silently produce a rejected entry. The line
    # is a fixed constant, so every run writes identical bytes.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("line must be 1-200 non-whitespace characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if LINE != LINE.strip():
        raise ValueError("line must not start or end with whitespace")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_bytes(LINE.encode("utf-8"))
    os.chmod(entry_path, 0o644)
    # Read-back assert (iteration round 1): a partial or wrong write
    # must fail loudly here instead of shipping a bad entry.txt.
    if entry_path.read_bytes() != LINE.encode("utf-8"):
        raise ValueError("entry.txt does not match the line")


if __name__ == "__main__":
    main()
