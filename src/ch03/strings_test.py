"""Demonstrate strings."""

import io
import pytest


def test_raw_strings() -> None:
    """Raw Strings."""
    path = r"c:\some\name"
    assert path == "c:\\some\\name"


def test_multiline() -> None:
    """Multiline strings."""
    multiline = """\
one
two"""
    assert multiline == "one\ntwo"


def test_concat_repeat() -> None:
    """String concatenation and repetition."""
    some_str = 2 * "pa" + "dum"
    assert some_str == "papadum"

    # Using str.join()
    strings = ["some", "strings"]
    assert " ".join(strings) == "some strings"

    # Using io.StringIO
    buffer = io.StringIO()
    buffer.write("some")
    buffer.write(" strings")
    stringio_content = buffer.getvalue()
    buffer.close()
    assert stringio_content == "some strings"


def test_concat_string_literal() -> None:
    """Concatenating literal strings."""
    some_str = "Breaking a long " "string"
    assert some_str == "Breaking a long string"


def test_string_index() -> None:
    """String indices."""
    some_str = "python"
    assert some_str[0] == "p"
    assert some_str[5] == "n"
    assert some_str[5] == some_str[-1]


def test_string_slice() -> None:
    """String slicing."""
    some_str = "python"
    assert some_str[:2] == "py"
    assert some_str[2:4] == "th"
    assert some_str[4:] == "on"
    assert some_str[-2:] == some_str[4:]
    assert some_str[4:100] == "on"


def test_immutable_string() -> None:
    """Assigning to an indexed position results in an error."""
    word = "python"
    with pytest.raises(TypeError):
        word[0] = "J"

    # If you need a different string, create a new one
    assert "J" + word[1:] == "Jython"


def test_string_len() -> None:
    """String length."""
    some_str = "python"
    assert len(some_str) == 6


def test_text_sequence_type() -> None:
    """Text sequence type - common sequence operations."""
    some_str = "python"
    assert "h" in some_str
    assert "e" not in some_str
    assert min(some_str) == "h"
    assert max(some_str) == "y"


def test_string_methods() -> None:
    """String methods."""
    some_str = "python"
    assert some_str.endswith("o", 3, 5)
    assert some_str.endswith(("m", "n"))
    assert some_str.rjust(10, "*") == "****python"


def test_formatted_string_literals() -> None:
    """Formatted string literals."""
    name = "Fred"
    assert f"He said his name is {name!r}" == "He said his name is 'Fred'"

    width = 7
    precision = 4
    value = 12.34567
    assert f"result:{value:{width}.{precision}}" == "result:  12.35"


def test_format_string_syntax() -> None:
    """Format string syntax."""
    assert "{1}, {0}, {2}".format("a", "b", "c") == "b, a, c"
    assert "{}, {}, {}".format("a", "b", "c") == "a, b, c"
    assert (
        "Coordinates: {latitude}, {longitude}".format(latitude="37N", longitude="15W")
        == "Coordinates: 37N, 15W"
    )

    # accessing argument's attributes
    complex_num = 3 - 5j
    assert (
        "{0}: real {0.real}, imaginary {0.imag}".format(complex_num)
        == "(3-5j): real 3.0, imaginary -5.0"
    )
