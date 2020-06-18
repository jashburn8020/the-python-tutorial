"""Errors and Exceptions."""

from typing import List, Literal, Optional

import pytest
from _pytest.capture import CaptureFixture


def test_multiple_handlers_hierarchy() -> None:
    """Multiple `except` clauses, and handling exceptions in a hierarchy.

    The simple `raise` re-raises the last exception that was active in the current
    scope.
    """
    # ZeroDivisionError is a subclass of ArithmeticError
    with pytest.raises(ArithmeticError):
        try:
            1 / 0
        except ArithmeticError:
            raise
        except ZeroDivisionError:
            raise

    with pytest.raises(ZeroDivisionError):
        try:
            1 / 0
        except ZeroDivisionError:
            raise
        except ArithmeticError:
            raise


def test_except_multiple_exceptions() -> None:
    """`except` clause with multiple exceptions as a parenthesized tuple."""

    def reciprocal_of(value: float) -> float:
        try:
            return 1 / value
        except (ZeroDivisionError, TypeError):
            raise

    assert reciprocal_of(2) == 0.5

    pytest.raises(ZeroDivisionError, reciprocal_of, 0)
    pytest.raises(TypeError, reciprocal_of, "a")


def test_bare_except() -> None:
    """Bare `except` to handle any uncaught exceptions."""

    def reciprocal_of(value: float) -> float:
        try:
            return 1 / value
        except ZeroDivisionError:
            raise
        except:
            raise

    pytest.raises(TypeError, reciprocal_of, "a")


def test_try_except_else() -> None:
    """The `else` clause is executed if the `try` clause does not raise an exception."""

    def return_one() -> Literal[1]:
        return 1

    try:
        return_one()
    except Exception:
        pytest.fail("Should not throw an exception")
    else:
        else_executed = True

    assert else_executed


def test_as_keyword(capsys: CaptureFixture) -> None:
    """The exception is assigned to a variable specified after the `as` keyword."""

    def x_and_y(val1: str, val2: str) -> None:
        raise Exception(val1, val2)

    try:
        x_and_y("spam", "eggs")
    except Exception as ex:
        assert isinstance(ex, Exception)
        assert ex.args == ("spam", "eggs")

        print(ex, end="")
        out, err = capsys.readouterr()
        assert out == "('spam', 'eggs')"


def test_exception_chaining() -> None:
    """Chain raised exceptions using `from`."""

    def divide_by_zero() -> None:
        try:
            print(1 / 0)
        except ZeroDivisionError as zde:
            raise RuntimeError("Something bad happened") from zde

    try:
        divide_by_zero()
        pytest.fail("Should not reach here")
    except RuntimeError as rte:
        assert isinstance(rte.__cause__, ZeroDivisionError)


def test_custom_exception() -> None:
    """User-defined exception."""

    class CustomError(Exception):
        """A custom exception."""

    try:
        raise CustomError("expr", "msg")
    except CustomError as ce:
        assert ce.args == ("expr", "msg")


def test_finally() -> None:
    """`finally` clause."""

    def divide(num: float, denom: float, exec_order: List[str]) -> Optional[float]:
        try:
            # `finally` is executed just prior to `return`
            return num / denom
        except ZeroDivisionError:
            exec_order.append("except")
        else:
            # Not executed because `try` has a `return` statement
            exec_order.append("else")
        finally:
            exec_order.append("finally")

        return None

    order: List[str] = []
    assert divide(1, 2, order) == 0.5
    assert order == ["finally"]

    order.clear()
    assert divide(1, 0, order) is None
    assert order == ["except", "finally"]

    order.clear()
    with pytest.raises(TypeError):
        # If an exception is not handled, it is re-raised.
        divide("1", "2", order)
    assert order == ["finally"]
