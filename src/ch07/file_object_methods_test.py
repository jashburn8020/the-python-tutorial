"""Methods of File Objects."""

from io import StringIO
from pathlib import Path
from typing import Final, List, Tuple

import pytest


SAMPLE_CONTENT: Final = """\
line one
line two

line three
"""


@pytest.fixture(name="sample_file")
def fixture_sample_file() -> Path:
    """Return a sample file."""
    return Path(__file__).parent.joinpath("sample.txt")


def test_read_all(sample_file: Path) -> None:
    """Read the entire contents of a file in one go in default text mode.

    Uses a `Path` object to represent the file to read.
    """
    with open(sample_file) as file:  # File object is a context manager
        data = file.read()
    assert data == SAMPLE_CONTENT
    assert file.closed


def test_read_incremental(sample_file: Path) -> None:
    """Read the contents of a file incrementally."""
    read_count = 0
    buffer = StringIO()
    with open(sample_file) as file:
        while content := file.read(10):  # Empty string is a falsy value
            buffer.write(content)
            read_count += 1

    assert buffer.getvalue() == SAMPLE_CONTENT
    assert read_count == 3


def test_read_file_line(sample_file: Path) -> None:
    """Read file line by line."""
    lines_readline: List[str] = []
    with open(sample_file) as file:
        while line_readline := file.readline():
            lines_readline.append(line_readline)

    assert (length := len(lines_readline)) == 4
    assert lines_readline[length - 1] == "line three\n"
    assert "".join(lines_readline) == SAMPLE_CONTENT

    lines_for: List[str] = []
    with open(sample_file) as file2:
        for line_for in file2:
            lines_for.append(line_for)
    assert lines_for == lines_readline


def test_read_file_to_list(sample_file: Path) -> None:
    """Read all lines in a file into a list using `list()` and `readlines()`."""
    with open(sample_file) as file:
        lines_list: List[str] = list(file)
    assert "".join(lines_list) == SAMPLE_CONTENT

    with open(sample_file) as file2:
        lines_readlines: List[str] = file2.readlines()
    assert lines_readlines == lines_list


def test_write_file(tmp_path: Path) -> None:
    """Write strings to a file.

    Opens the file with write, append and read modes.
    """
    output: Path = tmp_path.joinpath("c07_write.txt")

    with open(output, "w") as file_write:
        assert file_write.write("test line 1\n") == 12

    with open(output, "a") as file_append:
        assert file_append.write(str(("test line", 2))) == 16

    with open(output, "r") as file_read:
        assert file_read.read() == "test line 1\n('test line', 2)"


def test_write_lines(tmp_path: Path) -> None:
    """Write list of text to a file."""
    output: Path = tmp_path.joinpath("c07_writelines.txt")

    with open(output, "w") as file:
        file.writelines(["test line 1\n", str(("test line", 2))])

    with open(output) as file_read:
        assert file_read.read() == "test line 1\n('test line', 2)"
