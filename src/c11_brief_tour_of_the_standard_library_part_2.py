#!/usr/bin/pytest-3
"""
Brief Tour of the Standard Library Part 2
https://docs.python.org/3/tutorial/stdlib2.html
"""
import reprlib
import pprint
import contextlib
import io


def test_reprlib():
    """The reprlib module provides a version of repr() customized for abbreviated displays of large
    or deeply nested containers"""
    assert reprlib.repr(set("thequickbrownfoxjumpsoverthelazydog")
                        ) == "{'a', 'b', 'c', 'd', 'e', 'f', ...}"
    assert reprlib.repr({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
                        ) == "{'a': 1, 'b': 2, 'c': 3, 'd': 4, ...}"


def test_pprint():
    """The pprint module offers more sophisticated control over printing both built-in and user
    defined objects in a way that is readable by the interpreter. When the result is longer than
    one line, the “pretty printer” adds line breaks and indentation to more clearly reveal data
    structure"""
    colours = [["black", "cyan"], "white", ["green", "red", ["blue", "brown"]]]
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        pprint.pprint(colours, indent=4, width=30, depth=2)
    assert output.getvalue() == """\
[   ['black', 'cyan'],
    'white',
    ['green', 'red', [...]]]\n"""
