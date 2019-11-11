#!/usr/bin/pytest-3
"""
Brief Tour of the Standard Library Part 2
https://docs.python.org/3/tutorial/stdlib2.html
"""
from string import Template
import reprlib
import pprint
import contextlib
import io
import locale
import datetime
import logging
import re
import weakref
import gc
import array
import bisect
import heapq
import decimal
import pytest


def test_reprlib():
    """The reprlib module provides a version of repr() customized for abbreviated displays of large
    or deeply nested containers"""
    assert reprlib.repr(set("thequickbrownfoxjumpsoverthelazydog")
                        ) == "{'a', 'b', 'c', 'd', 'e', 'f', ...}"
    assert reprlib.repr({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
                        ) == "{'a': 1, 'b': 2, 'c': 3, 'd': 4, ...}"


def test_pprint():
    """The pprint module offers more sophisticated control over printing both built-in and user
    defined objects in a way that is readable by the interpreter. When the result is longer than
    one line, the “pretty printer” adds line breaks and indentation to more clearly reveal data
    structure"""
    colours = [["black", "cyan"], "white", ["green", "red", ["blue", "brown"]]]
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        pprint.pprint(colours, indent=4, width=30, depth=2)
    assert output.getvalue() == """\
[   ['black', 'cyan'],
    'white',
    ['green', 'red', [...]]]\n"""


def localise_money(amount):
    """Return localised monetary value based on the current locale"""
    conv = locale.localeconv()
    return locale.format_string("%s%.*f", (conv['currency_symbol'],
                                           conv['frac_digits'], amount), grouping=True)


def test_locale():
    """The locale module accesses a database of culture specific data formats.
    On Linux
    - check supported locales: locale -a
    - add locale: sudo locale-gen de_DE.UTF-8
    - update locale settings: sudo update-locale"""
    num = 12345678.90
    date_time = datetime.datetime(2000, 1, 15, 13, 10, 5)

    locale.setlocale(locale.LC_ALL, "zh_CN.UTF-8")
    assert localise_money(num) == "￥12,345,678.90"
    assert date_time.strftime("%c").strip() == "2000年01月15日 星期六 13时10分05秒"

    locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")
    assert localise_money(num) == "€12.345.678,90"
    assert date_time.strftime("%c").strip() == "Sa 15 Jan 2000 13:10:05"

    locale.resetlocale()


def test_template():
    """The string module includes a Template class. The format uses placeholder names formed by $
    with valid Python identifiers (alphanumeric characters and underscores).

    The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary or
    a keyword argument. For mail-merge style applications, user supplied data may be incomplete and
    the safe_substitute() method may be more appropriate."""

    template = Template("${village}folk send $$10 to ${cause}")
    replacements = {"village": "Nottingham", "cause": "the ditch fund"}
    sentence = template.substitute(replacements)
    assert sentence == "Nottinghamfolk send $10 to the ditch fund"

    pytest.raises(KeyError, template.substitute, village="Nottingham")

    incomplete_sentence = template.safe_substitute(village="Nottingham")
    assert incomplete_sentence == "Nottinghamfolk send $10 to ${cause}"


def test_template_customise():
    """You can derive subclasses of Template to customize the delimiter character by overriding the
    delimiter class attribute. You cannot change the delimiter after class creation."""

    class PercentTemplate(Template):
        """Subclass Template to specify a custom delimiter"""
        delimiter = "%"

    template = PercentTemplate("%{village}folk send $10 to %{cause} 50%% of the time")
    sentence = template.substitute(village="Nottingham", cause="the ditch fund")
    assert sentence == "Nottinghamfolk send $10 to the ditch fund 50% of the time"


class LoggingContext:
    """There are times when it would be useful to temporarily change the logging configuration and
    revert it back after doing something.
    https://docs.python.org/3/howto/logging-cookbook.html#using-a-context-manager-for-selective-logging"""

    def __init__(self, logger, level=None, handler=None, close=True):
        self.logger = logger
        self.logger.propagate = False
        self.level = level
        self.handler = handler
        self.close = close
        self.old_level = None

    def __enter__(self):
        if self.level is not None:
            self.old_level = self.logger.level
            self.logger.setLevel(self.level)
        if self.handler:
            self.logger.addHandler(self.handler)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.level is not None:
            self.logger.setLevel(self.old_level)
        if self.handler:
            self.logger.removeHandler(self.handler)
        if self.handler and self.close:
            self.handler.close()


def test_logging_simple():
    """Log message at the preset levels. Also demonstrates the use of a context manager."""
    logger = logging.getLogger(__name__)
    logs_string = io.StringIO()
    with LoggingContext(logger, handler=logging.StreamHandler(logs_string)):
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")

    assert logs_string.getvalue() == """debug message
info message
warning message
error message
critical message
"""


def test_logging_output_format():
    """Format log output message. See
    https://docs.python.org/3/library/logging.html#logrecord-attributes for the list of LogRecord
    attributes."""
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter("%(levelname)s %(funcName)s(): %(message)s")
    logs_string = io.StringIO()
    log_handler = logging.StreamHandler(logs_string)
    log_handler.setFormatter(formatter)
    with LoggingContext(logger, handler=log_handler):
        logger.warning("warning message")

    assert logs_string.getvalue() == "WARNING test_logging_output_format(): warning message\n"


def test_logging_extra():
    """'extra' can be used to pass a dictionary which is used to populate the __dict__ of the
    LogRecord created for the logging event with user-defined attributes. These custom attributes
    can then be used as you like. For example, they could be incorporated into logged messages."""
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter("%(levelname)s [%(user)s]: %(message)s")
    logs_string = io.StringIO()
    log_handler = logging.StreamHandler(logs_string)
    log_handler.setFormatter(formatter)
    with LoggingContext(logger, handler=log_handler):
        logger.warning("warning message", extra={"user": "Some User"})

    assert logs_string.getvalue() == "WARNING [Some User]: warning message\n"


def test_logging_capsys(capsys):
    """pytest capsys fixture. See https://docs.pytest.org/en/latest/capture.html"""
    logger = logging.getLogger(__name__)
    logger.debug("debug message")
    assert capsys.readouterr().err == ""

    logger.warning("warning message")
    assert capsys.readouterr().err == "warning message\n"


def test_logging_exception(capsys):
    """Exceptions can be logged using logger.exception(), or other logging methods from debug() to
    critical() and pass the exc_info parameter as True"""
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(formatter)
    with LoggingContext(logger, handler=log_handler):
        try:
            1 / 0
        except ZeroDivisionError:
            logger.exception("calculation error")

    pattern = re.compile(r"""^ERROR: calculation error
Traceback.+
  File.+
    1 / 0
ZeroDivisionError: division by zero$""")
    assert pattern.match(capsys.readouterr().err)

    with LoggingContext(logger, handler=log_handler):
        try:
            1 / 0
        except ZeroDivisionError:
            # If exc_info does not evaluate as false, it causes exception information to be added
            # to the logging message
            logger.warning("calculation error", exc_info=True)

    assert re.match(r"^WARNING: calculation error\nTraceback .+$", capsys.readouterr().err, re.M)


def test_logging_stack_info(capsys):
    """If 'stack_info' is true, stack information is added to the logging message, including the
    actual logging call. It shows how you got to a certain point in your code, even when no
    exceptions were raised."""
    logger = logging.getLogger(__name__)
    logger.warning("warning message", stack_info=True)
    assert re.match(r"^warning message\nStack \(most recent call last\):\n.+",
                    capsys.readouterr().err)


def test_weakref():
    """Occasionally there is a need to track objects only as long as they are being used by
    something else. Just tracking them creates a reference that makes them permanent (cannot be
    garbage collected). The weakref module provides tools for tracking objects without creating a
    reference. When the object is no longer needed, it is automatically removed from a weakref
    table.

    A primary use for weak references is to implement caches or mappings holding large objects,
    where it's desired that a large object not be kept alive solely because it appears in a cache
    or mapping. If, for example, an image object is a value in a WeakValueDictionary, then when the
    last remaining references to that image object are the weak references held by weak mappings,
    garbage collection can reclaim the object, and its corresponding entries in weak mappings are
    simply deleted."""
    # pylint: disable=too-few-public-methods
    class BigImage:
        """Dummy class to simulate a large object"""

        def __init__(self, value):
            self.value = value

        def __repr__(self):
            return str(self.value)

    big_image = BigImage(10)  # Create a reference
    weak_dict = weakref.WeakValueDictionary()
    weak_dict["big image"] = big_image

    gc.collect()
    assert weak_dict["big image"] is big_image

    del big_image
    gc.collect()
    with pytest.raises(KeyError):
        assert weak_dict["big image"]


def test_array():
    """Arrays are sequence types and behave very much like lists, except that the type of objects
    stored in them is constrained. It  can compactly represent an array of basic values:
    characters, integers, floating point numbers."""
    signed_int_array = array.array("i", [-1, 0, 1])
    assert sum(signed_int_array) == 0

    with pytest.raises(OverflowError, match="can't convert negative value to unsigned in"):
        array.array("I", [-1, 0, 1])


def test_bisect():
    """The bisect module provides support for maintaining a list in sorted order without having to
    sort the list after each insertion. For long lists of items with expensive comparison
    operations, this can be an improvement over the more common approach.

    bisect(): For a value x, the returned insertion point i partitions the array a into two halves
    so that the left side contains values <= x, and the right side contains values > x."""
    def grade(score, breakpoints=(60, 70, 80, 90), grades='FDCBA'):
        index = bisect.bisect(breakpoints, score)
        return grades[index]

    assert [grade(score) for score in [30, 99, 70, 77]] == ["F", "A", "C", "C"]


def test_bisect_insort():
    """insort(): Insert the value x after any existing entries of x"""
    scores = [(200, "tcl"), (400, "lua")]
    bisect.insort(scores, (300, "ruby"))
    assert scores == [(200, "tcl"), (300, "ruby"), (400, "lua")]


def test_heapq():
    """The heapq module provides an implementation of the heap queue algorithm, also known as the
    priority queue algorithm. Heaps are binary trees for which every parent node has a value less
    than or equal to any of its children.

    The lowest valued entry is always kept at position zero. This is useful for applications that
    repeatedly access the smallest element but do not want to run a full list sort."""
    data = [1, 3, 5, 2, 4, 6]
    heapq.heapify(data)  # Transform list into a heap, in-place, in linear time
    assert data == [1, 2, 5, 3, 4, 6]

    heapq.heappush(data, -1)
    assert data[0] == -1
    assert len(data) == 7

    assert heapq.heappop(data) == -1  # Pop and return the smallest item from the heap
    assert len(data) == 6


def test_decimal():
    """The decimal module offers a Decimal datatype for decimal floating point arithmetic. Compared
    to the built-in float implementation of binary floating point, the class is especially helpful
    for financial applications and other uses that require exact decimal representation."""
    context = decimal.getcontext()  # Get the environment for arithmetic operations
    # ROUND_HALF_EVEN: Round to nearest with ties going to nearest even integer
    assert context.rounding == "ROUND_HALF_EVEN"

    # 0.7 * 1.05 == 0.735
    assert round(0.7 * 1.05, 2) == 0.73
    assert round(decimal.Decimal("0.7") * decimal.Decimal("1.05"), 2) == decimal.Decimal("0.74")

    # Exact representation enables the Decimal class to perform modulo calculations and equality
    # tests that are unsuitable for binary floating point.
    # 0.09999999999999995
    assert 1.00 % 0.10 != 0.00
    assert decimal.Decimal("1.00") % decimal.Decimal("0.10") == decimal.Decimal("0.00")
