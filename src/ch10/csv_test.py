"""The `csv` module."""


import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List, NamedTuple


def test_read_csv_default() -> None:
    """Read a CSV file in the default (Excel) dialect."""
    csv_sample_path = Path(__file__).parent.joinpath("csv_sample1.csv")

    with open(csv_sample_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_rows: List[List[str]] = list(csv_reader)

    assert csv_rows == [
        ["Item Type", "Order Priority", "Order Date", "Order ID"],
        ["Office Supplies", "L", "5/2/2014", "1"],
        ["Cereal", "H", "4/18/2014", "2"],
    ]


def test_write_csv_default(tmp_path: Path) -> None:
    """Write a CSV file in the default (Excel) dialect.

    Write all rows, then append a single row to an existing CSV file.
    """
    csv_rows = [
        ["Item Type", "Order Priority", "Order Date", "Order ID"],
        ["Office Supplies", "L", "5/2/2014", "1"],
    ]
    csv_row = ["Cereal", "H", "4/18/2014", "2"]

    tmp_csv_path = tmp_path.joinpath("csv_sample.csv")
    with open(tmp_csv_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(csv_rows)

    with open(tmp_csv_path, "a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(csv_row)

    with open(tmp_csv_path) as csv_sample:
        data = csv_sample.read()
    assert (
        data
        == """\
Item Type,Order Priority,Order Date,Order ID
Office Supplies,L,5/2/2014,1
Cereal,H,4/18/2014,2
"""
    )


def test_read_csv_dict() -> None:
    """Read a CSV file into a `dict`."""
    csv_sample_path = Path(__file__).parent.joinpath("csv_sample1.csv")

    with open(csv_sample_path, newline="") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        assert csv_reader.fieldnames == [
            "Item Type",
            "Order Priority",
            "Order Date",
            "Order ID",
        ]
        csv_rows: List[Dict[str, str]] = list(csv_reader)

    assert csv_rows == [
        {
            "Item Type": "Office Supplies",
            "Order Priority": "L",
            "Order Date": "5/2/2014",
            "Order ID": "1",
        },
        {
            "Item Type": "Cereal",
            "Order Priority": "H",
            "Order Date": "4/18/2014",
            "Order ID": "2",
        },
    ]


def test_write_csv_dict(tmp_path: Path) -> None:
    """Write a CSV file from a `dict`."""
    fieldnames = [
        "Item Type",
        "Order Priority",
        "Order Date",
        "Order ID",
    ]
    csv_rows = [
        {
            "Item Type": "Office Supplies",
            "Order Priority": "L",
            "Order Date": "5/2/2014",
            "Order ID": "1",
        },
        {
            "Item Type": "Cereal",
            "Order Priority": "H",
            "Order Date": "4/18/2014",
            "Order ID": "2",
        },
    ]

    tmp_csv_path = tmp_path.joinpath("csv_sample.csv")
    with open(tmp_csv_path, "w", newline="") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(csv_rows)

    with open(tmp_csv_path) as csv_sample:
        data = csv_sample.read()
    assert (
        data
        == """\
Item Type,Order Priority,Order Date,Order ID
Office Supplies,L,5/2/2014,1
Cereal,H,4/18/2014,2
"""
    )


def test_read_dialect() -> None:
    """Read a CSV file in the 'unixpasswd' dialect.

    Uses a subclass of `Dialect`.
    """

    class UnixPasswdDialect(csv.Dialect):
        """Dialect for Unix `passwd` files."""

        # Specify all attributes because the `Dialect` class defaults all to None!
        delimiter = ":"
        quotechar = '"'
        escapechar = None
        doublequote = True
        skipinitialspace = False
        lineterminator = "\r\n"
        quoting = csv.QUOTE_NONE

    csv.register_dialect("unixpasswd", UnixPasswdDialect)

    fieldnames = [
        "Login Name",
        "Encrypted Password",
        "User ID",
        "Group ID",
        "User Name or Comment",
        "Home Directory",
        "Command Interpreter",
    ]
    csv_passwd_path = Path(__file__).parent.joinpath("csv_passwd")
    with open(csv_passwd_path, newline="") as passwd_file:
        passwd_reader = csv.DictReader(
            passwd_file, fieldnames=fieldnames, dialect="unixpasswd"
        )
        passwd_rows = list(passwd_reader)

    csv.unregister_dialect("unixpasswd")

    assert passwd_rows == [
        {
            "Login Name": "bin",
            "Encrypted Password": "x",
            "User ID": "2",
            "Group ID": "2",
            "User Name or Comment": "bin",
            "Home Directory": "/bin",
            "Command Interpreter": "/usr/sbin/nologin",
        },
        {
            "Login Name": "hplip",
            "Encrypted Password": "x",
            "User ID": "117",
            "Group ID": "7",
            "User Name or Comment": "HPLIP system user,,,",
            "Home Directory": "/var/run/hplip",
            "Command Interpreter": "/bin/false",
        },
    ]


def test_write_dialect(tmp_path: Path) -> None:
    """Write a CSV file in the 'unixpasswd' dialect."""
    passwd_rows = [
        ["bin", "x", "2", "2", "bin", "/bin", "/usr/sbin/nologin"],
        ["hplip", "x", "117", "7", "HPLIP user,,,", "/var/run/hplip", "/bin/false",],
    ]

    csv.register_dialect("unixpasswd", delimiter=":", quoting=csv.QUOTE_NONE)
    tmp_passwd_path = tmp_path.joinpath("csv_passwd")
    with open(tmp_passwd_path, "w", newline="") as passwd_file:
        csv_writer = csv.writer(passwd_file, "unixpasswd")
        csv_writer.writerows(passwd_rows)

    csv.unregister_dialect("unixpasswd")

    with open(tmp_passwd_path) as passwd_sample:
        data = passwd_sample.read()
    assert (
        data
        == """\
bin:x:2:2:bin:/bin:/usr/sbin/nologin
hplip:x:117:7:HPLIP user,,,:/var/run/hplip:/bin/false
"""
    )


def test_read_csv_object() -> None:
    """Read a CSV file into named tuple objects."""

    class Order(NamedTuple):
        """Represents a row in a CSV file."""

        item_type: str
        priority: str
        date: datetime
        id: int

    csv_sample_path = Path(__file__).parent.joinpath("csv_sample1.csv")

    with open(csv_sample_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header row
        orders: List[Order] = [
            Order(
                item_type=row[0],
                priority=row[1],
                date=datetime.strptime(row[2], "%m/%d/%Y"),
                id=int(row[3]),
            )
            for row in csv_reader
        ]

    assert len(orders) == 2
    assert orders[0] == Order(
        item_type="Office Supplies", priority="L", date=datetime(2014, 5, 2), id=1
    )
    assert orders[1] == Order(
        item_type="Cereal", priority="H", date=datetime(2014, 4, 18), id=2
    )
