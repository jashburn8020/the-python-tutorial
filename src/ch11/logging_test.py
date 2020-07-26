"""Using the `logging` module.

Notes:
- Within a fixture, adding a `StreamHandler` with `sys.stdout` as the stream to a
  logger does _not_ enable the `capsys` fixture to capture the log output.
- Adding a `StreamHandler` as above _within_ a test function does enable `capsys` to
  capture the log output.
- The `caplog` fixture does _not_ make use of the formatter set to the handler.
"""

import logging
import logging.config
import logging.handlers
import re
from collections import deque
from io import StringIO
from typing import Any, Deque, Generator, Optional

import pytest


class LoggerSettings:
    """Provide facilities to set up and tear down the root and module loggers.

    The root logger is provided with a `StreamHandler`, in which a `StringIO` is used to
    capture the log records sent to the handler. The log records are formatted using
    `logging.BASIC_FORMAT`.

    Module loggers are expected to propagate log records to the root logger to be
    handled.
    """

    def __init__(self) -> None:
        self.output = StringIO()
        self.root_handler = logging.StreamHandler(self.output)
        self.root_handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))

        root = logging.getLogger()
        root.addHandler(self.root_handler)

    def get_output(self) -> str:
        """Get the logging output."""
        output = self.output.getvalue()

        self.output = StringIO()
        self.root_handler.setStream(self.output)

        return output

    def set_formatter(self, formatter: logging.Formatter) -> None:
        """Set the formatter for the root handler."""
        self.root_handler.setFormatter(formatter)

    def reset_loggers(self) -> None:
        """Reset the root and module loggers to its defaults."""
        root = logging.getLogger()
        root.setLevel(logging.WARNING)

        root.removeHandler(self.root_handler)
        self.root_handler.close()

        module_logger = logging.getLogger(__name__)
        module_logger.setLevel(logging.NOTSET)
        module_logger.propagate = True


@pytest.fixture(name="logger_settings")
def fixture_logger_settings() -> Generator[LoggerSettings, None, None]:
    """."""
    settings = LoggerSettings()
    yield settings
    settings.reset_loggers()


def test_root_logger(logger_settings: LoggerSettings) -> None:
    """Log messages using the root logger at its default log level."""
    logging.debug("debug message")
    logging.info("info message")
    logging.warning("warning message")
    logging.error("error message")
    logging.critical("critical message")

    assert (
        logger_settings.get_output()
        == """\
WARNING:root:warning message
ERROR:root:error message
CRITICAL:root:critical message
"""
    )


def test_set_level(logger_settings: LoggerSettings) -> None:
    """Set the logging level.

    Let the `LogRecord` propagate to the root logger's handler before it is emitted.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

    assert (
        logger_settings.get_output()
        == """\
DEBUG:logging_test:debug message
INFO:logging_test:info message
WARNING:logging_test:warning message
ERROR:logging_test:error message
CRITICAL:logging_test:critical message
"""
    )

    logger.setLevel(logging.INFO)
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")

    assert (
        logger_settings.get_output()
        == """\
INFO:logging_test:info message
WARNING:logging_test:warning message
"""
    )


def test_log_message_args(logger_settings: LoggerSettings) -> None:
    """Add data to log messages as arguments."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    logger.debug("Debug message with simple string data: %s", "string_data")
    logger.info("Info message with data converted using repr(): %r", "aa\n")
    logger.warning("Warning message with data converted using str(): %s", {"a": "b"})
    logger.error("Error message with numeric data: %d, %.2f", 3, 3.14159)
    logger.critical("Critical message with data from a dictionary: %(a)s", {"a": "b"})

    assert (
        logger_settings.get_output()
        == """\
DEBUG:logging_test:Debug message with simple string data: string_data
INFO:logging_test:Info message with data converted using repr(): 'aa\\n'
WARNING:logging_test:Warning message with data converted using str(): {'a': 'b'}
ERROR:logging_test:Error message with numeric data: 3, 3.14
CRITICAL:logging_test:Critical message with data from a dictionary: b
"""
    )


def test_log_exception(logger_settings: LoggerSettings) -> None:
    """Log exceptions using `logger.exception()`."""
    logger = logging.getLogger(__name__)
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Calculation error")

    log_msg = logger_settings.get_output()
    assert re.match(
        r"ERROR:logging_test:Calculation error\nTraceback .+", log_msg, re.M,
    )


def test_log_exception_warning(logger_settings: LoggerSettings) -> None:
    """Log exceptions using `logger.warning()`."""
    logger = logging.getLogger(__name__)
    try:
        1 / 0
    except ZeroDivisionError:
        logger.warning("Calculation error", exc_info=True)

    log_msg = logger_settings.get_output()
    assert re.match(
        r"WARNING:logging_test:Calculation error\nTraceback .+", log_msg, re.M,
    )


