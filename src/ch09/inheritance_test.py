"""Inheritance."""


class Person:
    """Base class."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a greeting."""
        return "Hi!"

    def introduce_self(self) -> str:
        """Get self introduction."""
        greeting = self.greet()  # May end up calling the method in a derived class.
        return f"{greeting} I'm {self.name}"


class Student(Person):
    """Derived class."""

    def __init__(self, name: str, graduation_year: int) -> None:
        super().__init__(name)
        self.year = graduation_year

    def change_name(self, name: str) -> None:
        """Change the name that is set via the constructor."""
        self.name = name

    def greet(self) -> str:
        """Return a different greeting."""
        return "Hello!"

    def introduce_self(self) -> str:
        """Override base class method."""
        return f"{super().introduce_self()} of class {self.year!s}"


def test_inheritance() -> None:
    """Single inheritance."""
    adamu = Person("Adamu")
    assert adamu.introduce_self() == "Hi! I'm Adamu"

    bishara = Student("Adamu", 2000)
    bishara.change_name("Bishara")
    assert bishara.introduce_self() == "Hello! I'm Bishara of class 2000"


def test_isinstance() -> None:
    """Check an instance's type."""
    student = Student("student", 2000)
    assert isinstance(student, Person)
    assert isinstance(student, Student)


def test_issubclass() -> None:
    """Check class inheritance."""
    assert issubclass(Student, Person)
    assert issubclass(Student, Student)
