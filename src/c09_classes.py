#!/usr/bin/pytest-3
"""
Classes
https://docs.python.org/3/tutorial/classes.html
"""
import pytest


# Odds and ends


# Iterators


def test_generator_expressions():
    """Some simple generators can be coded succinctly as expressions using a syntax similar to list
    comprehensions but with parentheses instead of square brackets. These expressions are designed
    for situations where the generator is used right away by an enclosing function. Generator
    expressions are more compact but less versatile than full generator definitions, and tend to be
    more memory friendly than equivalent list comprehensions."""

    assert sum(i * i for i in range(10)) == 285

    data = "golf"
    assert "".join(data[index] for index in range(len(data) - 1, -1, -1)) == "flog"
