#!/usr/bin/pytest-3
"""
An Informal Introduction to Python
https://docs.python.org/3/tutorial/introduction.html
"""

# Strings


def test_raw_strings():
    """Raw Strings"""
    path = r"c:\some\name"
    assert path == "c:\\some\\name"


def test_multiline():
    """Multiline strings"""
    multiline = """\
one
two"""
    assert multiline == "one\ntwo"


def test_concat_repeat():
    """String concatenation and repetition"""
    some_str = 3 * "un" + "nium"
    assert some_str == "unununnium"


def test_concat_string_literal():
    """Concatenating literal strings"""
    some_str = ("Breaking a long "
                "string")
    assert some_str == "Breaking a long string"


def test_string_index():
    """String indices"""
    some_str = "python"
    assert some_str[0] == "p"
    assert some_str[5] == "n"
    assert some_str[5] == some_str[-1]


def test_string_slice():
    """String slicing"""
    some_str = "python"
    assert some_str[:2] == "py"
    assert some_str[2:4] == "th"
    assert some_str[4:] == "on"
    assert some_str[-2:] == some_str[4:]
    assert some_str[4:100] == "on"


def test_string_len():
    """String length"""
    some_str = "python"
    assert len(some_str) == 6


def test_string_methods():
    """
    String methods
    https://docs.python.org/3/library/stdtypes.html#string-methods
    """
    some_str = "python"
    assert some_str.endswith("o", 3, 5)
    assert some_str.endswith(('m', 'n'))
    assert some_str.rjust(10, "*") == "****python"


def test_formatted_string_literals():
    """
    Formatted string literals
    https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    """
    name = "Fred"
    assert f"He said his name is {name!r}" == "He said his name is 'Fred'"

    width = 7
    precision = 4
    value = 12.34567
    assert f"result:{value:{width}.{precision}}" == "result:  12.35"


def test_format_string_syntax():
    """
    Format string syntax
    https://docs.python.org/3/library/string.html#formatstrings
    """
    assert "{1}, {0}, {2}".format("a", "b", "c") == "b, a, c"
    assert "{}, {}, {}".format("a", "b", "c") == "a, b, c"
    assert "Coordinates: {latitude}, {longitude}".format(
        latitude="37N", longitude="15W") == "Coordinates: 37N, 15W"

    # accessing argument's attributes
    complex_num = 3 - 5j
    assert "{0}: real {0.real}, imaginary {0.imag}".format(
        complex_num) == "(3-5j): real 3.0, imaginary -5.0"

# Lists


def test_list_index_slice():
    """List indexing and slicing"""
    squares = [1, 4, 9, 16, 25]
    assert squares[4] == 25
    assert squares[2] == squares[-3]
    assert squares[2:] == [9, 16, 25]  # new list

    squares[1:3] = [36, 49]
    assert squares == [1, 36, 49, 16, 25]
    squares[2:4] = []
    assert squares == [1, 36, 25]


def test_list_concat():
    """List concatentation"""
    squares = [1, 4, 9]
    squares = squares + [16, 25]
    assert squares == [1, 4, 9, 16, 25]


def test_list_append():
    """Appending to a list"""
    squares = [1, 4, 9]
    squares.append(4 ** 2)
    assert squares == [1, 4, 9, 16]
