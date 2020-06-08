"""Referencing and assigning variables - enclosing functions and global."""


def test_enclosing_var() -> None:
    """Referencing and assigning variables of enclosing functions."""
    enclosing_var_ref = "enclosing"
    enclosing_var_assign = "enclosing"

    def ref_assign_enclosing_var() -> None:
        # Variables of enclosing functions can be referenced
        assert enclosing_var_ref == "enclosing"

        # Variables of enclosing functions cannot be assigned unless named in a nonlocal
        # statement
        nonlocal enclosing_var_assign
        enclosing_var_assign = "assigned"

    ref_assign_enclosing_var()
    assert enclosing_var_assign == "assigned"

    def assign_enclosing_var_fail() -> None:
        # Local variable as it is not named in a nonlocal statement
        enclosing_var_assign = "reassigned"

    assign_enclosing_var_fail()
    assert enclosing_var_assign != "reassigned"


GLOBAL_VAR_1 = "global"
GLOBAL_VAR_2 = "global"


def test_global_var() -> None:
    """Referencing and assigning global variables."""

    def ref_assign_global_var() -> None:
        # Global variables can be referenced
        assert GLOBAL_VAR_1 == "global"

        # Global variables cannot be assigned unless named in a global statement
        global GLOBAL_VAR_2
        GLOBAL_VAR_2 = "assigned"

    ref_assign_global_var()
    assert GLOBAL_VAR_2 == "assigned"

    def assign_global_var_fail() -> None:
        # Local variables as it is not named in a global statement
        GLOBAL_VAR_2 = "reassigned"

    assign_global_var_fail()
    assert GLOBAL_VAR_2 != "reassigned"
