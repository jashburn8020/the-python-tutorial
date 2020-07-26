"""Tools for working with lists."""

from array import array
from bisect import bisect, bisect_left, insort
from collections import deque
from heapq import heapify, heappop, heappush, heappushpop, nlargest
from math import floor
from typing import Callable, Deque, List, Sequence

import pytest


def test_array() -> None:
    """Use an `array` to store signed `int`s."""
    signed_int_array: array[int] = array("i", [-1, 0, 1])
    assert signed_int_array[1] == 0
    assert sum(signed_int_array) == 0
    assert len(signed_int_array) == 3

    signed_int_array.append(2)
    assert signed_int_array.tolist() == [-1, 0, 1, 2]

    signed_int_array.extend((3, 4))
    assert signed_int_array.tolist() == [-1, 0, 1, 2, 3, 4]

    assert signed_int_array.pop(0) == -1
    assert signed_int_array.tolist() == [0, 1, 2, 3, 4]

    assert signed_int_array[1] == 1

    with pytest.raises(TypeError, match="an integer is required"):
        signed_int_array.insert(1, "a")

    with pytest.raises(
        OverflowError, match="can't convert negative value to unsigned int"
    ):
        array("I", [-1, 0, 1])


def test_deque() -> None:
    """Some operations with `deque`."""
    queue: Deque[str] = deque("bcd", 5)
    queue.append("e")
    queue.appendleft("a")
    assert list(queue) == ["a", "b", "c", "d", "e"]

    queue.append("f")
    assert list(queue) == ["b", "c", "d", "e", "f"]

    assert queue.pop() == "f"
    assert queue.popleft() == "b"
    assert queue[1] == "d"

    queue.clear()
    assert len(queue) == 0
    with pytest.raises(IndexError, match="pop from an empty deque"):
        queue.pop()


def grade(score: int, insert_func: Callable[[Sequence[int], int], int]) -> str:
    """Return a grade for the specified `score` based on the insertion function."""
    breakpoints: Sequence[int] = (60, 70, 80, 90)
    grades: str = "FDCBA"

    index = insert_func(breakpoints, score)
    return grades[index]


def test_bisect_left() -> None:
    """Use `bisect_left()` to locate insertion point in a sorted sequence."""
    sorted_seq = [60, 70, 80, 90]
    assert bisect_left(sorted_seq, 59) == 0
    assert bisect_left(sorted_seq, 91) == 4
    assert bisect_left(sorted_seq, 80) == 2

    assert [grade(score, bisect_left) for score in [59, 91, 80]] == [
        "F",
        "A",
        "C",
    ]


def test_bisect_bisect() -> None:
    """Use `bisect()` to locate insertion point in a sorted sequence."""
    sorted_seq = [60, 70, 80, 90]
    assert bisect(sorted_seq, 59) == 0
    assert bisect(sorted_seq, 91) == 4
    assert bisect(sorted_seq, 80) == 3

    assert [grade(score, bisect) for score in [59, 91, 80]] == ["F", "A", "B"]


def test_bisect_insort() -> None:
    """Use `insort()` to insert elements whilst maintaining the sequence's sorting."""
    scores = [(200, "tcl"), (400, "lua")]
    insort(scores, (300, "ruby"))
    assert scores == [(200, "tcl"), (300, "ruby"), (400, "lua")]


def assert_heap_elements(heap: List[int]) -> None:
    """Verify that `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]`."""
    max_assert = floor((len(heap) - 2) / 2)
    for k in range(max_assert + 1):
        assert heap[k] <= heap[2 * k + 1]
        if (k * 2 + 2) < len(heap):
            assert heap[k] <= heap[2 * k + 2]


def test_heapq_heapify() -> None:
    """Transform a list into a heap, i.e., rearrange into heap order."""
    data = [1, 3, 5, 2, 7, 4, 6]
    heapify(data)
    assert data == [1, 2, 4, 3, 7, 5, 6]
    assert_heap_elements(data)


def test_heapq_push_pop() -> None:
    """Push and pop to and from a heap."""
    data = [1, 3, 5, 2, 7, 4, 6]
    heapify(data)

    heappush(data, 4)
    assert data == [1, 2, 4, 3, 7, 5, 6, 4]
    assert_heap_elements(data)

    assert heappop(data) == 1
    assert data == [2, 3, 4, 4, 7, 5, 6]
    assert_heap_elements(data)

    assert heappushpop(data, 5) == 2
    assert data == [3, 4, 4, 5, 7, 5, 6]
    assert_heap_elements(data)

    non_heap = [1, 3, 5, 2, 7, 4, 6]
    heappush(non_heap, 4)  # works only with a heap, not any arbitrary list
    with pytest.raises(AssertionError):
        assert_heap_elements(non_heap)


def test_heapq_nlargest() -> None:
    """Get the `n` largest elements."""
    data = [1, 3, 5, 2, 7, 4, 6]
    assert nlargest(6, data) == [7, 6, 5, 4, 3, 2]
