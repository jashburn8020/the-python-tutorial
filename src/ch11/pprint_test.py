"""Output formatting using `pprint`."""

from io import StringIO
import pprint
import json
from pathlib import Path
from _pytest.capture import CaptureFixture


def test_pp(capsys: CaptureFixture) -> None:
    """Using the shortcut `pp` function."""
    colours = [["black", "cyan"], "white", ["green", "red", ["blue", "brown"]]]

    pprint.pp(colours)
    out, err = capsys.readouterr()
    assert out == "[['black', 'cyan'], 'white', ['green', 'red', ['blue', 'brown']]]\n"

    pprint.pp(colours, indent=4, width=30, depth=2)
    out, err = capsys.readouterr()
    assert (
        out
        == """\
[   ['black', 'cyan'],
    'white',
    ['green', 'red', [...]]]\n"""
    )


def test_pprint_pformat(capsys: CaptureFixture) -> None:
    """Using the shortcut pprint and pformat functions."""
    colours = [["black", "cyan"], "white", ["green", "red", ["blue", "brown"]]]

    pprint.pprint(colours)
    out, err = capsys.readouterr()
    assert out == "[['black', 'cyan'], 'white', ['green', 'red', ['blue', 'brown']]]\n"

    output = StringIO()
    pprint.pprint(colours, stream=output, indent=4, width=30, depth=2)
    pprint_output = output.getvalue()
    assert (
        pprint_output
        == """\
[   ['black', 'cyan'],
    'white',
    ['green', 'red', [...]]]\n"""
    )

    assert pprint.pformat(colours, indent=4, width=30, depth=2) == pprint_output.strip()


def test_pretty_printer() -> None:
    """Using `PrettyPrinter` object and `pformat()` instance method."""
    json_path = Path(__file__).parent.joinpath("pprint.json")
    with open(json_path) as json_file:
        project_info = json.load(json_file)

    printer = pprint.PrettyPrinter(indent=2, width=60, depth=2)
    assert (
        printer.pformat(project_info)
        == r"""{ 'info': { 'author': 'A. Random Developer',
            'classifiers': [...],
            'description': 'A sample Python project\n'
                           '=======================\n'
                           '\n'
                           'This is the description file '
                           'for the project.',
            'name': 'sampleproject'},
  'last_serial': 7562906}"""
    )
