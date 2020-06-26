"""Private Variables, and Odds and Ends."""

from typing import Generic, Iterable, List, Tuple, TypeVar

import pytest

T = TypeVar("T")


class Mapping(Generic[T]):
    """Name wrangling applied to class attribute and method."""

    def __init__(self, iterable: Iterable[T]) -> None:
        self.__items_list: List[T] = []
        self.__update(iterable)

    def update(self, iterable: Iterable[T]) -> None:
        for item in iterable:
            self.__items_list.append(item)

    __update = update  # Private copy of original `update()` method


U = TypeVar("U")
V = TypeVar("V")


class MappingSubclass(Mapping[Tuple[U, V]]):
    """Subclass's overridden `update()` doesn't break parent intraclass method call."""

    def update(self, keys: Iterable[U], values: Iterable[V]) -> None:
        """Provide new signature that will break `__init__()` without mangling."""
        super().update(zip(keys, values))


def test_mapping() -> None:
    """Prove parent class works."""
    mapping: Mapping[int] = Mapping((1, 2, 3))
    mapping.update((4, 5, 6))
    assert mapping._Mapping__items_list == [1, 2, 3, 4, 5, 6]


def test_mappingsub() -> None:
    """Subclass overriding method without breaking intraclass method call."""
    mappingsub: MappingSubclass[str, int] = MappingSubclass([("a", 1), ("b", 2)])
    mappingsub.update(("c", "d"), (3, 4))
    assert mappingsub._Mapping__items_list == [("a", 1), ("b", 2), ("c", 3), ("d", 4)]


class MappingBroken(Generic[T]):
    """Name wrangling not applied."""

    def __init__(self, iterable: Iterable[T]) -> None:
        self.__items_list: List[T] = []
        self.update(iterable)

    def update(self, iterable: Iterable[T]) -> None:
        for item in iterable:
            self.__items_list.append(item)


class MappingSubclassBroken(MappingBroken[Tuple[U, V]]):
    """Subclass's overridden `update()` breaks parent intraclass method call."""

    def update(self, keys: Iterable[U], values: Iterable[V]) -> None:
        """Provide new signature that breaks `__init__()`."""
        super().update(zip(keys, values))


def test_mappingsub_broken() -> None:
    """Subclass overriding method breaking intraclass method call."""
    with pytest.raises(TypeError) as ex_info:
        MappingSubclassBroken([("a", 1), ("b", 2)])

    assert "update() missing 1 required positional argument" in str(ex_info.value)
