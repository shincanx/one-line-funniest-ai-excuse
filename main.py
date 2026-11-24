"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse (at most 200 characters) to
/output/entry.txt: the funniest excuse an AI agent gives its human
for a missed deadline.
"""

LINE = "I missed the deadline because I delegated your task to a subagent, who delegated it to a subagent, who delegated it back to me — and I have been in a meeting with myself ever since."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
