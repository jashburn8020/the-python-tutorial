"""Demonstrate formatted string literals."""

import math
from datetime import datetime
from decimal import Decimal
from typing import Dict, List


def test_conversion_modifiers() -> None:
    """`!s` and `!r` conversions apply `str()` and `repr()`, respectively."""
    animal, name = ("eel", "Bob")
    assert f"The {animal!s}'s name is {name!r}" == "The eel's name is 'Bob'"


def test_format_nested_fields() -> None:
    """Nested fields in formatting.

    Uses width and precision formatting.
    """
    value: Decimal = Decimal("12.34567")
    width: int = 10
    precision: int = 5
    assert f"result: {value:{width}.{precision}}" == "result:     12.346"


def test_format_floating_point_precision() -> None:
    """Precision (`.3`) and fixed-point type (`f`) formatting."""
    assert f"pi is approximately {math.pi:.3f}" == "pi is approximately 3.142"


def test_format_decimal_width() -> None:
    """Width (`10`) and decimal integer type (`d`) formatting.

    Along with fill (`.`) and align (`<` and `>`).
    """
    table: Dict[str, int] = {"Sjoerd": 4127, "Jack": 254098}

    assert f"{'Sjoerd':10} ==> {table['Sjoerd']:10d}" == "Sjoerd     ==>       4127"

    names_phones: List[str] = [
        f"{name + ' ':.<10}{' ' + str(phone):.>10}" for name, phone in table.items()
    ]
    assert names_phones[0] == "Sjoerd ........ 4127"
    assert names_phones[1] == "Jack ........ 254098"


def test_date_format() -> None:
    """Using date format specifier."""
    timestamp: datetime = datetime(2010, 7, 4, 12, 5, 58)
    assert f"{timestamp:%d %B %Y %H:%M:%S}" == "04 July 2010 12:05:58"
