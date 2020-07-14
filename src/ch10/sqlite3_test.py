"""Using the `sqlite3` module to access SQLite databases."""

import sqlite3
from datetime import date, datetime
from pathlib import Path
from typing import Generator, List, NamedTuple, Tuple

import pytest


@pytest.fixture(name="connect_memory_db")
def fixture_connect_memory_db() -> Generator[sqlite3.Connection, None, None]:
    """Connect to an in-memory database, pre-populated with data."""
    conn = sqlite3.connect(":memory:")
    create_schema(conn)
    insert_data(conn)

    yield conn

    conn.close()


@pytest.fixture(name="connect_file_db")
def fixture_connect_file_db(
    tmp_path: Path,
) -> Generator[sqlite3.Connection, None, None]:
    """Connect to a file-based database, pre-populated with data."""
    db_path = tmp_path.joinpath("sqlite3.db")
    db_exists = db_path.exists()
    conn = sqlite3.connect(db_path)
    if not db_exists:
        create_schema(conn)
        insert_data(conn)

    yield conn

    conn.close()


def create_schema(conn: sqlite3.Connection) -> None:
    """Create the database schema using `executescript()`."""
    with conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.executescript(
            """\
create table tasks(
    id integer primary key autoincrement not null,
    priority integer default 1,
    details text,
    deadline date
);"""
        )


def insert_data(conn: sqlite3.Connection) -> None:
    """Insert data into a database using `executemany()`."""
    data = [
        (2, "Task 1", "2020-07-08"),
        (1, "Task 2", "2020-07-11"),
    ]

    with conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.executemany(
            "insert into tasks (priority, details, deadline) values (?, ?, ?);", data
        )


def test_context_manager_commit() -> None:
    """Use connection as a context manager to automatically commit changes.

    Uses qmark style placeholders for `execute()`.
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    try:
        create_schema(conn)

        with conn:
            cursor.execute(
                "insert into tasks (details, deadline) values (?, ?);",
                ("Task 1", "2020-07-11"),
            )
            # Still in transaction, not committed yet.
            assert conn.in_transaction

        # Change automatically committed - no uncommitted changes.
        assert not conn.in_transaction

        with conn:
            cursor.execute("select * from tasks;")
        assert cursor.fetchone() == (1, 1, "Task 1", "2020-07-11")
    finally:
        conn.close()


def test_context_manager_rollback() -> None:
    """Use connection as a context manager to automatically rollback changes.

    Uses named style placeholders for `execute()`.
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    try:
        create_schema(conn)

        with conn:
            cursor.execute(
                "insert into tasks (details, deadline) values (:det, :dline);",
                {"det": "Task 1", "dline": "2020-07-11"},
            )
            assert conn.in_transaction
            raise RuntimeError
    except RuntimeError:
        assert not conn.in_transaction

        # Change automatically rolled back.
        with conn:
            cursor.execute("select * from tasks;")
        assert cursor.fetchone() is None
    finally:
        conn.close()


def test_retrieve_iterator(connect_file_db: sqlite3.Connection) -> None:
    """Retrieve data using the cursor as an iterator."""
    with connect_file_db as conn:
        cursor = conn.cursor()
        rows = list(cursor.execute("select * from tasks order by priority"))

    assert rows == [(2, 1, "Task 2", "2020-07-11"), (1, 2, "Task 1", "2020-07-08")]


def test_retrieve_fetch_one(connect_memory_db: sqlite3.Connection) -> None:
    """Retrieve data one row at a time."""
    with connect_memory_db as conn:
        cursor = conn.cursor()
        cursor.execute("select * from tasks")

    assert cursor.fetchone() == (1, 2, "Task 1", "2020-07-08")
    assert cursor.fetchone() == (2, 1, "Task 2", "2020-07-11")
    assert cursor.fetchone() is None


def test_retrieve_fetch_all(connect_memory_db: sqlite3.Connection) -> None:
    """Retrieve all rows in one go."""
    with connect_memory_db as conn:
        cursor = conn.cursor()
        cursor.execute("select details from tasks")

    assert cursor.fetchall() == [("Task 1",), ("Task 2",)]
    assert cursor.fetchall() == []


def test_retrieve_row(connect_memory_db: sqlite3.Connection) -> None:
    """Retrieve rows as `Row` objects.

    Uses non-standard `execute()` shortcut.
    """
    with connect_memory_db as conn:
        conn.row_factory = sqlite3.Row
        row: sqlite3.Row = conn.execute("select * from tasks;").fetchone()

    assert len(row) == 4
    assert row.keys() == ["id", "priority", "details", "deadline"]
    assert row[1] == row["priority"] == 2
    assert tuple(row) == (1, 2, "Task 1", "2020-07-08")
    assert list(row) == [1, 2, "Task 1", "2020-07-08"]


def test_retrieve_object(connect_memory_db: sqlite3.Connection) -> None:
    """Retrieve rows as custom objects."""

    class Task(NamedTuple):
        """A task stored as a row in the database."""

        id: int
        priority: int
        details: str
        deadline: date

    def task_factory(cursor: sqlite3.Cursor, row: Tuple[int, int, str, str]) -> Task:
        """Create `Task` objects out of rows."""
        return Task(
            row[0], row[1], row[2], datetime.strptime(row[3], "%Y-%m-%d").date()
        )

    with connect_memory_db as conn:
        conn.row_factory = task_factory
        tasks: List[Task] = conn.execute("select * from tasks;").fetchall()

    assert len(tasks) == 2
    assert tasks[0] == Task(1, 2, "Task 1", date(2020, 7, 8))
    assert tasks[1] == Task(2, 1, "Task 2", date(2020, 7, 11))


def test_default_date_adapter_converter() -> None:
    """Using the default date (`datetime.date`) adapter and converter."""
    conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    try:
        create_schema(conn)

        with conn:
            cursor.execute(
                "insert into tasks (priority, details, deadline) values (?, ?, ?);",
                (2, "Task 1", date(2020, 7, 8)),
            )
            cursor.execute("select * from tasks;")
        assert cursor.fetchone() == (1, 2, "Task 1", date(2020, 7, 8))
    finally:
        conn.close()


def test_save_database(connect_memory_db: sqlite3.Connection, tmp_path: Path) -> None:
    """Save a database in an SQL text format."""
    dump_path = tmp_path.joinpath("dump.sql")
    with open(dump_path, mode="w") as dump_file:
        for line in connect_memory_db.iterdump():
            dump_file.write(f"{line}\n")

    with open(dump_path) as dump_read:
        assert (
            dump_read.read()
            == """\
BEGIN TRANSACTION;
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('tasks',2);
CREATE TABLE tasks(
    id integer primary key autoincrement not null,
    priority integer default 1,
    details text,
    deadline date
);
INSERT INTO "tasks" VALUES(1,2,'Task 1','2020-07-08');
INSERT INTO "tasks" VALUES(2,1,'Task 2','2020-07-11');
COMMIT;
"""
        )
