#!/usr/bin/pytest-3
"""
Classes
https://docs.python.org/3/tutorial/classes.html
"""
import pytest


def test_scope():
    """How to reference the different scopes and namespaces, and how global and nonlocal affect
    variable binding"""
    def do_local():
        # pylint: disable=redefined-outer-name
        # Redefines name from outer scope (global spam)
        spam = "local spam"
        assert spam  # workaround to suppress pyflakes warning that spam is unused - I know!

    def do_nonlocal():
        # pylint: disable=redefined-outer-name
        # Redefines name from outer scope (global spam)
        # nonlocal indicates that spam lives in an enclosing scope and should be rebound there.
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        # pylint: disable=invalid-name, global-variable-undefined
        # invalid-name: Constant name "spam" doesn't conform to UPPER_CASE naming style
        # global-variable-undefined: Global variable "spam" undefined at the module level
        # global indicates that spam lives in the global scope and should be rebound there.
        global spam
        spam = "global spam"

    # pylint: disable=redefined-outer-name
    spam = "test spam"

    do_local()
    assert spam == "test spam"

    do_nonlocal()
    assert spam == "nonlocal spam"

    do_global()
    assert spam == "nonlocal spam"


with pytest.raises(NameError, match="name 'spam' is not defined"):
    assert spam == "global spam"

# spam defined as global by do_global()
test_scope()
assert spam == "global spam"


class Dog:
    """Demo class"""
    dog_tricks = []

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        """Add a trick to the instance variable"""
        self.tricks.append(trick)

    def get_name(self):
        """Get the name instance variable"""
        return self.name


def test_data_attributes():
    """Data attributes need not be declared; like local variables, they spring into existence when
    they are first assigned to."""
    fido = Dog("Fido")
    assert fido.get_name() == "Fido"
    assert fido.name == fido.get_name()

    # pylint: disable=attribute-defined-outside-init
    fido.powers = []
    powers = fido.powers
    powers.append("fly")
    assert fido.powers == ["fly"]

    del fido.powers
    with pytest.raises(AttributeError, match="'Dog' object has no attribute 'powers'"):
        print(fido.powers)


def test_class_instance_variables():
    """Instance variables are for data unique to each instance, and class variables are for
    attributes and methods shared by all instances of the class."""
    fido = Dog("Fido")
    dido = Dog("Dido")

    Dog.dog_tricks.append("drool")
    fido.dog_tricks.append("roll over")
    dido.dog_tricks.append("play dead")
    assert fido.dog_tricks == ["drool", "roll over", "play dead"]

    fido.add_trick("stand")
    dido.add_trick("sit")
    assert dido.tricks == ["sit"]


def test_method_objects():
    """Method objects can be stored away and called at a later time."""
    fido = Dog("Fido")
    name = fido.get_name
    assert name() == "Fido"
    assert fido.get_name() == Dog.get_name(fido)


def add_power(self, power):
    """Function defined outside class."""
    if not hasattr(self, "power"):
        self.powers = []
    self.powers.append(power)


def test_add_function_to_class():
    """It is not necessary that the function definition is textually enclosed in the class
    definition: assigning a function object to a local variable in the class is also ok."""
    Dog.add_power = add_power
    fido = Dog("Fido")
    fido.add_power("swim")
    assert fido.powers == ["swim"]
    with pytest.raises(AttributeError, match="type object 'Dog' has no attribute 'powers'"):
        # pylint: disable=no-member
        print(Dog.powers)

    del Dog.add_power
