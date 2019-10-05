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
    # Class variable
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

# Inheritance


class Person:  # pylint: disable=too-few-public-methods
    """Base class"""

    def __init__(self, name):
        self.name = name

    def introduce_self(self):
        """Get self introduction"""
        return f"Hi, I'm {self.name}"


class Student(Person):
    """Derived class"""

    def __init__(self, name, graduation_year):
        """Can be omitted if __init__ doesn't do anything different from base class's."""
        super().__init__(name)
        self.year = graduation_year

    def change_name(self, name):
        """Change the name that is set via the constructor."""
        self.name = name

    def introduce_self(self):
        """Override base class method."""
        return f"{super().introduce_self()} of class {self.year}"


def test_inheritance():
    """Single inheritance"""
    student = Student("Adamu", "2000")
    student.change_name("Bishara")
    assert student.introduce_self() == "Hi, I'm Bishara of class 2000"


class BaseOne:  # pylint: disable=too-few-public-methods
    """Multiple inheritance: First base class"""

    def __init__(self, name):
        self.name = name

    def identify(self):
        """Identify instance name"""
        return f"{self.name} of BaseOne"


class BaseTwo:
    """Multiple inheritance: Second base class"""

    def __init__(self, name):
        self.name = name

    def identify(self):
        """Identify instance name"""
        return f"{self.name} of BaseTwo"

    def identify_embelished(self):
        """Identify instance with embelishment"""
        return f"{self.name} the Great"


def test_multiple_inheritance():
    """Multiple inheritance: Search for attributes inherited from a parent class as depth-first,
    left-to-right, not searching twice in the same class where there is an overlap in the
    hierarchy."""

    class DerivedClass(BaseOne, BaseTwo):
        """Derived class demonstrating attributes search order"""

    derived = DerivedClass("Derived")
    assert derived.identify() == "Derived of BaseOne"
    assert derived.identify_embelished() == "Derived the Great"


class Mapping:  # pylint: disable=too-few-public-methods
    """Name mangling: Calling own method instead of derived class's"""

    def __init__(self, iterable):
        # Name mangling: Can only be accessed externally through _Mapping__items_list.
        self.__items_list = []

        # If we don't use the private copy here, we'll get:
        # TypeError: update() missing 1 required positional argument: 'values'
        self.__update(iterable)

    def update(self, iterable):
        """Append instance iterable with values from argument"""
        for item in iterable:
            self.__items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):  # pylint: disable=too-few-public-methods
    """Name mangling: Derived class"""

    def update(self, keys, values):  # pylint: disable=arguments-differ
        """Append iterables mapped as tuples to instance iterable"""
        for item in zip(keys, values):
            self._Mapping__items_list.append(item)  # pylint: disable=no-member


def test_private_variables():
    """Private variables don't exist in Python. However, there is a convention: a name prefixed
    with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it
    is a function, a method or a data member). It should be considered an implementation detail and
    subject to change without notice.

    Name mangling: Any identifier of the form __spam (at least two leading underscores, at most one
    trailing underscore) is textually replaced with _classname__spam"""
    mapping = MappingSubclass([1, 2])
    mapping.update((3, 5), (4, 6))
    # pylint: disable=no-member, protected-access
    with pytest.raises(AttributeError):
        assert mapping.__items_list
    assert mapping._Mapping__items_list == [1, 2, (3, 4), (5, 6)]
