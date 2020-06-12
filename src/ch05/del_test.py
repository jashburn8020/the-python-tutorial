"""The `del` Statement."""

from typing import List


def test_del_list() -> None:
    """Remove element(s) from a list."""
    nums: List[int] = [1, 2, 3, 4, 5]
    del nums[0]
    assert nums == [2, 3, 4, 5]

    del nums[1:3]
    assert nums == [2, 5]

    del nums[:]
    assert nums == []

    # Delete entire variable
    del nums
