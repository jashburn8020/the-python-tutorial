"""The `datetime` module."""

import time
from datetime import date, datetime, timedelta, timezone

import pytest


def test_timedelta_str_repr() -> None:
    """`str` and `repr` operations on `timedelta`."""
    some_time = timedelta(hours=24, minutes=10)
    assert str(some_time) == "1 day, 0:10:00"
    assert repr(some_time) == "datetime.timedelta(days=1, seconds=600)"


def test_timedelta_normalization() -> None:
    """`timedelta` normalization."""
    some_time = timedelta(hours=24, minutes=10)
    assert some_time == timedelta(days=1, seconds=600)


def test_timedelta_arithmetic() -> None:
    """Arithmetic operations with `timedelta`."""
    ten_mins = timedelta(minutes=10)
    assert ten_mins * 6 == timedelta(hours=1)
    assert ten_mins - timedelta(seconds=60) == timedelta(minutes=9)
    assert ten_mins / timedelta(minutes=5) == 2.0


def test_date_class_methods() -> None:
    """Some `date` class methods."""
    assert date.fromisoformat("2020-07-01") == date(2020, 7, 1)


def test_date_instance_methods() -> None:
    """Some `date` instance methods."""
    some_date = date(2020, 7, 15)
    assert some_date.replace(month=6) == date(2020, 6, 15)
    assert some_date.weekday() == 2
    assert some_date.isoformat() == "2020-07-15"
    assert str(some_date) == "2020-07-15"


def test_date_operations() -> None:
    """Some operations supported by `date`."""
    some_date = date(2020, 7, 15)
    assert some_date + timedelta(hours=24) == date(2020, 7, 16)
    assert some_date + timedelta(hours=13) == date(2020, 7, 15)
    assert some_date - date(2020, 7, 10) == timedelta(days=5)
    assert some_date < date(2020, 7, 16)


def test_datetime_class_methods() -> None:
    """Some `datetime` class methods."""
    assert datetime.fromisoformat("2011-11-04 00:05:23.283+00:00") == datetime(
        2011, 11, 4, 0, 5, 23, 283000, tzinfo=timezone.utc
    )
    assert datetime.fromisoformat("2011-11-04T00:05:23+01:00") == datetime(
        2011, 11, 4, 0, 5, 23, tzinfo=timezone(timedelta(seconds=3600))
    )


def test_datetime_instance_methods() -> None:
    """Some `datetime` instance methods."""
    some_datetime = datetime(2020, 7, 15, 12, 0, 0, tzinfo=timezone(timedelta(hours=2)))
    # local_datetime = some_datetime.astimezone()
    # If the current system local time zone is BST (UTC +1):
    # assert local_datetime.hour == 11
    # assert local_datetime.utcoffset() == timedelta(hours=1)
    # assert local_datetime.tzname() == "BST"
    # assert local_datetime.dst() is None

    bst_timezone = timezone(timedelta(hours=1), "BST")
    bst_datetime = some_datetime.astimezone(bst_timezone)
    assert bst_datetime.hour == 11
    assert bst_datetime.utcoffset() == timedelta(hours=1)
    assert bst_datetime.tzname() == "BST"
    assert bst_datetime.dst() is None

    assert some_datetime.timetuple() == time.struct_time(
        (2020, 7, 15, 12, 0, 0, 2, 197, -1)
    )

    assert some_datetime.timestamp() == 1594807200.0
    unix_epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    assert some_datetime.timestamp() == (some_datetime - unix_epoch).total_seconds()

    assert some_datetime.isoformat() == "2020-07-15T12:00:00+02:00"
    assert some_datetime.isoformat(" ", "minutes") == "2020-07-15 12:00+02:00"


def test_datetime_operations() -> None:
    """Some operations supported by `datetime`."""
    some_datetime = datetime(2020, 7, 15, 12, 0, 0, tzinfo=timezone(timedelta(hours=2)))

    assert some_datetime + timedelta(hours=24) == datetime(
        2020, 7, 16, 12, 0, 0, tzinfo=timezone(timedelta(hours=2))
    )

    assert some_datetime + timedelta(hours=13) == datetime(
        2020, 7, 16, 1, 0, 0, tzinfo=timezone(timedelta(hours=2))
    )

    assert some_datetime - datetime(
        2020, 7, 10, 10, 0, 0, tzinfo=timezone(timedelta(hours=2))
    ) == timedelta(days=5, hours=2)

    assert (
        some_datetime - datetime(2020, 7, 15, 10, 0, 0, tzinfo=timezone.utc)
        == timedelta()
    )

    with pytest.raises(TypeError) as ex_info:
        some_datetime - datetime(2020, 7, 15, 10, 0, 0)
    assert "can't subtract offset-naive and offset-aware datetimes" in str(
        ex_info.value
    )


def test_strftime() -> None:
    """Using the `strftime()` method."""
    some_date = date(2020, 7, 15)
    assert some_date.strftime("%A %d %B %Y") == "Wednesday 15 July 2020"

    some_datetime = datetime(2020, 7, 15, 12, 0, 0, tzinfo=timezone(timedelta(hours=2)))
    assert (
        some_datetime.strftime("%A, %d %B %Y %I:%M%p %Z")
        == "Wednesday, 15 July 2020 12:00PM UTC+02:00"
    )


def test_strptime() -> None:
    """Using the `strptime()` method."""
    some_datetime = datetime.strptime("15/7/20 12:00 +0200", "%d/%m/%y %H:%M %z")
    assert some_datetime == datetime(
        2020, 7, 15, 12, 0, 0, tzinfo=timezone(timedelta(hours=2))
    )
