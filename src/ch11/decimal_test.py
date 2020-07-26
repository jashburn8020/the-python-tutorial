"""Decimal floating point arithmetic."""

import decimal
from decimal import Decimal


def test_decimal() -> None:
    """Use `decimal` for precise floating point calculations."""
    context = decimal.getcontext()
    assert context.rounding == "ROUND_HALF_EVEN"

    # 0.7 * 1.05 == 0.735
    assert round(0.7 * 1.05, 2) == 0.73
    assert round(Decimal("0.7") * Decimal("1.05"), 2) == Decimal("0.74")

    assert 1.00 % 0.10 == 0.09999999999999995
    assert Decimal("1.00") % Decimal("0.10") == Decimal("0.00")

    assert sum([0.1] * 10) == 0.9999999999999999
    assert sum([Decimal("0.1")] * 10) == Decimal("1.0")
