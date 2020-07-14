"""Mathematics."""

import math
import random
import statistics


def test_math() -> None:
    """The `math` module."""
    assert round(math.cos(math.pi / 3), 5) == round(math.sin(math.pi / 6), 5) == 0.5
    assert math.log10(100) == 2


def test_random() -> None:
    """The `random` module."""
    fruits = ["apple", "banana", "cherry"]
    assert random.choice(fruits) in fruits

    assert random.randint(1, 5) in [1, 2, 3, 4, 5]


def test_statistics() -> None:
    """The `statistics` module."""
    data = [2, 2, 3, 4, 5]
    assert statistics.mean(data) == 3.2
    assert statistics.median(data) == 3
    assert statistics.mode(data) == 2
