"""Output formatting using `locale`."""

import locale
from datetime import datetime
from typing import Generator

import pytest


@pytest.fixture(name="zh_cn")
def fixture_zh_cn() -> Generator[None, None, None]:
    """Set current locale to `zh_CN.UTF-8`."""
    locale.setlocale(locale.LC_ALL, ("zh_CN", "UTF-8"))
    yield
    locale.resetlocale()


@pytest.fixture(name="de_de")
def fixture_de_de() -> Generator[None, None, None]:
    """Set current locale to `de_DE.UTF-8`."""
    locale.setlocale(locale.LC_ALL, ("de_DE", "UTF-8"))
    yield
    locale.resetlocale()


def test_number_zh(zh_cn: None) -> None:
    """Format number using the Chinese locale."""
    assert locale.format_string("Int: %d", 1234567, grouping=True) == "Int: 1,234,567"
    assert locale.atoi("1,234,567") == 1234567

    assert (
        locale.format_string("Float: %.2f", 12345.67, grouping=True)
        == "Float: 12,345.67"
    )
    assert locale.atof("12,345.67") == 12345.67


def test_number_de(de_de: None) -> None:
    """Format number using the German locale."""
    assert locale.format_string("Int: %d", 1234567, grouping=True) == "Int: 1.234.567"
    assert locale.atoi("1.234.567") == 1234567

    assert (
        locale.format_string("Float: %.2f", 12345.67, grouping=True)
        == "Float: 12.345,67"
    )
    assert locale.atof("12.345,67") == 12345.67


def test_currency_zh(zh_cn: None) -> None:
    """Format number with currency using the Chinese locale."""
    assert locale.currency(12345.67, grouping=True) == "￥12,345.67"


def test_currency_de(de_de: None) -> None:
    """Format number with currency using the German locale."""
    assert locale.currency(12345.67, grouping=True) == "12.345,67 €"


def test_datetime_zh(zh_cn: None) -> None:
    """Format date and time using the Chinese locale."""
    date_time = datetime(2020, 7, 15, 13, 10, 5)
    assert date_time.strftime("%c") == "2020年07月15日 星期三 13时10分05秒"


def test_datetime_de(de_de: None) -> None:
    """Format date and time using the German locale."""
    date_time = datetime(2020, 7, 15, 13, 10, 5)
    assert date_time.strftime("%c") == "Mi 15 Jul 2020 13:10:05 "
