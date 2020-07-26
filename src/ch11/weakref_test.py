"""Using `weakref` to create a cache."""

import gc
from weakref import WeakValueDictionary

import pytest


def test_weakref() -> None:
    """Use a `WeakValueDictionary` to cache large object."""

    class BigImage:
        """Dummy class to simulate a large object."""

        def __init__(self, value: int) -> None:
            self.value = value

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, BigImage):
                return NotImplemented

            return self.value == other.value

    big_image = BigImage(10)  # Create a reference
    weak_dict = WeakValueDictionary()
    weak_dict["big image"] = big_image

    gc.collect()
    assert weak_dict["big image"] is big_image

    del big_image
    gc.collect()
    with pytest.raises(KeyError):
        assert weak_dict["big image"]
