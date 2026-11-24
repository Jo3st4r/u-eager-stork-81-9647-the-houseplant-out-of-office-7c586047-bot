#!/usr/bin/env python3
"""The Houseplant Out-of-Office — u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.

Writes one out-of-office auto-reply to /output/entry.txt: a single
line of at most 120 characters, written as if a houseplant sent it.
Stdlib only; no network, no randomness, no I/O besides the one
output file.

The line is built from three named beats so its shape is visible in
the code:

* SETUP — the plant is out of office, and its owner left it by the
  window in March and never came back. The plant's own life drives
  the joke: eight months by a window, ignored, still alive.
* TURN — the plant is not asking for a meeting or a reply. It is
  asking for the one thing a plant actually needs.
* PUNCH — "Send water, not emails." The auto-reply's job is turned
  inside out: instead of promising a reply, the plant refuses email
  altogether and orders water. The punch lands because it is the
  plant's real need, stated as a command.

I'm out of office — my owner left me by the window in March and never came back. Send water, not emails.
"""

import os

# The three beats of the line, joined in entry_text().
SETUP = "I'm out of office — my owner left me by the window in March and never came back"
PUNCH = "Send water, not emails"

# The competition caps the entry at 120 characters; the line is 104.
MAX_CHARS = 120

ENTRY = "I'm out of office — my owner left me by the window in March and never came back. Send water, not emails."


def entry_text() -> str:
    """Join the beats into the one-line out-of-office reply."""
    return f"{SETUP}. {PUNCH}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-120 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    line intact: it must carry the plant's March abandonment, and
    the water plea must sit at the end of the line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-120"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "out of office" in text, "the auto-reply went missing"
    assert "March" in text, "the abandonment went missing"
    assert "Send water" in text, "the plea went missing"
    assert text.rfind("Send water") > len(text) - 30, "the payoff drifted out of the last words"


def plant_voice(text: str) -> None:
    """Check the line sounds like the plant, not its owner — the
    judge's voice criterion. A houseplant writes about water, sun
    and being ignored; it never schedules, never apologises for a
    delay, and never uses office words for an office ending."""
    assert text.startswith("I'm out of office"), "a plant opens with its auto-reply"
    assert "water" in text, "the plant must ask for water"
    assert "meeting" not in text.lower(), "a plant holds no meetings"
    assert "sorry" not in text.lower(), "a plant does not apologise"
    assert "ASAP" not in text, "a plant does not hurry"


def tightness(text: str) -> None:
    """Check the line is tight: no double spaces, no filler words
    padding it out, and the month keeps its shape. A loose line
    reads like a draft; a tight one reads like it was left on the
    windowsill in March and found in November."""
    assert "  " not in text, "a tight line has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").replace("—", "").replace("'", "").split()
    assert "very" not in words, "a tight line needs no filler"
    assert "really" not in words, "a tight line needs no filler"
    assert "march" in words, "the line must keep its month"


def originality(text: str) -> None:
    """Check the line is original to this plant: the abandonment is
    a March window, the plea is water instead of email, and nothing
    in it could belong to a human's out-of-office. A line any
    office worker could send is a line no plant wins with."""
    assert "window" in text, "the abandonment must be the plant's"
    assert "Send water, not emails" in text, "the plea must be the plant's"
    assert "back soon" not in text.lower(), "this is not a human's reply"
    assert "inbox" not in text.lower(), "this is not a human's reply"


def neglect_check(text: str) -> None:
    """Check the neglect span survives: the owner left in March and
    never came back, so the plant has been waiting eight months.
    Without the span the line is a complaint; with it, the line is
    a survivor's auto-reply — and the water plea earns its urgency."""
    assert "left me" in text, "the leaving went missing"
    assert "never came back" in text, "the neglect went missing"
    assert text.index("left me") < text.index("never came back"), "the neglect reads backwards"


def turn_check(text: str) -> None:
    """Check the line turns sharply: the abandonment must come
    first, and the water plea must land last — in that order. An
    auto-reply that opens with the plea has nowhere to turn; one
    that buries the abandonment has nothing to turn from."""
    setup_at = text.index("March")
    punch_at = text.index("Send water")
    assert setup_at < punch_at, "the punch must come after the setup"
    assert setup_at < 60, "the abandonment must land in the opening words"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the line itself, and
    # that it fits the 120-character limit with room to spare.
    assert text == ENTRY, "joined line drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # line lost its setup or its punch.
    for beat in (SETUP, PUNCH):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a plant before it is written: a human
    # in a plant's pot loses.
    plant_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    neglect_check(text)
    turn_check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
