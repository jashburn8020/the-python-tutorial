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
        return f"{self.name} from BaseOne"


class BaseTwo:
    """Multiple inheritance: Second base class"""

    def __init__(self, name):
        self.name = name

    def identify(self):
        """Identify instance name"""
        return f"{self.name} from BaseTwo"

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
    assert derived.identify() == "Derived from BaseOne"
    assert derived.identify_embelished() == "Derived the Great"

# Private variables


class Mapping:  # pylint: disable=too-few-public-methods
    """Name mangling: Calling own method instead of derived class's"""

    def __init__(self, iterable):
        # Name mangling: Can only be accessed externally through _Mapping__items_list.
        self.__items_list = []

        # If we don't use the private copy here, when subclassed by MappingSubclass, we'll get:
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

# Odds and ends


def test_struct():
    """A data type similar to the Pascal “record” or C “struct”, bundling together a few named data
    items"""
    class Employee:  # pylint: disable=too-few-public-methods
        """Empty class definition to emulate a struct."""

    john = Employee()  # An empty record
    # pylint: disable=attribute-defined-outside-init
    john.name = "John Doe"
    john.dept = "IT"

    assert john.__dict__ == {"name": "John Doe", "dept": "IT"}


class Engine:
    """Engine that can be turned on and off"""

    def turn_on(self):  # pylint: disable=missing-docstring, no-self-use
        return "vroom"

    def turn_off(self):  # pylint: disable=missing-docstring, no-self-use
        return "hiss"


class LightBulb:
    """Light bulb that can be turned on and smashed"""

    def turn_on(self):  # pylint: disable=missing-docstring, no-self-use
        return "let there be light"

    def smash(self):  # pylint: disable=missing-docstring, no-self-use
        return "fizz"


class Car:  # pylint: disable=too-few-public-methods
    """A car that uses an engine, but can take in anything that implements turn_on()"""

    def __init__(self, engine):
        self.engine = engine

    def run(self):
        """Run anything that implements turn_on()"""
        return self.engine.turn_on()


def test_duck_typing():
    """A piece of Python code that expects a particular abstract data type can often be passed a
    class that emulates the methods of that data type instead."""
    car_engine = Car(Engine())
    assert car_engine.run() == "vroom"

    car_bulb = Car(LightBulb())
    assert car_bulb.run() == "let there be light"

# Iterators


def test_iterator():
    """Implementing a custom iterator

    Behind the scenes of a for statement: The for statement calls iter() on the container object.
    The function returns an iterator object that defines the method __next__(), which accesses
    elements in the container one at a time. When there are no more elements, __next__() raises a
    StopIteration exception which tells the for loop to terminate."""

    class Reverse:
        """Container that iterates iterables in reverse"""

        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __next__(self):
            """The next() built-in function calls this method."""
            if self.index <= 0:
                raise StopIteration()
            self.index -= 1
            return self.data[self.index]

        def __iter__(self):
            """The iter() built-in function calls this method. The return type must define the
            __next__() method."""
            return self

    rev_nums = Reverse((1, 2, 3))
    assert [num for num in rev_nums] == [3, 2, 1]


def test_generators():
    """Generators are used for creating iterators. They are written like regular functions but use
    the yield statement whenever they want to return data. Each time next() is called on it, the
    generator resumes where it left off (it remembers all the data values and which statement was
    last executed).

    Key features:
    - generators are compact - __iter__() and __next__() methods are created automatically
    - local variables and execution state such as self.index and self.data are automatically saved
    between calls
    - when generators terminate, they automatically raise StopIteration"""

    def reverse(data):
        for index in range(len(data) - 1, -1, -1):
            yield data[index]

    # One way to use reverse()
    assert "".join(reverse("golf")) == "flog"

    # Another way to use reverse()
    reversed_str = ""
    for char in reverse("golf"):
        # pylint: disable=consider-using-join
        reversed_str += char
    assert reversed_str == "flog"


def test_generator_expressions():
    """Some simple generators can be coded succinctly as expressions using a syntax similar to list
    comprehensions but with parentheses instead of square brackets. These expressions are designed
    for situations where the generator is used right away by an enclosing function. Generator
    expressions are more compact but less versatile than full generator definitions, and tend to be
    more memory friendly than equivalent list comprehensions."""

    assert sum(i * i for i in range(10)) == 285

    data = "golf"
    assert "".join(data[index] for index in range(len(data) - 1, -1, -1)) == "flog"
