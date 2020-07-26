"""Output formatting using `reprlib`."""

import reprlib


def test_reprlib_string() -> None:
    """Limit the number of characters in a string representation."""
    test_str = "thequickbrownfoxjumpsoverthelazydog"

    assert (reprlib_str := reprlib.repr(test_str)) == "'thequickbrow...verthelazydog'"
    assert len(reprlib_str) == 30

    (short_repr := reprlib.Repr()).maxstring = 15

    assert (short_reprlib_str := short_repr.repr(test_str)) == "'thequ...zydog'"
    assert len(short_reprlib_str) == 15


def test_reprlib_dict() -> None:
    """Limit the number of entries in a dictionary representation."""
    test_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}

    assert reprlib.repr(test_dict) == "{'a': 1, 'b': 2, 'c': 3, 'd': 4, ...}"

    (short_repr := reprlib.Repr()).maxdict = 2
    assert short_repr.repr(test_dict) == "{'a': 1, 'b': 2, ...}"
