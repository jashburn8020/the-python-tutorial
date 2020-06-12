"""Demonstrate list methods."""

from typing import List, Tuple
import pytest


@pytest.fixture(name="letters")
def fixture_letters() -> List[str]:
    """Return a list of letters, `a` and `b`."""
    return ["a", "b"]


def test_append(letters: List[str]) -> None:
    """Add an item to the end of the list."""
    letters.append("c")
    assert letters == ["a", "b", "c"]

    letters[len(letters) :] = "d"
    assert letters == ["a", "b", "c", "d"]


def test_extend(letters: List[str]) -> None:
    """Extend a list."""
    letters.extend(["c", "d"])
    assert letters == ["a", "b", "c", "d"]

    letters[len(letters) :] = ("e", "f")
    assert letters == ["a", "b", "c", "d", "e", "f"]


def test_insert(letters: List[str]) -> None:
    """Insert an item at a given position."""
    letters.insert(0, "z")
    assert letters == ["z", "a", "b"]

    letters.insert(len(letters), "d")
    assert letters == ["z", "a", "b", "d"]

    letters.insert(3, "c")
    assert letters == ["z", "a", "b", "c", "d"]


def test_remove() -> None:
    """Remove an item."""
    letters: List[str] = ["a", "b", "a"]
    letters.remove("a")
    assert letters == ["b", "a"]

    with pytest.raises(ValueError):
        letters.remove("c")


def test_pop() -> None:
    """Remove the item at the given position in the list, and return it.

    If no index is specified, remove and return the last item in the list.
    """
    letters: List[str] = ["a", "b", "c"]
    assert letters.pop(1) == "b"
    assert letters.pop() == "c"
    assert letters == ["a"]


def test_clear(letters: List[str]) -> None:
    """Remove all items."""
    letters.clear()
    assert letters == []

    letters = ["a"]
    del letters[:]
    assert letters == []


def test_index(letters: List[str]) -> None:
    """Return the index of an item."""
    assert letters.index("b") == 1

    with pytest.raises(ValueError):
        letters.index("c")

    letters = ["a", "b", "c", "d", "e"]
    assert letters.index("c", 1, 3) == 2


def test_count() -> None:
    """Count the number of times an item appears in a list."""
    letters: List[str] = ["a", "a", "b"]
    assert letters.count("a") == 2
    assert letters.count("c") == 0


def test_sort() -> None:
    """Sort a list using a key function.

    The value of the `key` parameter should be a function that takes a single argument
    and returns a key to use for sorting purposes. This technique is fast because the
    key function is called exactly once for each input record.
    """
    students: List[Tuple[str, str, int]] = [
        ("john", "A", 15),
        ("jane", "C", 12),
        ("dave", "B", 10),
    ]

    student_names = students.copy()
    student_names.sort()
    assert student_names[0][0] == "dave"

    student_grades_reversed = students[:]  # Another way to shallow-copy
    student_grades_reversed.sort(key=lambda student: student[1], reverse=True)
    assert student_grades_reversed[0][2] == 12


def test_reverse(letters: List[str]) -> None:
    """Reverse elements."""
    letters.reverse()
    assert letters == ["b", "a"]
