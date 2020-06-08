"""Demonstrate `for`."""

from typing import List


def test_for_string() -> None:
    """Iterate over a string."""
    alpha = "ababa"
    num_of_as = 0

    for letter in alpha:
        if letter == "a":
            num_of_as += 1

    assert num_of_as == 3


def test_for_list() -> None:
    """Iterate over a list."""
    words: List[str] = ["cat", "window", "defenestrate"]
    char_count: List[int] = []
    for word in words:
        char_count.append(len(word))

    assert char_count == [3, 6, 12]


def test_for_modify() -> None:
    """Modifying a list in a `for` loop.

    If you need to modify the sequence you are iterating over while inside the loop
    (for example to duplicate selected items), it is recommended that you first make a
    copy.
    """
    words: List[str] = ["cat", "window", "defenestrate"]
    for word in words[:]:  # copy of words
        if len(word) > 5:
            words.insert(0, word)

    assert words == ["defenestrate", "window", "cat", "window", "defenestrate"]


def test_for_modify_no_copy() -> None:
    """Modifying a list in a `for` loop without first making a copy of the list.

    Not a good idea.
    """
    words: List[str] = ["cat", "window", "defenestrate"]
    for word in words:
        if len(word) > 5 and len(words) < 7:
            words.insert(0, word)

    assert words == [
        "window",
        "window",
        "window",
        "window",
        "cat",
        "window",
        "defenestrate",
    ]
