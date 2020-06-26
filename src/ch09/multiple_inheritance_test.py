"""Multiple Inheritance."""

import pytest


class BaseOne:
    """First base class."""

    def __init__(self, name: str) -> None:
        self.name = name

    def identify(self) -> str:
        """Identify instance name."""
        return f"{self.name} from BaseOne"


class BaseTwo:
    """Second base class."""

    def __init__(self, name: str) -> None:
        self.name = name

    def identify(self) -> str:
        """Identify instance name."""
        return f"{self.name} from BaseTwo"

    def identify_embellished(self) -> str:
        """Identify instance with embellishment."""
        # When called from a subclass, `self` is an instance of the subclass.
        return f"{self.identify()} the Great"


def test_multiple_inheritance() -> None:
    """Multiple inheritance - simplest case."""

    class DerivedClass(BaseOne, BaseTwo):
        """Derived class demonstrating attributes search order."""

    derived = DerivedClass("Derived")
    assert derived.identify() == "Derived from BaseOne"
    assert derived.identify_embellished() == "Derived from BaseOne the Great"


class BaseThree:
    """Third base class - problematic."""

    def __init__(self, name: str, embellishment: str) -> None:
        self.name = name
        self.embellishment = embellishment

    def identify(self) -> str:
        """Identify instance name."""
        return f"{self.name} from BaseThree"

    def identify_embellished(self) -> str:
        """Identify instance with embellishment."""
        return f"{self.identify()} the {self.embellishment}"


def test_different_init_signature() -> None:
    """Multiple inheritance - base classes have different `__init__()` signatures."""

    class DerivedOneThree(BaseOne, BaseThree):
        """`BaseOne`'s `__init__()` has 1 parameter, while `BaseThree` has 2."""

    derived_13 = DerivedOneThree("Derived")
    with pytest.raises(AttributeError) as ex_info:
        derived_13.identify_embellished()
    assert "object has no attribute 'embellishment'" in str(ex_info.value)

    class DerivedOneThreeFixed(BaseOne, BaseThree):
        """Fix by explicitly calling `BaseThree`'s `__init__()`."""

        def __init__(self, name: str) -> None:
            super().__init__(name)
            BaseThree.__init__(self, name, "Fixer")
            # The following will no work - `super()` refers to `BaseOne`.
            # super().__init__(name, "Fixer")

    derived_13_fixed = DerivedOneThreeFixed("Derived")
    assert derived_13_fixed.identify_embellished() == "Derived from BaseOne the Fixer"

    assert DerivedOneThreeFixed.__mro__ == (
        DerivedOneThreeFixed,
        BaseOne,
        BaseThree,
        object,
    )
