#!/usr/bin/pytest-3
"""
Errors and Exceptions
https://docs.python.org/3/tutorial/errors.html
"""
import pytest

# Handling exceptions


def test_except_multiple_exceptions():
    """Except clause with multiple exceptions as a parenthesized tuple"""
    def reciprocal_of(value):
        reciprocal = 0
        try:
            reciprocal = 1 / value
        except (ZeroDivisionError, TypeError):
            pass

        return reciprocal

    assert reciprocal_of(0) == 0
    assert reciprocal_of("a") == 0

    assert reciprocal_of(2) == 0.5


def test_exception_hierarchy():
    """Handling of exception hierarchy"""
    # pylint: disable=bad-except-order, broad-except
    caught_exception = None
    try:
        1 / 0
    except ArithmeticError:
        caught_exception = ArithmeticError
    except ZeroDivisionError:
        caught_exception = ZeroDivisionError

    assert caught_exception == ArithmeticError

    caught_exception = None
    try:
        1 / 0
    except ZeroDivisionError:
        caught_exception = ZeroDivisionError
    except ArithmeticError:
        caught_exception = ArithmeticError

    assert caught_exception == ZeroDivisionError


def test_bare_except():
    """Last except clause may omit the exception name(s), to serve as a wildcard. Use this with
    extreme caution, since it is easy to mask a real programming error in this way! It can be used
    to print an error message and then re-raise the exception (allowing a caller to handle the
    exception)."""
    def reciprocal_of(value):
        # pylint: disable=try-except-raise
        reciprocal = 0
        try:
            reciprocal = 1 / value
        except ZeroDivisionError:
            pass
        except:  # nopep8
            # If no expressions are present, raise re-raises the last exception that was active
            # in the current scope. If no exception is active in the current scope, a
            # RuntimeError exception is raised indicating that this is an error.
            raise

        return reciprocal

    pytest.raises(TypeError, reciprocal_of, "a")


def test_exception_chaining():
    """The from clause is used for exception chaining: if given, the second expression must be
    another exception class or instance, which will then be attached to the raised exception as the
    __cause__ attribute (which is writable)."""
    def divide_by_zero():
        try:
            1 / 0
        except ZeroDivisionError as zde:
            # Exception class is passed - it will be implicitly instantiated by calling its
            # constructor with no arguments
            raise RuntimeError from zde

    try:
        divide_by_zero()
    except RuntimeError as rte:
        assert isinstance(rte.__cause__, ZeroDivisionError)


def test_try_except_else():
    """The else clause, when present, must follow all except clauses. It is useful for code that
    must be executed if the try clause does not raise an exception."""
    # pylint: disable=broad-except
    def return_one():
        return 1

    try:
        one = return_one()
    except Exception:
        pytest.fail("Should not throw an exception")
    else:
        assert one == 1


def test_exception_arguments():
    """When an exception occurs, it may have an associated value, also known as the exception's
    argument. The presence and type of the argument depend on the exception type."""
    try:
        raise RuntimeError("spam", "eggs")
    except RuntimeError as rte:
        # Arguments stored in .args
        assert rte.args == ("spam", "eggs")
        # For convenience, the exception instance defines __str__() so the arguments can be printed
        # directly without having to reference .args.
        assert str(rte) == "('spam', 'eggs')"

# Defining clean-up actions


def test_finally():
    """If a finally clause is present, the finally clause will execute as the last task before the
    try statement completes. The finally clause runs whether or not the try statement produces an
    exception. It is useful for releasing external resources (such as files or network
    connections), regardless of whether the use of the resource was successful."""
    def divide(num, denom, exec_order):
        try:
            num / denom
        except ZeroDivisionError:
            exec_order.append("except")
            return exec_order
        else:
            exec_order.append("else")
            return exec_order
        finally:
            exec_order.append("finally")

        return exec_order

    order = []
    divide(1, 2, order)
    assert order == ["else", "finally"]

    order.clear()
    divide(1, 0, order)
    assert order == ["except", "finally"]

    order.clear()
    with pytest.raises(TypeError):
        divide("1", "2", order)
    assert order == ["finally"]
