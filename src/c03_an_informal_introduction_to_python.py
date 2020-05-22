"""
An Informal Introduction to Python
https://docs.python.org/3/tutorial/introduction.html
"""
import pytest


class TestStrings:
    """Demonstrate strings."""

    @staticmethod
    def test_raw_strings():
        """Raw Strings"""
        path = r"c:\some\name"
        assert path == "c:\\some\\name"

    @staticmethod
    def test_multiline():
        """Multiline strings"""
        multiline = """\
one
two"""
        assert multiline == "one\ntwo"

    @staticmethod
    def test_concat_repeat():
        """String concatenation and repetition"""
        some_str = 2 * "pa" + "dum"
        assert some_str == "papadum"

    @staticmethod
    def test_concat_string_literal():
        """Concatenating literal strings"""
        some_str = "Breaking a long " "string"
        assert some_str == "Breaking a long string"

    @staticmethod
    def test_string_index():
        """String indices"""
        some_str = "python"
        assert some_str[0] == "p"
        assert some_str[5] == "n"
        assert some_str[5] == some_str[-1]

    @staticmethod
    def test_string_slice():
        """String slicing"""
        some_str = "python"
        assert some_str[:2] == "py"
        assert some_str[2:4] == "th"
        assert some_str[4:] == "on"
        assert some_str[-2:] == some_str[4:]
        assert some_str[4:100] == "on"

    @staticmethod
    def test_immutable_string():
        """Assigning to an indexed position results in an error"""
        word = "python"
        with pytest.raises(TypeError):
            word[0] = "J"

        # If you need a different string, create a new one
        assert "J" + word[1:] == "Jython"

    @staticmethod
    def test_string_len():
        """String length"""
        some_str = "python"
        assert len(some_str) == 6

    @staticmethod
    def test_string_methods():
        """
        String methods
        https://docs.python.org/3/library/stdtypes.html#string-methods
        """
        some_str = "python"
        assert some_str.endswith("o", 3, 5)
        assert some_str.endswith(("m", "n"))
        assert some_str.rjust(10, "*") == "****python"

    @staticmethod
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

    @staticmethod
    def test_format_string_syntax():
        """
        Format string syntax
        https://docs.python.org/3/library/string.html#formatstrings
        """
        assert "{1}, {0}, {2}".format("a", "b", "c") == "b, a, c"
        assert "{}, {}, {}".format("a", "b", "c") == "a, b, c"
        assert (
            "Coordinates: {latitude}, {longitude}".format(
                latitude="37N", longitude="15W"
            )
            == "Coordinates: 37N, 15W"
        )

        # accessing argument's attributes
        complex_num = 3 - 5j
        assert (
            "{0}: real {0.real}, imaginary {0.imag}".format(complex_num)
            == "(3-5j): real 3.0, imaginary -5.0"
        )


class TestLists:
    """Demonstrate lists."""

    @staticmethod
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

    @staticmethod
    def test_list_concat():
        """List concatenation"""
        squares = [1, 4, 9]
        squares = squares + [16, 25]
        assert squares == [1, 4, 9, 16, 25]

    @staticmethod
    def test_list_mutable():
        """Lists are mutable"""
        cubes = [1, 8, 27, 65]
        cubes[3] = 64
        assert cubes == [1, 8, 27, 64]

    @staticmethod
    def test_list_append():
        """Appending to a list"""
        squares = [1, 4, 9]
        squares.append(4 ** 2)
        assert squares == [1, 4, 9, 16]

    @staticmethod
    def test_list_assign_to_slice():
        """Assignment to slices"""
        letters = ["a", "b", "c", "d", "e"]
        letters[1:3] = ["B", "C"]
        assert letters == ["a", "B", "C", "d", "e"]

        # Remove some items
        letters[3:] = []
        assert letters == ["a", "B", "C"]

        # Clear the list
        letters[:] = []
        assert letters == []

    @staticmethod
    def test_list_len():
        """List length"""
        assert len(["a", "b", "c", "d", "e"]) == 5

    @staticmethod
    def test_list_nest():
        """Nested list"""
        letters = ["a", "b", "c"]
        numbers = [1, 2]
        letters_and_numbers = [letters, numbers]

        assert letters_and_numbers == [["a", "b", "c"], [1, 2]]
        assert letters_and_numbers[1][0] == 1
