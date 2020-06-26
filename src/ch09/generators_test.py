"""Generators."""

from pathlib import Path
from typing import Generator, List, NamedTuple, Sequence, Set, Tuple, TypeVar

import pytest

T = TypeVar("T")


def reverse(data: Sequence[T]) -> Generator[T, None, None]:
    """Return a simple generator that only yields values in reverse."""
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


def test_generator_for() -> None:
    """Iterating through a generator in a `for` loop."""
    reversed_str: List[str] = []
    for char in reverse("golf"):
        reversed_str.append(char)
    assert "".join(reversed_str) == "flog"

    assert "".join(reverse("golf")) == "flog"


def test_generator_manual() -> None:
    """Iterating through a generator manually."""
    reversed_int: List[int] = []

    generator = reverse([1, 2, 3])
    reversed_int.append(next(generator))
    reversed_int.append(next(generator))
    reversed_int.append(next(generator))

    with pytest.raises(StopIteration):
        next(generator)

    assert reversed_int == [3, 2, 1]


def test_generator_send() -> None:
    """Interact with a generator using its `send()` method."""

    def reverse_send() -> Generator[int, int, str]:
        """Return a generator that produces `int`s in descending order."""
        start = yield 0
        for index in range(start, -1, -1):
            yield index

        return "done"

    reversed_int: List[int] = []

    generator = reverse_send()
    # The first `send()` to start the generator must be a `None`.
    assert generator.send(None) == 0

    reversed_int.append(generator.send(3))
    for num in generator:
        reversed_int.append(num)

    assert reversed_int == [3, 2, 1, 0]


def test_generator_echo() -> None:
    """Generator yield, send and return types."""

    def echo_round() -> Generator[int, float, str]:
        """Round `float` that is sent in to the nearest `int`."""
        sent = yield 0
        while sent >= 0:
            sent = yield round(sent)
        return "Done"

    generator = echo_round()
    assert next(generator) == 0

    assert generator.send(1.1) == 1
    assert generator.send(1.6) == 2

    with pytest.raises(StopIteration) as ex_info:
        generator.send(-1)
    assert "Done" in str(ex_info.value)


def test_generator_expressions() -> None:
    """Generator expression as a succinct form of generator function."""
    data = "golf"
    # This generator expression is essentially the same as the reverse() function above.
    reverse_generator: Generator[str, None, None] = (
        data[i] for i in range(len(data) - 1, -1, -1)
    )

    assert next(reverse_generator) == "f"
    assert next(reverse_generator) == "l"
    assert next(reverse_generator) == "o"
    assert next(reverse_generator) == "g"

    with pytest.raises(StopIteration):
        next(reverse_generator)


def test_gen_expr_maths() -> None:
    """Some mathematical operations implemented with generator expressions."""
    # Sum of squares
    squares_generator: Generator[int, None, None] = (i * i for i in range(10))
    assert sum(squares_generator) == sum((1, 4, 9, 16, 25, 36, 49, 64, 81))

    # Dot product
    x_vector: Tuple[int, int, int] = (1, 3, 5)
    y_vector: Tuple[int, int, int] = (2, 4, 6)
    assert sum(x * y for x, y in zip(x_vector, y_vector)) == 44


def test_gen_expr_unique_words() -> None:
    """Using a generator expression to find unique words in a file."""
    sample_file: Path = Path(__file__).parent.joinpath("sample.txt")
    with open(sample_file) as file:
        unique_words: Set[str] = set(words for line in file for words in line.split())

    assert unique_words == {"line", "one", "two", "three"}


def test_gen_expr_named_tuples() -> None:
    """Using a generator expression with named tuples."""
    Student = NamedTuple("Student", [("gpa", float), ("name", str)])
    graduates: List[Student] = [
        Student(gpa=3.5, name="Tallys"),
        Student(gpa=3.8, name="Kaniya"),
        Student(gpa=3.7, name="Toibe"),
    ]

    valedictorian = max((student.gpa, student.name) for student in graduates)
    assert valedictorian == (3.8, "Kaniya")
