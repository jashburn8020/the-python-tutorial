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
