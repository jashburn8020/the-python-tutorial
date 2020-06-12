"""Sets."""

from typing import List, Set

import pytest


def test_construct_set() -> None:
    """Construct sets."""
    numbers: Set[int] = set([1, 2, 1, 2])
    assert numbers == {1, 2}

    letters: Set[str] = set("abracadabra")
    assert letters == {"a", "b", "c", "d", "r"}

    letters_braces = {"abracadabra"}
    assert letters_braces == {"abracadabra"}

    with pytest.raises(TypeError) as ex_info:
        invalid_set = {[1, 2]}
    assert "unhashable type" in str(ex_info.value)


def test_add_remove() -> None:
    """Some set features."""
    some_set: Set[int] = set()
    assert not some_set

    some_set.add(1)
    some_set.add(2)
    assert some_set == {1, 2}
    assert some_set == {2, 1}

    some_set.update((2, 3))
    assert some_set == {1, 2, 3}

    some_set.remove(2)
    assert 2 not in some_set

    with pytest.raises(KeyError):
        some_set.remove(2)

    # Similar to remove(), but does nothing if the element is absent
    some_set.discard(2)
    assert some_set == {1, 3}


def test_set_comprehension() -> None:
    """Set comprehension."""
    assert {x for x in "abracadabra" if x not in "abc"} == {"d", "r"}


def test_maths_operations() -> None:
    """Some mathematical operations."""
    set_one: Set[str] = {"a", "b", "c"}
    set_two: Set[str] = set("cde")
    str_two: str = "cde"

    # Difference
    assert set_one - set_two == {"a", "b"}
    assert set_one.difference(str_two) == {"a", "b"}

    # Symmetric difference
    assert set_one ^ set_two == {"a", "b", "d", "e"}
    assert set_one.symmetric_difference(str_two) == {"a", "b", "d", "e"}

    # Union
    assert set_one | set_two == {"a", "b", "c", "d", "e"}
    assert set_one.union(str_two) == {"a", "b", "c", "d", "e"}

    # Intersection
    assert set_one & set_two == {"c"}
    assert set_one.intersection(str_two) == {"c"}


def test_maths_subset() -> None:
    """Subset operations."""
    set_three: Set[int] = {1, 2, 3}
    list_three: List[int] = [1, 2, 3]
    set_four: Set[int] = {1, 2, 3, 4, 5}
    list_four: List[int] = [1, 2, 3, 4, 5]

    # Subset
    assert set_three <= set_four
    assert set_three <= set(list_three)
    assert set_three.issubset(list_four)
    # Proper subset
    assert set_three < set_four
    assert not set_three < set(list_three)


def test_maths_disjoint() -> None:
    """Disjoint operations."""
    set_five: Set[int] = {1, 2, 3}
    set_six: Set[int] = {4, 5, 6}

    assert set_five.isdisjoint(set_six)
    assert set_five & set_six == set()
    assert set_five ^ set_six == set_five | set_six
