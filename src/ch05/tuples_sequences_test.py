"""Tuples and Sequences."""

from typing import List

import pytest


def test_construct_tuple() -> None:
    """Construct tuples."""
    some_tuple = ()
    # PEP 8: For sequences, (strings, lists, tuples), use the fact that empty sequences
    # are false
    assert not some_tuple

    single_elem_tuple = (1,)
    assert len(single_elem_tuple) == 1

    assert tuple() == ()
    assert tuple("abc") == ("a", "b", "c")
    assert tuple([1, 2, 3]) == (1, 2, 3)


def test_tuple_packing_sequence_unpacking() -> None:
    """Tuple packing and sequence unpacking - the reverse.

    Sequence unpacking works for any sequence but not `str`.
    """
    # Black fails to reformat when Tuple type hint is included...
    # packed_tuple: Tuple[int, int, str] = 1, 2, "c"
    packed_tuple = 1, 2, "c"
    # Unpack
    one, two, three = packed_tuple
    assert one == 1 and two == 2 and three == "c"

    # Unpack list
    some_list: List[int] = [1, 2]
    elem_one, elem_two = some_list
    assert elem_one == 1 and elem_two == 2


def test_tuple_features() -> None:
    """More about tuples."""
    first_tuple = 1, 2, 3
    nested_tuple = first_tuple, 4, (5, 6)
    # Access by indexing
    assert nested_tuple[0] == (1, 2, 3)
    assert nested_tuple[2][0] == 5

    # Tuples are immutable
    with pytest.raises(TypeError):
        first_tuple[0] = 0
