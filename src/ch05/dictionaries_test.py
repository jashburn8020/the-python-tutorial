"""Dictionaries."""

from types import MappingProxyType
from typing import Dict, ItemsView, KeysView, ValuesView

import pytest


def test_construct_dictionary() -> None:
    """Construct dictionaries using braces and `dict()`."""
    fruits_braces: Dict[str, int] = {"banana": 5, "cherry": 4, "durian": 2}
    fruits_dict: Dict[str, int] = dict([("banana", 5), ("cherry", 4), ("durian", 2)])
    fruits_kwargs: Dict[str, int] = dict(banana=5, cherry=4, durian=2)

    assert fruits_braces == fruits_dict == fruits_kwargs


def test_dict_comprehension() -> None:
    """Construct dictionaries using dict comprehension."""
    even_power_twos = {even: even ** 2 for even in range(10) if even % 2 == 0}
    assert even_power_twos == {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


def test_store_extract_del() -> None:
    """Store, extract, delete values from a dictionary."""
    fruits: Dict[str, int] = {}
    fruits["banana"] = 5
    assert fruits["banana"] == 5

    del fruits["banana"]
    assert fruits == {}


def test_list_len_key_in() -> None:
    """Get all keys, length of dictionary, and check for a key."""
    fruits: Dict[str, int] = {"cherry": 4, "banana": 5, "durian": 2}

    assert len(fruits) == 3
    assert list(fruits) == ["cherry", "banana", "durian"]
    assert sorted(fruits) == ["banana", "cherry", "durian"]
    assert "banana" in fruits


def test_more_set_get() -> None:
    """More ways to set and get values to/from a dictionary."""
    fruits: Dict[str, int] = {}

    # setdefault()
    value = fruits.setdefault("cherry", 4)
    assert value == 4 and fruits["cherry"] == 4

    value = fruits.setdefault("cherry", 0)
    assert value == 4 and fruits["cherry"] == 4

    # update()
    fruits.update([("durian", 2), ("banana", 5)])

    # get()
    assert fruits.get("elderberry") is None
    assert fruits.get("elderberry", 8) == 8

    # popitem(), pop()
    assert fruits.popitem() == ("banana", 5)
    assert fruits.pop("cherry") == 4
    assert fruits.pop("elderberry", 0) == 0
    with pytest.raises(KeyError):
        fruits.pop("elderberry")

    assert fruits == {"durian": 2}


def test_view_objects() -> None:
    """Operations returning view objects."""
    fruits: Dict[str, int] = {"cherry": 4, "banana": 5, "durian": 2}

    # items()
    fruit_items: ItemsView[str, int] = fruits.items()
    # ItemsView is an iterable - has the __items__ method
    assert list(fruit_items) == [("cherry", 4), ("banana", 5), ("durian", 2)]

    # keys()
    fruit_keys: KeysView[str] = fruits.keys()
    assert list(fruit_keys) == ["cherry", "banana", "durian"]

    # values()
    fruit_values: ValuesView[int] = fruits.values()
    assert list(fruit_values) == [4, 5, 2]
    assert fruit_values != fruits.values()

    # Change a value in the dictionary
    fruits["cherry"] = 14
    assert ("cherry", 14) in fruit_items
    assert 14 in fruit_values

    # Remove an entry in the dictionary
    del fruits["banana"]
    assert len(fruit_items) == 2
    assert ("banana", 5) not in fruit_items
    assert "banana" not in fruit_keys
    assert 5 not in fruit_values

    # Add an entry into the dictionary
    fruits["elderberry"] = 8
    assert len(fruit_items) == 3
    assert ("elderberry", 8) in fruit_items
    assert "elderberry" in fruit_keys
    assert 8 in fruit_values


def test_mappingproxytype() -> None:
    """Read-only view of a `dict`."""
    fruits: Dict[str, int] = {"cherry": 4, "banana": 5, "durian": 2}
    read_only_fruits = MappingProxyType(fruits)

    assert read_only_fruits["durian"] == 2

    with pytest.raises(TypeError) as ex_info:
        read_only_fruits["durian"] = 9
    assert "does not support item assignment" in str(ex_info.value)

    fruits["durian"] = 9
    assert read_only_fruits["durian"] == 9
