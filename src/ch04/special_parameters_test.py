"""Using the `/` and `*` special parameters."""

from typing import Tuple

import pytest


def test_standard_args() -> None:
    """Arguments may be passed by position or keyword.

    `/` and `*` are not present in the function definition.
    """

    def standard_args(arg1: int, arg2: int) -> Tuple[int, int]:
        return (arg1, arg2)

    assert standard_args(1, 2) == (1, 2)
    assert standard_args(arg2=2, arg1=1) == (1, 2)


def test_pos_only_args() -> None:
    """Arguments passed in by position only."""

    def pos_only_args(arg1: int, arg2: int, /) -> Tuple[int, int]:
        return (arg1, arg2)

    assert pos_only_args(1, 2) == (1, 2)

    with pytest.raises(TypeError) as ex_info:
        pos_only_args(1, arg2=2)
    assert "some positional-only arguments passed as keyword arguments" in str(
        ex_info.value
    )


def test_kwd_only_args() -> None:
    """Arguments pass in by keywords only."""

    def kwd_only_args(*, arg1: int, arg2: int) -> Tuple[int, int]:
        return (arg1, arg2)

    assert kwd_only_args(arg2=2, arg1=1) == (1, 2)

    with pytest.raises(TypeError) as ex_info:
        kwd_only_args(1, arg2=2)
    assert "takes 0 positional arguments" in str(ex_info.value)


def test_combined_args() -> None:
    """Using both `/` and `*` special parameters."""

    def combined_args(
        pos1: int, /, pos_or_kwd2: int, *, kwd3: int
    ) -> Tuple[int, int, int]:
        return (pos1, pos_or_kwd2, kwd3)

    assert combined_args(1, 2, kwd3=3) == (1, 2, 3)
    assert combined_args(1, pos_or_kwd2=2, kwd3=3) == (1, 2, 3)
    assert combined_args(1, kwd3=3, pos_or_kwd2=2) == (1, 2, 3)

    with pytest.raises(TypeError) as ex_info:
        combined_args(pos_or_kwd2=1, pos1=2, kwd3=3)
    assert "positional-only arguments passed as keyword arguments" in str(ex_info.value)

    with pytest.raises(TypeError) as ex_info:
        combined_args(kwd3=3, pos1=1, pos_or_kwd2=2)
    assert "positional-only arguments passed as keyword arguments" in str(ex_info.value)
