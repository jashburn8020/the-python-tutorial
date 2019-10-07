#!/usr/bin/pytest-3
"""
Brief Tour of the Standard Library
https://docs.python.org/3/tutorial/stdlib.html
"""
import os
import re
import math
import random
import statistics
import datetime


def test_os():
    """The os module provides functions for interacting with the operating system."""
    os.environ["TEST"] = "tester"
    assert os.getenv("TEST") == "tester"


def test_re():
    """The re module provides regular expression tools for advanced string processing."""
    assert re.findall(
        r"\bf[a-z]*", "which foot or hand fell fastest") == ["foot", "fell", "fastest"]
    assert re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat") == "cat in the hat"


def test_math():
    """The math module gives access to the underlying C library functions for floating point
    math."""
    assert round(math.cos(math.pi / 4), 3) == round(math.sin(math.pi / 4), 3)
    assert math.log10(100) == 2


def test_random():
    """The random module provides tools for making random selections."""
    fruits = ["apple", "banana", "cherry"]
    assert random.choice(fruits) in fruits

    assert random.randint(1, 5) in [1, 2, 3, 4, 5]


def test_statistics():
    """The statistics module calculates basic statistical properties of numeric data."""
    data = [2, 2, 3, 4, 5]
    assert statistics.mean(data) == 3.2
    assert statistics.median(data) == 3
    assert statistics.mode(data) == 2


def test_datetime():
    """The datetime module supplies classes for manipulating dates and times. The module also
    supports objects that are timezone aware."""
    date1 = datetime.date(2003, 3, 3)
    date2 = datetime.date(2003, 4, 3)
    assert (date2 - date1).days == 31
