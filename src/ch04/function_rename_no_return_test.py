"""Demonstrate renaming functions, and functions without a `return` statement."""

from typing import List


def test_function_rename() -> None:
    """Rename a function locally."""

    def fibonacci(maxval: int) -> List[int]:
        """Return a list containing the Fibonacci series up to `maxval`."""
        result: List[int] = []
        current, nextval = 0, 1
        while current < maxval:
            result.append(current)
            current, nextval = nextval, current + nextval
        return result

    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]
    fib = fibonacci
    assert fib(10) == [0, 1, 1, 2, 3, 5, 8]


def test_function_no_return() -> None:
    """Functions without a `return` statement do return a value - `None`."""

    def function_no_return() -> None:
        ...

    assert function_no_return() is None
