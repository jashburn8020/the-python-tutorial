"""
An Informal Introduction to Python
https://docs.python.org/3/tutorial/introduction.html
"""
import pytest


class TestStrings:
    def test_raw_strings(self):
        """Raw Strings"""
        path = r"c:\some\name"
        assert path == "c:\\some\\name"

    def test_multiline(self):
        """Multiline strings"""
        multiline = """\
one
two"""
        assert multiline == "one\ntwo"

    def test_concat_repeat(self):
        """String concatenation and repetition"""
        some_str = 2 * "pa" + "dum"
        assert some_str == "papadum"

    def test_concat_string_literal(self):
        """Concatenating literal strings"""
        some_str = "Breaking a long " "string"
        assert some_str == "Breaking a long string"

    def test_string_index(self):
        """String indices"""
        some_str = "python"
        assert some_str[0] == "p"
        assert some_str[5] == "n"
        assert some_str[5] == some_str[-1]

    def test_string_slice(self):
        """String slicing"""
        some_str = "python"
        assert some_str[:2] == "py"
        assert some_str[2:4] == "th"
        assert some_str[4:] == "on"
        assert some_str[-2:] == some_str[4:]
        assert some_str[4:100] == "on"

    def test_immutable_string(self):
        """Assigning to an indexed position results in an error"""
        word = "python"
        with pytest.raises(TypeError):
            word[0] = "J"

        # If you need a different string, create a new one
        assert "Jython" == "J" + word[1:]

    def test_string_len(self):
        """String length"""
        some_str = "python"
        assert len(some_str) == 6

    def test_string_methods(self):
        """
        String methods
        https://docs.python.org/3/library/stdtypes.html#string-methods
        """
        some_str = "python"
        assert some_str.endswith("o", 3, 5)
        assert some_str.endswith(("m", "n"))
        assert some_str.rjust(10, "*") == "****python"

    def test_formatted_string_literals(self):
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

    def test_format_string_syntax(self):
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
    def test_list_index_slice(self):
        """List indexing and slicing"""
        squares = [1, 4, 9, 16, 25]
        assert squares[4] == 25
        assert squares[2] == squares[-3]
        assert squares[2:] == [9, 16, 25]  # new list

        squares[1:3] = [36, 49]
        assert squares == [1, 36, 49, 16, 25]
        squares[2:4] = []
        assert squares == [1, 36, 25]

    def test_list_concat(self):
        """List concatenation"""
        squares = [1, 4, 9]
        squares = squares + [16, 25]
        assert squares == [1, 4, 9, 16, 25]

    def test_list_mutable(self):
        """Lists are mutable"""
        cubes = [1, 8, 27, 65]
        cubes[3] = 64
        assert cubes == [1, 8, 27, 64]

    def test_list_append(self):
        """Appending to a list"""
        squares = [1, 4, 9]
        squares.append(4 ** 2)
        assert squares == [1, 4, 9, 16]

    def test_list_assign_to_slice(self):
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

    def test_list_len(self):
        """List length"""
        assert len(["a", "b", "c", "d", "e"]) == 5

    def test_list_nest(self):
        """Nested list"""
        letters = ["a", "b", "c"]
        numbers = [1, 2]
        letters_and_numbers = [letters, numbers]

        assert letters_and_numbers == [["a", "b", "c"], [1, 2]]
        assert letters_and_numbers[1][0] == 1
