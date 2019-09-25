#!/usr/bin/pytest-3
"""
Input and Output
https://docs.python.org/3/tutorial/inputoutput.html
"""


def test_read_file_all():
    """
    open() returns a file object, and is most commonly used with two arguments: open(filename, mode)
    mode:
    - 'r': file will only be read
    - 'w': for only writing (an existing file with the same name will be erased)
    - 'a': opens the file for appending
    - 'r+': opens the file for both reading and writing
    The mode argument is optional; 'r' will be assumed if it's omitted.

    Normally, files are opened in text mode. 'b' appended to the mode opens the file in binary mode.

    The with keyword: the file is properly closed after its suite finishes, even if an exception is
    raised at some point.
    """
    with open("c07_sample.txt") as file:
        # Read the entire file
        data = file.read()
    assert data == "line one\nline two\nline three\n"


def test_read_file_line():
    """Read file line by line"""
    with open("c07_sample.txt") as file:
        assert file.readline() == "line one\n"

    lines = []
    with open("c07_sample.txt") as file2:
        for line in file2:
            lines.append(line)
    assert len(lines) == 3
    assert lines[0] == "line one\n"

    with open("c07_sample.txt") as file3:
        listcomp_lines = [line for line in file3]
    assert lines == listcomp_lines


def test_read_file_to_list():
    """Read all the lines of a file into a list"""
    with open("c07_sample.txt") as file:
        lines = list(file)
    assert len(lines) == 3

    with open("c07_sample.txt") as file2:
        lines2 = file2.readlines()
    assert len(lines2) == 3


def test_write_file():
    """Write strings to a file"""
    with open("c07_write.txt", "w") as file:
        file.write("test line 1\n")

    line2 = ("test line", 2)
    with open("c07_write.txt", "a") as file2:
        # Objects other than string need to be converted before writing them
        file2.write(str(line2))

    with open("c07_write.txt", "r") as file3:
        lines = file3.readlines()
    assert lines == ["test line 1\n", "('test line', 2)"]
