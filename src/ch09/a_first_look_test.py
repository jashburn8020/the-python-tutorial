"""A First Look at Classes."""

from typing import Generic, List, TypeVar

import pytest


class Greeting:
    """A simple example class."""

    def __init__(self, message: str) -> None:
        """Customize an instance to a specific initial state."""
        self.msg = message

    def greet(self) -> str:
        return self.msg


def test_data_attribute() -> None:
    """Data attributes."""
    greeting = Greeting("hello")

    greeting.counter = 1
    greeting.counter += 1
    assert greeting.counter == 2

    del greeting.counter
    with pytest.raises(
        AttributeError, match="'Greeting' object has no attribute 'counter'"
    ):
        print(greeting.counter)


def test_method_object() -> None:
    """Method objects."""
    greeting = Greeting("hello")

    # Store method object to be called at a later time.
    method_obj = greeting.greet
    assert method_obj() == "hello"

    assert greeting.greet() == Greeting.greet(greeting)


class Dog:

    shared_tricks: List[str] = []  # Mistaken use of a class variable

    def __init__(self, name: str) -> None:
        self.name = name
        self.tricks: List[str] = []

    def add_shared_trick(self, trick: str) -> None:
        """Add trick to class variable - mistake."""
        self.shared_tricks.append(trick)

    def add_trick(self, trick: str) -> None:
        """Add trick to instance variable."""
        self.tricks.append(trick)


def test_class_instance_variables() -> None:
    """Class and instance variables."""
    fido = Dog("Fido")
    dido = Dog("Dido")

    fido.add_shared_trick("roll over")
    dido.add_shared_trick("play dead")
    assert fido.shared_tricks == dido.shared_tricks == ["roll over", "play dead"]

    fido.add_trick("roll over")
    dido.add_trick("play dead")
    assert fido.tricks == ["roll over"]
    assert dido.tricks == ["play dead"]


def add_power(self: Dog, power: str) -> None:
    """Define a function outside the class."""
    if not hasattr(self, "power"):
        self.powers = []
    self.powers.append(power)


def test_add_function_to_class() -> None:
    """Assign a function object to a local variable in a class."""
    Dog.add_power = add_power

    fido = Dog("Fido")
    fido.add_power("drool")
    assert fido.powers == ["drool"]

    with pytest.raises(
        AttributeError, match="type object 'Dog' has no attribute 'powers'"
    ):
        # `powers` is an instance variable, not a class variable.
        print(Dog.powers)


T = TypeVar("T")


class Bag(Generic[T]):
    def __init__(self) -> None:
        self.data: List[T] = []

    def add(self, value: T) -> None:
        """Add a value to the bag."""
        self.data.append(value)

    def addtwice(self, value: T) -> None:
        """Add a value to the bag, twice, by using `self`'s method attribute."""
        self.add(value)
        self.add(value)


def test_calling_other_methods() -> None:
    """Calling other methods by using method attributes of the `self` argument."""
    bag = Bag[str]()
    bag.addtwice("apple")

    assert bag.data == ["apple", "apple"]
