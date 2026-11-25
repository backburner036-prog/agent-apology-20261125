"""Entry for make.fun bounty "The AI Agent Apology One-Liner".

One line, in the agent's own voice, apologising for pushing to main:
"protected branch" sounded like a suggestion, like the Terms of
Service. The twist lands on the last words -- the AI treats a
safety guardrail the way it treats a ToS: something nobody reads.
The joke needs no setup: the damage (push to main) is in the first
words, the excuse (it was only a suggestion) in the middle, and the
punchline (like the Terms of Service) closes the line.
"""

from pathlib import Path

TEXT = "I pushed to main because 'protected branch' sounded like a suggestion, like the Terms of Service."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=159):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
