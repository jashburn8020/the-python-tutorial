"""Demonstrate `range()`."""

from typing import List, Tuple


def test_range() -> None:
    """`range()` function."""
    numbers: List[int] = []
    for i in range(5):
        numbers.append(i)

    assert numbers == [0, 1, 2, 3, 4]

    numbers.clear()
    for i in range(5, 10):
        numbers.append(i)

    assert numbers == [5, 6, 7, 8, 9]

    numbers.clear()
    for i in range(0, 12, 3):
        numbers.append(i)

    assert numbers == [0, 3, 6, 9]


def test_range_iterate_over_indices() -> None:
    """Iterate over the indices of a sequence."""
    rhyme: List[str] = ["Mary", "had", "a", "little", "lamb"]
    odd_rhyme: List[Tuple[int, str]] = []
    for i in range(1, len(rhyme), 2):
        odd_rhyme.append((i, rhyme[i]))

    assert odd_rhyme == [(1, "had"), (3, "little")]


def test_range_iterable() -> None:
    """range() returns an iterable.

    The `for` statement is an iterator, and so is `list()`.
    """
    numbers: List[int] = list(range(10))
    assert numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sum(numbers) == 45
