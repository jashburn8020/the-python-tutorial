"""Demonstrate lambda expressions."""

from typing import Any, Callable, Union


def test_lambda_function_object() -> None:
    """Lambda returned by a function."""

    def power(base: int) -> Callable[[int], Any]:
        """Lambda expression to calculate power."""
        # Power (** and pow()) return type is Any
        # See https://github.com/python/typeshed/issues/285
        return lambda exponent: base ** exponent

    two_raised_to_the_power_of = power(2)
    assert two_raised_to_the_power_of(3) == 8


def test_lambda_inline() -> None:
    """Lambda, inlined."""
    doubler: Callable[[Union[int, str]], Union[int, str]] = lambda value: value * 2
    assert doubler(5) == 10
    assert doubler("a") == "aa"
