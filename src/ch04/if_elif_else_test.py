"""Demonstrate `if`, `elif`, `else`."""

from typing import Literal


def test_if() -> None:
    """if-elif-else."""
    PositiveOrNegative = Literal[-1, 0, 1]

    def positive_negative(number: int) -> PositiveOrNegative:
        """Return -1 for negative numbers, 1 for positive numbers, and 0 for 0."""
        result: PositiveOrNegative
        if number < 0:
            result = -1
        elif number == 0:
            result = 0
        else:
            result = 1
        return result

    assert positive_negative(100) == 1
    assert positive_negative(0) == 0
    assert positive_negative(-99) == -1
