"""Looping Techniques."""

import math
from typing import Dict, List, Tuple


def test_dict_items() -> None:
    """Looping through a dictionary using `items()`."""
    knights_dict: Dict[str, str] = {"gallahad": "pure", "robin": "brave"}

    knights: List[str] = [
        name.title() + " the " + value.title() for name, value in knights_dict.items()
    ]

    assert knights == ["Gallahad the Pure", "Robin the Brave"]


def test_seq_enumerate() -> None:
    """Looping through a sequence using `enumerate()`."""
    tic_tac_toe: Dict[int, str] = {}

    for index, value in enumerate(["tic", "tac", "toe"], start=1):
        tic_tac_toe[index] = value

    assert tic_tac_toe == {1: "tic", 2: "tac", 3: "toe"}


def test_seqs_zip() -> None:
    """Looping over 2 or more sequences using `zip()`."""
    attrs: List[str] = ["name", "quest", "drink"]
    values: List[str] = ["lancelot", "the holy grail"]
    props: Dict[str, str] = {}

    for attr, value in zip(attrs, values):
        props[attr] = value

    assert props == {"name": "lancelot", "quest": "the holy grail"}


def test_seq_reversed() -> None:
    """Loop over a sequence in reverse using `reversed()`."""
    fruits: List[str] = [
        fruit.upper() for fruit in reversed(["banana", "cherry", "durian"])
    ]
    assert fruits == ["DURIAN", "CHERRY", "BANANA"]


def test_seq_sorted() -> None:
    """Loop over a sequence in sorted order using `sorted()`."""
    fruits_amount: List[Tuple[str, int]] = [("cherry", 4), ("banana", 5), ("durian", 2)]
    assert [
        fruit_name[0]
        for fruit_name in sorted(fruits_amount, key=lambda fruit: fruit[1])
    ] == ["durian", "cherry", "banana",]


def test_changing_list() -> None:
    """Changing a list - often simpler and safer to create a new list."""
    raw_data: List[float] = [56.2, float("NaN"), 51.7, float("NaN"), 47.8]
    filtered_data: List[float] = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)
    assert filtered_data == [56.2, 51.7, 47.8]

    filtered_data_listcomp: List[float] = [
        data for data in raw_data if not math.isnan(data)
    ]
    assert filtered_data_listcomp == filtered_data
