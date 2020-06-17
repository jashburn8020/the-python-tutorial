"""Demonstrate String `format()`."""

import math
from datetime import datetime
from decimal import Decimal
from typing import Dict, List


def test_args_by_position() -> None:
    """Accessing arguments by position."""
    assert "{0}, {1}, {2}".format("a", "b", "c") == "a, b, c"
    assert "{}, {}, {}".format("a", "b", "c") == "a, b, c"
    assert "{2}, {1}, {0}".format("a", "b", "c") == "c, b, a"
    assert "{0}{1}{0}".format("abra", "cad") == "abracadabra"
    # Unpacking argument sequence
    assert "{2}, {1}, {0}".format(*"abc") == "c, b, a"


def test_args_by_name() -> None:
    """Accessing arguments by name."""
    assert "{lat}, {long}".format(lat="37.2N", long="-15.8W") == "37.2N, -15.8W"

    coord: Dict[str, str] = {"lat": "37.2N", "long": "-15.8W"}
    assert "{lat}, {long}".format(**coord) == "37.2N, -15.8W"
    assert "{0[lat]}, {0[long]}".format(coord) == "37.2N, -15.8W"


def test_args_combined() -> None:
    """Accessing arguments by position and name."""
    assert "{}, {other}, {}".format(1, 2, other=3) == "1, 3, 2"


def test_arg_index_attrs() -> None:
    """Accessing argument index and attributes."""
    assert "{0.real}, {0.imag}".format(3 - 5j) == "3.0, -5.0"

    class Point:
        """Point with x-y coordinates."""

        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return "Point({self.x}, {self.y})".format(self=self)

    assert str(Point(3, 4)) == "Point(3, 4)"

    assert "x: {0[0]}, y: {0[1]}".format((3, 4)) == "x: 3, y: 4"


def test_format_nested_fields() -> None:
    """Nested fields in formatting.

    Uses width and precision formatting.
    """
    value: Decimal = Decimal("12.34567")
    width: int = 10
    precision: int = 5
    assert "result: {0:{1}.{2}}".format(value, width, precision) == "result:     12.346"


def test_conversion_modifiers() -> None:
    """`!s` and `!r` conversions apply `str()` and `repr()`, respectively."""
    assert (
        "The {animal!s}'s name is {name!r}".format(animal="eel", name="Bob")
        == "The eel's name is 'Bob'"
    )


def test_format_floating_point_precision() -> None:
    """Precision (`.3`) and fixed-point type (`f`) formatting."""
    assert "pi is approx {pi:.3f}".format(pi=math.pi) == "pi is approx 3.142"


def test_format_decimal_width() -> None:
    """Width (`10`) and decimal integer type (`d`) formatting.

    Along with fill (`.`) and align (`<` and `>`).
    """
    table: Dict[str, int] = {"Sjoerd": 4127, "Jack": 254098}
    names_phones: List[str] = [
        "{:.<10}{:.>10}".format(name + " ", " " + str(phone))
        for name, phone in table.items()
    ]
    assert names_phones[0] == "Sjoerd ........ 4127"
    assert names_phones[1] == "Jack ........ 254098"


def test_date_format() -> None:
    """Using date format specifier."""
    timestamp: datetime = datetime(2010, 7, 4, 12, 5, 58)
    assert "{ts:%d %B %Y %H:%M:%S}".format(ts=timestamp) == "04 July 2010 12:05:58"
