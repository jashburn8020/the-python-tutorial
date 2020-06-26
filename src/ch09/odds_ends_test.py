"""Odds and Ends.

- Struct
- Structural subtyping
"""

from typing import Optional

import pytest
from typing_extensions import Protocol


def test_struct() -> None:
    """An empty class to emulate a struct."""

    class Employee:
        ...

    john = Employee()  # An empty record
    john.name = "John Doe"
    john.dept = "IT"

    assert john.__dict__ == {"name": "John Doe", "dept": "IT"}


def test_structural_subtyping() -> None:
    """Structural subtyping."""

    class SupportsOn(Protocol):
        """A protocol for anything that can be turned on."""

        def turn_on(self) -> str:
            ...

    class Engine:
        """Engine that can be turned on - a structural subtype of `SupportsOn`."""

        def turn_on(self) -> str:
            return "vroom"

    class LightBulb:
        """Light bulb that can be turned on - a structural subtype of `SupportsOn`."""

        def turn_on(self) -> str:
            return "let there be light"

    class Car:
        """A car that can be fitted with anything that implements `turn_on()`."""

        def __init__(self, on_able: SupportsOn) -> None:
            self.on_able = on_able

        def run(self) -> str:
            """Run anything that implements `turn_on()`."""
            return self.on_able.turn_on()

    car_engine = Car(Engine())
    assert car_engine.run() == "vroom"

    car_light = Car(LightBulb())
    assert car_light.run() == "let there be light"


def test_property() -> None:
    """Using `property()` to define a managed attribute."""

    class ManagedProperty:
        """The `name` property is managed."""

        def __init__(self) -> None:
            self._name: Optional[str] = None

        def get_name(self) -> Optional[str]:
            return self._name

        def set_name(self, value: str) -> None:
            self._name = value if value != "Ivan" else "Ivan the Terrible"

        def del_name(self) -> None:
            del self._name

        name = property(get_name, set_name, del_name, "I'm the 'name' property.")

    managed_property = ManagedProperty()
    managed_property.name = "Ivan"
    assert managed_property.name == "Ivan the Terrible"

    del managed_property.name
    with pytest.raises(AttributeError) as ex_info:
        print(managed_property.name)
    assert "has no attribute '_name'" in str(ex_info.value)


def test_read_only_property() -> None:
    """Using `property()` to define a read-only property."""

    class ReadOnlyProperty:
        """The `name` property is read-only."""

        def __init__(self, name: str) -> None:
            self._name = name

        def get_name(self) -> str:
            return self._name + " the Terrible"

        name = property(get_name)

    read_only = ReadOnlyProperty("Ivan")
    assert read_only.name == "Ivan the Terrible"

    with pytest.raises(AttributeError) as ex_info:
        read_only.name = "Henry"
    assert "can't set attribute" in str(ex_info.value)

    with pytest.raises(AttributeError) as ex_info:
        del read_only.name
    assert "can't delete attribute" in str(ex_info.value)


def test_property_decorator() -> None:
    """Using the `@property` decorator to define a managed attribute."""

    class ManagedPropertyDecorator:
        """The `name` property is managed."""

        def __init__(self) -> None:
            self._name: str

        @property
        def name(self) -> str:
            """I'm the `name` property."""
            return self._name

        @name.setter
        def name(self, value: str) -> None:
            self._name = value

        # @name.deleter
        # def name(self) -> None:
        #     del self._name

    decorated_property = ManagedPropertyDecorator()
    decorated_property.name = "Ivan"
    assert decorated_property.name == "Ivan"

    with pytest.raises(AttributeError) as ex_info:
        del decorated_property.name
    assert "can't delete attribute" in str(ex_info.value)
