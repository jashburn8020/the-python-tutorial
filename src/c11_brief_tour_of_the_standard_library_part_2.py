#!/usr/bin/pytest-3
"""
Brief Tour of the Standard Library Part 2
https://docs.python.org/3/tutorial/stdlib2.html
"""
import reprlib
import pprint
import contextlib
import io
import locale
import datetime
import pytest
from string import Template


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
