"""Using Lists as Stacks and Queues."""

from typing import Deque, List
from collections import deque


def test_list_stack() -> None:
    """Using lists as stacks (LIFO) - append and pop."""
    stack: List[int] = []
    stack.append(1)
    stack.append(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_list_queue_slow() -> None:
    """Using lists as queues (FIFO) - insert, pop.

    Doing inserts or pops from the beginning of a list is slow because all of the other
    elements have to be shifted by one.
    """
    slow_queue: List[int] = []
    slow_queue.append(1)
    slow_queue.append(2)
    assert slow_queue.pop(0) == 1
    assert slow_queue.pop(0) == 2

    slow_queue.insert(0, 1)
    slow_queue.insert(0, 2)
    assert slow_queue.pop() == 1
    assert slow_queue.pop() == 2


def test_list_queue_fast() -> None:
    """Faster queue using a `deque`."""
    fast_queue: Deque[int] = deque([])
    fast_queue.append(1)
    fast_queue.append(2)
    assert fast_queue.popleft() == 1
    assert fast_queue.popleft() == 2
