"""Demonstrate arbitrary argument lists."""

from typing import Dict, Tuple

from _pytest.capture import CaptureFixture


def test_arbitrary_keyword_arguments() -> None:
    """Arbitrary number of keyword arguments, parameter of the form `**name`."""

    def arbitrary_keyword_arguments(
        first: int, **seconds: int
    ) -> Tuple[int, Dict[str, int]]:
        return (first, seconds.copy())

    first_arg, args_dict = arbitrary_keyword_arguments(1, second=2, third=3)
    assert first_arg == 1

    assert isinstance(args_dict, dict)
    assert len(args_dict) == 2
    assert args_dict["second"] == 2
    assert args_dict["third"] == 3


def test_combined_arbitrary_arguments(capsys: CaptureFixture) -> None:
    """Combining parameters of the form `*name` and `**name`."""

    def print_nvp(
        title: str, *separator_line_chars: str, **name_value_pair: int
    ) -> None:
        """Print name-value pairs to stdout."""
        print(title)
        print("".join(separator_line_chars) * 3)
        for name in name_value_pair:
            print(name, ":", name_value_pair[name])

    print_nvp("Name-Value Pairs", "-", "=", one=1, two=2)

    out, err = capsys.readouterr()
    assert out == "Name-Value Pairs\n-=-=-=\none : 1\ntwo : 2\n"


def test_arbitrary_argument_list() -> None:
    """Arbitrary argument list, parameter of the form `*name`."""

    def arbitrary_argument_list(*args: str, sep: str = " ") -> str:
        """`args` accepts an arbitrary number of arguments.

        It is normally last in the list of formal parameters because it scoops up all
        remaining input arguments, wrapped up in a tuple. Formal parameters that occur
        after `*args` are keyword arguments only.
        """
        return sep.join(args)

    assert arbitrary_argument_list("1", "2", "3", sep=",") == "1,2,3"
