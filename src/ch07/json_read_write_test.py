"""Saving Structured Data with `json`."""

import json
from pathlib import Path
from typing import Any, Dict


def test_list_to_json_str() -> None:
    """Serialize a list to JSON-formatted string."""
    assert json.dumps([1, "simple", "list"]) == '[1, "simple", "list"]'


def test_dict_python_types_to_json_str() -> None:
    """Serialize a `dict` of Python types to JSON-formatted string."""
    python_types: Dict[str, Any] = {
        "dict": {"a": "one", "b": 2},
        "array": [3, 4],
        "tuple": (5, 6),
        "boolean": True,
        "null": None,
    }

    json_val = """\
{
    "dict": {
        "a": "one",
        "b": 2
    },
    "array": [
        3,
        4
    ],
    "tuple": [
        5,
        6
    ],
    "boolean": true,
    "null": null
}"""
    # indent=4 to pretty print
    assert json.dumps(python_types, indent=4) == json_val


def test_dict_to_json_file(tmp_path: Path) -> None:
    """Serialize a `dict` of Python types to a JSON file."""
    output: Path = tmp_path.joinpath("c07_dump.json")
    python_types: Dict[str, Any] = {
        "dict": {"a": "one"},
        "array": [True, False],
        "null": None,
    }

    with open(output, "w") as json_write:
        json.dump(python_types, json_write)

    with open(output, "r") as json_read:
        json_str = json_read.read()
    assert json_str == '{"dict": {"a": "one"}, "array": [true, false], "null": null}'


def test_json_str_to_python_types() -> None:
    """Deserialize a JSON string to Python types."""
    assert json.loads('{"boolean": true, "null": null}') == {
        "boolean": True,
        "null": None,
    }


def test_json_file_to_obj() -> None:
    """Deserialize a JSON file to Python types."""
    sample_file: Path = Path(__file__).parent.joinpath("sample.json")
    python_types: Dict[str, Any] = {
        "dict": {"a": "one", "b": 2},
        "array": [3, 4],
        "tuple": [5, 6],
        "boolean": True,
        "null": None,
    }

    with open(sample_file, "r") as json_file:
        loaded_types = json.load(json_file)
    assert loaded_types == python_types
