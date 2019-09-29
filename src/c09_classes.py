#!/usr/bin/pytest-3
"""
Classes
https://docs.python.org/3/tutorial/classes.html
"""
import pytest


def test_scope():
    """How to reference the different scopes and namespaces, and how global and nonlocal affect
    variable binding"""
    def do_local():
        # pylint: disable=redefined-outer-name
        # Redefines name from outer scope (global spam)
        spam = "local spam"
        assert spam  # workaround to suppress pyflakes warning that spam is unused - I know!

    def do_nonlocal():
        # pylint: disable=redefined-outer-name
        # Redefines name from outer scope (global spam)
        # nonlocal indicates that spam lives in an enclosing scope and should be rebound there.
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        # pylint: disable=invalid-name, global-variable-undefined
        # invalid-name: Constant name "spam" doesn't conform to UPPER_CASE naming style
        # global-variable-undefined: Global variable "spam" undefined at the module level
        # global indicates that spam lives in the global scope and should be rebound there.
        global spam
        spam = "global spam"

    # pylint: disable=redefined-outer-name
    spam = "test spam"

    do_local()
    assert spam == "test spam"

    do_nonlocal()
    assert spam == "nonlocal spam"

    do_global()
    assert spam == "nonlocal spam"


with pytest.raises(NameError, match="name 'spam' is not defined"):
    assert spam == "global spam"

# spam defined as global by do_global()
test_scope()
assert spam == "global spam"
