"""Office Joke Open entry: writes one single-line office joke to /output/entry.txt.

The joke: a reply-all storm (a specific, real office disaster) ended by the
very thing that caused it. Concrete detail: 214 reply-all emails. Twist in
the last words: everyone replies-all to agree with the order to stop.
"""
import os

JOKE = (
    "After 214 reply-all emails, IT stopped the storm by replying-all: "
    "'Please stop replying-all.' Everyone replied-all to agree."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