def test_log_stack_info(logger_settings: LoggerSettings) -> None:
    """Log stack information."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.debug("Debug message", stack_info=True)

    log_msg = logger_settings.get_output()
    assert re.match(r"DEBUG:logging_test:Debug message\nStack .+", log_msg, re.M)


@pytest.mark.parametrize(
    "formatter",
    [
        logging.Formatter("%(levelname)s %(funcName)s %(thread)d: %(message)s"),
        logging.Formatter("{levelname} {funcName} {thread}: {message}", style="{"),
        logging.Formatter("$levelname $funcName $thread: $message", style="$"),
    ],
)
def test_format(formatter: logging.Formatter, logger_settings: LoggerSettings) -> None:
    """Format log message using various style."""
    logger_settings.set_formatter(formatter)

    logger = logging.getLogger(__name__)
    logger.warning("The message")
    log_msg = logger_settings.get_output()
    assert re.match(r"WARNING test_format \d+: The message$", log_msg)


def test_format_datefmt(logger_settings: LoggerSettings) -> None:
    """Format log message date/time."""
    formatter = logging.Formatter("%(asctime)s %(message)s", "%d/%m/%Y %H:%M:%S")
    logger_settings.set_formatter(formatter)

    logger = logging.getLogger(__name__)
    logger.warning("The message")
    log_msg = logger_settings.get_output()
    # 18/07/2020 17:35:42 The message
    assert re.match(r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2} The message$", log_msg)


def test_log_extra(logger_settings: LoggerSettings) -> None:
    """Log extra information using the `extra` keyword argument."""
    formatter = logging.Formatter("%(levelname)s [%(user)s]: %(message)s")
    logger_settings.set_formatter(formatter)

    logger = logging.getLogger(__name__)
    logger.warning("The message", extra={"user": "Some User"})
    assert logger_settings.get_output() == "WARNING [Some User]: The message\n"


def test_log_buffering() -> None:
    """Buffer log records up to the buffer capacity after which old records are dropped.

    Flush (output) the buffer of log records only when a record at a specified level or
    higher is logged.
    """

    class BoundedMemoryHandler(logging.handlers.MemoryHandler):
        """A handler class that buffers logging records in memory.

        Buffer up to `capacity` number of `LogRecord`s before discarding old
        `LogRecord`s. Flushing of all records in the buffer occurs whenever an event of
        `flushLevel` or greater is seen. The flushed records are sent to the `target`
        handler.
        """

        def __init__(
            self,
            capacity: int,
            flushLevel: int = logging.ERROR,
            target: Optional[logging.Handler] = None,
        ) -> None:
            super().__init__(capacity, flushLevel, target, False)
            self.flushLevel = flushLevel
            self.target = target
            self.buffer: Deque[logging.LogRecord] = deque([], capacity)

        def shouldFlush(self, record: logging.LogRecord) -> bool:
            """Check for a record at the `flushLevel` or higher."""
            return record.levelno >= self.flushLevel

        def flush(self) -> None:
            """Send the buffered records to the target, and clear the buffer."""
            self.acquire()
            try:
                if self.target:
                    while self.buffer:
                        self.target.handle(self.buffer.popleft())
            finally:
                self.release()

    stringio = StringIO()
    stringio_handler = logging.StreamHandler(stringio)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    stringio_handler.setFormatter(formatter)

    bqueue_handler = BoundedMemoryHandler(3, target=stringio_handler)

    root_logger = logging.getLogger()
    root_logger.addHandler(bqueue_handler)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    logger.info("1")
    logger.info("2")
    logger.info("3")
    logger.info("4")
    assert stringio.getvalue() == ""

    logger.error("5")
    assert stringio.getvalue() == "INFO: 3\nINFO: 4\nERROR: 5\n"

    # Create a new `StringIO` otherwise `getvalue()` will still return the old values.
    stringio = StringIO()
    stringio_handler.setStream(stringio)

    logger.info("6")
    logger.critical("7")
    assert stringio.getvalue() == "INFO: 6\nCRITICAL: 7\n"

    root_logger.removeHandler(bqueue_handler)
    bqueue_handler.close()

    logger.setLevel(logging.NOTSET)


def test_log_buffering_decorator() -> None:
    """Buffer log records up to capacity after which old records are dropped.

    See `test_log_buffering()`.
    """

    class BufferingHandlerDecorator:
        """Similar to `BoundedMemoryHandler`, but using the Decorator pattern.

        This is a proof of concept.

        See https://python-patterns.guide/gang-of-four/decorator-pattern/#implementing-dynamic-wrapper
        """

        def __init__(
            self,
            wrapped: logging.Handler,
            capacity: int,
            flush_level: int = logging.ERROR,
        ) -> None:
            self.wrapped = wrapped
            self.capacity = capacity
            self.flush_level = flush_level
            self.buffer: Deque[logging.LogRecord] = deque([], capacity)

        def handle(self, record: logging.LogRecord) -> bool:
            """."""
            allow = self.wrapped.filter(record)

            if not allow:
                return allow

            self.wrapped.acquire()
            try:
                self.buffer.append(record)
                if record.levelno >= self.flush_level:
                    while self.buffer:
                        self.wrapped.emit(self.buffer.popleft())
            finally:
                self.wrapped.release()

            return allow

        def __getattr__(self, name: str) -> Any:
            return getattr(self.__dict__["wrapped"], name)

        def __setattr__(self, name: str, value: Any) -> None:
            if name in ("wrapped", "capacity", "flush_level", "buffer"):
                self.__dict__[name] = value
            else:
                setattr(self.__dict__["wrapped"], name, value)

        def __delattr__(self, name: str) -> None:
            delattr(self.__dict__["wrapped"], name)

    stringio = StringIO()
    stringio_handler = logging.StreamHandler(stringio)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    stringio_handler.setFormatter(formatter)

    bqueue_handler = BufferingHandlerDecorator(stringio_handler, 3)

    root_logger = logging.getLogger()
    root_logger.addHandler(bqueue_handler)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    logger.info("1")
    logger.info("2")
    logger.info("3")
    logger.info("4")
    assert stringio.getvalue() == ""

    logger.error("5")
    assert stringio.getvalue() == "INFO: 3\nINFO: 4\nERROR: 5\n"

    # Create a new `StringIO` otherwise `getvalue()` will still return the old values.
    stringio = StringIO()
    stringio_handler.setStream(stringio)

    logger.info("6")
    logger.critical("7")
    assert stringio.getvalue() == "INFO: 6\nCRITICAL: 7\n"

    root_logger.removeHandler(bqueue_handler)
    bqueue_handler.close()

    logger.setLevel(logging.NOTSET)
