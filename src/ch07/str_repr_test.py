"""Demonstrate `str()` and `repr()`."""

from _pytest.capture import CaptureFixture


def test_str_repr_string() -> None:
    """`str()` and `repr()` for a string object."""
    some_str = "hello\n"

    assert str(some_str) == "hello\n"
    assert repr(some_str) == "'hello\\n'"
    assert eval(repr(some_str)) == some_str


def test_custom_str_repr(capsys: CaptureFixture) -> None:
    """Custom `__str__()` and `__repr__()`."""

    class SomeObj:
        """Class with custom `__str__()` and `__repr__()`."""

        def __init__(self, value: int) -> None:
            self.value = value

        def __str__(self) -> str:
            return "some_obj<" + str(self.value) + ">"

        def __repr__(self) -> str:
            return "<some_obj: value=" + repr(self.value) + ">"

    some_obj: SomeObj = SomeObj(1)

    assert str(some_obj) == "some_obj<1>"
    assert repr(some_obj) == "<some_obj: value=1>"

    print(some_obj, end="")
    out, err = capsys.readouterr()
    assert out == "some_obj<1>"
