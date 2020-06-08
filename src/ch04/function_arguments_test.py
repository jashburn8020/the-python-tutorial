"""Demonstrate default arguments and keyword arguments."""

from typing import List, Optional, Union, Tuple

import pytest


def test_default_args() -> None:
    """Default arguments."""

    def default_args(value: Union[int, str], multiplier: int = 2) -> Union[int, str]:
        """If `multiplier` is not provided, the default value will be used.

        Throw `ValueError` if `value` is same as `multiplier`.
        """
        if value == multiplier:
            raise ValueError(f"Value {value} is the same as multiplier {multiplier}")

        return value * multiplier

    assert default_args(5) == 10
    assert default_args("a", 3) == "aaa"

    with pytest.raises(ValueError) as ex_info:
        default_args(5, 5)
    assert "Value 5 is the same as multiplier 5" in str(ex_info.value)


def test_default_value_accumulation() -> None:
    """Default value is evaluated only once.

    With a mutable object, it accumulates arguments passed to it on subsequent calls.
    """

    def mutable_default_value_shared(
        value: int, container: List[int] = []
    ) -> List[int]:
        """`container` default value is a mutable object - AVOID."""
        container.append(value)
        return container

    def mutable_default_value_not_shared(
        value: int, container: Optional[List[int]] = None
    ) -> List[int]:
        """Avoids the default mutable object problem."""
        if container is None:
            container = []
        container.append(value)
        return container

    assert mutable_default_value_shared(1) == [1]
    assert mutable_default_value_shared(2) == [1, 2]

    assert mutable_default_value_not_shared(1) == [1]
    assert mutable_default_value_not_shared(2) == [2]


def test_keyword_arguments() -> None:
    """Keyword arguments are arguments of the form `kwarg=value`."""

    def keyword_arguments(
        first: int, second: int = 2, third: int = 3
    ) -> Tuple[int, int, int]:
        """Accept 1 required argument and 2 optional arguments."""
        return (first, second, third)

    # 1 positional argument
    assert keyword_arguments(10) == (10, 2, 3)
    # 1 keyword argument
    assert keyword_arguments(first=10) == (10, 2, 3)
    # 2 keyword arguments, order unimportant
    assert keyword_arguments(second=20, first=10) == (10, 20, 3)
    # 1 positional argument, 1 keyword argument
    assert keyword_arguments(10, third=30) == (10, 2, 30)
    # Positional argument cannot follow a keyword argument
    # keyword_arguments(second=20, 10)
