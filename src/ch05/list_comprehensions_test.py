"""List Comprehensions."""

import math
from typing import List, Tuple


def test_listcomp() -> None:
    """List comprehension, compared to using a 'normal' `for` loop."""
    # 'Normal' for loop
    squares: List[int] = []
    for num in range(5):
        squares.append(num ** 2)
    assert squares == [0, 1, 4, 9, 16]
    assert num == 4  # Side-effect: num exists after the loop completes

    # List comprehension - no side-effects
    squares_listcomp = [num ** 2 for num in range(5)]
    assert squares_listcomp == squares


def test_for_if() -> None:
    """List comprehension with multiple `for` and `if` clauses."""
    # 'Normal' for loops
    combinations: List[Tuple[int, int]] = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combinations.append((x, y))
    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # List comprehension
    combinations_listcomp: List[Tuple[int, int]] = [
        (i, j) for i in [1, 2, 3] for j in [3, 1, 4] if i != j
    ]
    assert combinations_listcomp == combinations


def test_filter() -> None:
    """Filter a list."""
    # Filter the list to exclude negative numbers
    assert [elem for elem in [-4, -2, 0, 2, 4] if elem >= 0] == [0, 2, 4]


def test_apply_functions() -> None:
    """Apply functions to all elements."""
    # Apply a function to all elements
    assert [abs(elem) for elem in [-4, -2, 0, 2, 4]] == [4, 2, 0, 2, 4]

    # Nested functions
    assert [str(round(math.pi, precision)) for precision in range(1, 4)] == [
        "3.1",
        "3.14",
        "3.142",
    ]


def test_element_method() -> None:
    """Call a method on each element."""
    fruits: List[str] = ["apple", "banana", "cherry"]
    assert [elem.upper() for elem in fruits] == ["APPLE", "BANANA", "CHERRY"]


def test_flatten_list() -> None:
    """Flatten a list."""
    nested_list: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert [num for elem in nested_list for num in elem] == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_split_string() -> None:
    """Split a string into its constituent letters."""
    assert [letter.upper() for letter in "abcde"] == ["A", "B", "C", "D", "E"]


def test_nested_listcomp() -> None:
    """The initial expression in a list comprehension can be any expression."""
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    transposed_matrix = [[row[elem] for row in matrix] for elem in range(4)]
    assert transposed_matrix == [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
