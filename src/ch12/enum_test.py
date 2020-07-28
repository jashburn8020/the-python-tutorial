"""Support for enumerations."""

from enum import Enum, IntEnum, auto
from typing import List

import pytest


class Color(Enum):
    """Colour enumeration."""

    RED = 1
    GREEN = 2
    BLUE = 3


def test_create() -> None:
    """Create an enum."""
    assert str(Color.RED) == "Color.RED"
    assert repr(Color.GREEN) == "<Color.GREEN: 2>"
    assert isinstance(Color.BLUE, Color)
    assert Color.RED.name == "RED"
    assert Color.GREEN.value == 2


def test_iteration() -> None:
    """Iterate an enum."""
    colors = [(color.name, color.value) for color in Color]
    assert colors == [("RED", 1), ("GREEN", 2), ("BLUE", 3)]

    assert list(Color) == [Color.RED, Color.GREEN, Color.BLUE]


def test_comparison() -> None:
    """Compare enum members."""
    assert Color.RED is Color.RED
    assert Color.GREEN == Color.GREEN

    with pytest.raises(TypeError, match="not supported"):
        Color.BLUE > Color.GREEN


def test_comparison_intenum() -> None:
    """Compare `IntEnum` members."""

    class Shape(IntEnum):
        """Shape enumeration."""

        CIRCLE = 0
        SQUARE = 4
        TRIANGLE = 3

    assert Shape.CIRCLE < Shape.TRIANGLE
    assert Shape.SQUARE > Shape.TRIANGLE

    assert sorted(Shape) == [Shape.CIRCLE, Shape.TRIANGLE, Shape.SQUARE]


def test_enum_alias() -> None:
    """Enum member alias - enum members with the same value."""

    class Shape(Enum):
        """Shape enumeration with alias."""

        CIRCLE = 0
        ELLIPSE = 1
        OVAL = 2
        EGG_SHAPE = 2

    assert Shape.OVAL is Shape.EGG_SHAPE
    assert Shape.OVAL == Shape.EGG_SHAPE
    assert [shape.name for shape in Shape] == ["CIRCLE", "ELLIPSE", "OVAL"]


def test_auto_values() -> None:
    """Generate enum values automatically."""

    class Shape(Enum):
        """Shape enumeration with auto-generated values."""

        CIRCLE = auto()
        ELLIPSE = auto()
        OVAL = auto()

    shapes = [(shape.name, shape.value) for shape in Shape]
    assert shapes == [("CIRCLE", 1), ("ELLIPSE", 2), ("OVAL", 3)]


def test_programmatic_enums() -> None:
    """Create enums programmatically."""
    PrimaryColor = Enum("PrimaryColor", "YELLOW RED BLUE")
    SecondaryColor = Enum("SecondaryColor", "ORANGE, GREEN, PURPLE", start=4)
    TertiaryColor = Enum("TertiaryColor", [("CITRON", 7), ("RUSSET", 8), ("BUFF", 9)])
    QuaternaryColor = Enum("QuaternaryColor", {"PLUM": 10, "OLIVE": 11, "SAGE": 12})

    assert PrimaryColor.RED.value == 2
    assert SecondaryColor.GREEN.value == 5
    assert [color.value for color in TertiaryColor] == [7, 8, 9]
    assert [color.name for color in QuaternaryColor] == ["PLUM", "OLIVE", "SAGE"]


def test_nonint_member_values() -> None:
    """Create enums with non-integer member values.
    
    Also define attributes and method.
    """

    class BugStatus(Enum):
        """Bug status and its transition."""

        NEW = (50, ["INVALID", "IN_PROGRESS"])
        INVALID = (40, ["NEW"])
        IN_PROGRESS = (30, ["NEW", "FIX_COMMITTED"])
        FIX_COMMITTED = (20, ["IN_PROGRESS", "FIX_RELEASED"])
        FIX_RELEASED = (10, ["NEW"])

        def __init__(self, num: int, transitions: List[str]) -> None:
            self.num = num
            self.transitions = transitions

        def can_transition(self, new_state: "BugStatus") -> bool:
            """Return `True` if this status can transition to the specified status."""
            return new_state.name in self.transitions

    assert BugStatus.IN_PROGRESS.value == (30, ["NEW", "FIX_COMMITTED"])
    assert BugStatus.IN_PROGRESS.num == 30  # custom attribute
    assert BugStatus.IN_PROGRESS.can_transition(BugStatus.FIX_COMMITTED)
    assert not BugStatus.IN_PROGRESS.can_transition(BugStatus.INVALID)
