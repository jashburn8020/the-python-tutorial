"""Iterators."""

from typing import Generic, Iterator, List, Sequence, TypeVar

import pytest

T = TypeVar("T")


class Reverse(Generic[T]):
    """Container that iterates in reverse."""

    def __init__(self, data: Sequence[T]) -> None:
        self.data = data
        self.index = len(data)

    def __next__(self) -> T:
        """Return the next data item.

        The `next()` built-in function calls this method.
        """
        if self.index <= 0:
            raise StopIteration()
        self.index -= 1
        return self.data[self.index]

    def __iter__(self) -> Iterator[T]:
        """Return an object that defines the `__next__()` method.

        The `iter()` built-in function calls this method.
        """
        return self


def test_iterator_for() -> None:
    """Iterating through a custom iterator in a `for` loop."""
    rev_nums: List[int] = []
    for num in Reverse((1, 2, 3)):
        rev_nums.append(num)

    assert rev_nums == [3, 2, 1]
    assert list(Reverse((1, 2, 3))) == rev_nums


def test_iterator_manual() -> None:
    """Iterating through a custom iterator manually."""
    rev_letters: List[str] = []

    letters_iter: Iterator[str] = iter(Reverse("abc"))
    rev_letters.append(next(letters_iter))
    rev_letters.append(next(letters_iter))
    rev_letters.append(next(letters_iter))

    with pytest.raises(StopIteration):
        next(letters_iter)

    assert rev_letters == ["c", "b", "a"]
