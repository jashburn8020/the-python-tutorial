"""Manual string formatting."""

from typing import List


def test_rjust() -> None:
    """Right-justifying a string."""
    squares: List[str] = [
        str(x).rjust(2) + " " + str(x * x).rjust(3) for x in range(1, 5)
    ]
    assert squares[0] == " 1   1"
    assert squares[1] == " 2   4"
    assert squares[2] == " 3   9"
    assert squares[3] == " 4  16"


def test_zfill() -> None:
    """Zero-fill a string."""
    assert "3.14".zfill(6) == "003.14"
    assert "-3.14".zfill(6) == "-03.14"
