"""Demonstrate lists."""

from typing import List, Union


def test_list_index_slice() -> None:
    """List indexing and slicing."""
    squares = [1, 4, 9, 16, 25]
    assert squares[4] == 25
    assert squares[2] == squares[-3]
    assert squares[2:] == [9, 16, 25]  # new list

    squares[1:3] = [36, 49]
    assert squares == [1, 36, 49, 16, 25]
    squares[2:4] = []
    assert squares == [1, 36, 25]


def test_list_concat() -> None:
    """List concatenation."""
    squares = [1, 4, 9]
    squares += [16, 25]
    assert squares == [1, 4, 9, 16, 25]


def test_list_mutable() -> None:
    """Lists are mutable."""
    cubes = [1, 8, 27, 65]
    cubes[3] = 64
    assert cubes == [1, 8, 27, 64]


def test_list_append() -> None:
    """Appending to a list."""
    squares = [1, 4, 9]
    squares.append(4 ** 2)
    assert squares == [1, 4, 9, 16]


def test_list_assign_to_slice() -> None:
    """Assignment to slices."""
    letters = ["a", "b", "c", "d", "e"]
    letters[1:3] = ["B", "C"]
    assert letters == ["a", "B", "C", "d", "e"]

    # Remove some items
    letters[3:] = []
    assert letters == ["a", "B", "C"]

    # Clear the list
    letters[:] = []
    assert letters == []


def test_list_len() -> None:
    """List length."""
    assert len(["a", "b", "c", "d", "e"]) == 5


def test_list_nest() -> None:
    """Nested list."""
    letters = ["a", "b", "c"]
    numbers = [1, 2]
    letters_and_numbers: List[Union[List[int], List[str]]] = [letters, numbers]

    assert letters_and_numbers == [["a", "b", "c"], [1, 2]]
    assert letters_and_numbers[1][0] == 1
