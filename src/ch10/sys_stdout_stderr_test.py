"""`sys` module's `stdout` and `stderr`."""

import sys

from _pytest.capture import CaptureFixture


def test_write_stdout_stderr(capsys: CaptureFixture) -> None:
    """Write to standard out and error."""
    sys.stdout.write("standard out")
    sys.stderr.write("standard error")

    out, err = capsys.readouterr()
    assert out == "standard out"
    assert err == "standard error"


def test_print_stdout_stderr(capsys: CaptureFixture) -> None:
    """Print to standard out and error."""
    print("standard out")
    print("standard error", file=sys.stderr)

    out, err = capsys.readouterr()
    assert out == "standard out\n"
    assert err == "standard error\n"
