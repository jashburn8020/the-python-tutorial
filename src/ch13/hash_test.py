"""Defining `__hash__` and `__eq__` in objects."""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict


class Colour(Enum):
    """Colour enumeration."""

    RED = auto()
    BLUE = auto()
    GREEN = auto()


def test_default_hash_eq() -> None:
    """Test objects with default `__hash__` and `__eq__` implementations."""

    class DefaultWidget:
        """Does not define `__hash__` and `__eq__`; default implementations are used."""

        def __init__(self, identifier: int, name: str, colour: Colour):
            self.identifier = identifier
            self.name = name
            self.colour = colour

    widget_1 = DefaultWidget(1, "A", Colour.BLUE)
    widget_2 = DefaultWidget(1, "A", Colour.BLUE)
    widget_3 = DefaultWidget(2, "A", Colour.BLUE)

    assert widget_1 != widget_2
    assert hash(widget_1) != hash(widget_2)

    assert widget_1 is not widget_2

    widget_set = {widget_1, widget_2, widget_3}
    assert len(widget_set) != 2

    widget_dict: Dict[DefaultWidget, int] = {}
    widget_dict[widget_1] = 1
    widget_dict[widget_2] = 2
    widget_dict[widget_3] = 3
    assert len(widget_dict) != 2
    assert widget_dict[widget_1] != 2


def test_custom_hash_eq() -> None:
    """Test objects with custom `__hash__` and `__eq__` implementations."""

    class HashEqWidget:
        """Defines `__hash__` and `__eq__`.

        *Not* recommended because the objects are mutable.
        """

        def __init__(self, identifier: int, name: str, colour: Colour):
            self.identifier = identifier
            self.name = name
            self.colour = colour

        def __hash__(self) -> int:
            return hash((self.identifier, self.name, self.colour))

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, HashEqWidget):
                return NotImplemented

            return (
                self.identifier == other.identifier
                and self.name == other.name
                and self.colour == other.colour
            )

    widget_1 = HashEqWidget(1, "A", Colour.BLUE)
    widget_2 = HashEqWidget(1, "A", Colour.BLUE)
    widget_3 = HashEqWidget(2, "A", Colour.BLUE)

    assert widget_1 == widget_2
    assert hash(widget_1) == hash(widget_2)

    # They still are different objects
    assert widget_1 is not widget_2

    widget_set = {widget_1, widget_2, widget_3}
    assert len(widget_set) == 2

    widget_dict: Dict[HashEqWidget, int] = {}
    widget_dict[widget_1] = 1
    widget_dict[widget_2] = 2
    widget_dict[widget_3] = 3
    assert len(widget_dict) == 2
    assert widget_dict[widget_1] == 2


def test_dataclass() -> None:
    """Test `dataclass` objects."""

    @dataclass(eq=True, frozen=True)
    class DataClassWidget:
        """Data class with `eq` and `frozen` set to `True`.

        `__eq__` and `__hash__` are generated. Instances are frozen/immutable and so
        they are safe to be used in hashable collections.
        """

        identifier: int
        name: str
        colour: Colour

    widget_1 = DataClassWidget(1, "A", Colour.BLUE)
    widget_2 = DataClassWidget(1, "A", Colour.BLUE)
    widget_3 = DataClassWidget(2, "A", Colour.BLUE)

    assert widget_1 == widget_2
    assert hash(widget_1) == hash(widget_2)

    # They still are different objects
    assert widget_1 is not widget_2

    widget_set = {widget_1, widget_2, widget_3}
    assert len(widget_set) == 2

    widget_dict: Dict[DataClassWidget, int] = {}
    widget_dict[widget_1] = 1
    widget_dict[widget_2] = 2
    widget_dict[widget_3] = 3
    assert len(widget_dict) == 2
    assert widget_dict[widget_1] == 2
