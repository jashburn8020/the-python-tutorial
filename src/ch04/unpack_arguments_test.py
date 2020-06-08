"""Demonstrate unpacking arguments."""

from typing import Tuple


def keyword_arguments(
    first: int, second: int = 2, third: int = 3
) -> Tuple[int, int, int]:
    """Accept 1 required argument and 2 optional arguments."""
    return (first, second, third)


def test_unpacking_arguments() -> None:
    """Unpack a list or tuple using the `*`-operator."""
    args = (10, 20, 30)
    # Without unpacking, the entire tuple is a single argument
    assert keyword_arguments(args) == ((10, 20, 30), 2, 3,)
    # Unpack
    assert keyword_arguments(*args) == (10, 20, 30)
    assert keyword_arguments(*(1, 2, 3)) == (1, 2, 3)


def test_unpack_dictionary() -> None:
    """Use the `**`-operator to unpack a dictionary."""
    args_dict = {"third": 30, "second": 20}
    assert keyword_arguments(first=10, **args_dict) == (10, 20, 30,)
