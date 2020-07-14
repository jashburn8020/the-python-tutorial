"""String pattern matching using the `re` module."""

import re
from typing import Any, Iterator, Match, Optional, Pattern

import pytest


def test_pattern_search() -> None:
    """Compiled pattern search."""
    pattern: Pattern[str] = re.compile(r"[a-z]+\d")

    assert not pattern.search("drum and bass")

    match: Optional[Match[str]] = pattern.search("tempo d3")
    assert match
    assert match.group() == "d3"
    assert match.start() == 6
    assert match.end() == 8
    assert match.span() == (6, 8)


def test_pattern_match() -> None:
    """Compiled pattern match."""
    pattern: Pattern[str] = re.compile(r"[a-z]+\d")

    assert not pattern.match("tempo d3")

    match: Optional[Match[str]] = pattern.search("tempod3")
    assert match
    assert match.group() == "tempod3"
    assert match.span() == (0, 7)


def test_pattern_findall_iter() -> None:
    """Compiled pattern find all matching strings."""
    pattern = re.compile(r"\d+")
    assert pattern.findall("12 drummers, 11 pipers, 10 lords") == ["12", "11", "10"]

    iterator: Iterator[Match[str]] = pattern.finditer("12 drummers, 11 ..., 10 ...")
    assert [match.span() for match in iterator] == [(0, 2), (13, 15), (21, 23)]


def test_module_functions() -> None:
    """`re` module top-level functions."""
    match_search = re.search(r"\bclass\b", "no class at all")
    assert match_search and match_search.group() == "class"

    assert not re.match(r"\bclass\b", "no class at all")
    match_match = re.match(r"\w+\s+class", "no class at all")
    assert match_match and match_match.group() == "no class"


def test_group_numbering() -> None:
    """Capturing strings using grouping metacharacters."""
    match = re.match(r"(a(b)c)(d)", "abcdef")
    assert match and match.group() == match.group(0) == "abcd"
    assert match.group(1) == "abc"
    assert match.group(2) == "b"
    assert match.group(3) == "d"

    assert match.group(1, 3) == ("abc", "d")
    assert match.groups() == ("abc", "b", "d")


def test_backreference() -> None:
    """Using backreferences to detect doubled words."""
    match = re.search(r"\b(\w+)\s+\1\b", "Paris in the the spring")
    assert match and match.group() == "the the"


def test_named_group() -> None:
    """Retrieving matched strings using named groups."""
    match = re.match(r"(?P<first>\w+) (?:[A-Z]\. )?(?P<last>\w+)", "Jane P. Doe")
    assert match and match.group(1) == "Jane"
    assert match.group("last") == "Doe"
    assert match.groupdict() == {"first": "Jane", "last": "Doe"}


def test_positive_lookahead() -> None:
    """Positive lookahead assertion.

    Match first name where last name is 'Brown'.
    """
    pattern = re.compile(r"\w+(?= Brown$)")

    match = pattern.search("Jim Brown")
    assert match and match.group() == "Jim"

    assert not pattern.search("Lisa Smith")
    assert not pattern.search("Jim Browning")
    assert not pattern.search("JimBrown")


def test_negative_lookahead() -> None:
    """Negative lookahead assertion.

    Match filename except where its extension is `bat` or `exe`.
    """
    pattern = re.compile(r".*[.](?!bat$|exe$)[^.]*$")

    match = pattern.search("foo.bar")
    assert match and match.group() == "foo.bar"

    match = pattern.search("mail.batch")
    assert match and match.group() == "mail.batch"

    match = pattern.search("autoexec.bat.orig")
    assert match and match.group() == "autoexec.bat.orig"

    assert not pattern.search("autoexec.bat")
    assert not pattern.search("send.exe")


def test_positive_lookbehind() -> None:
    """Positive lookbehind assertion."""
    pattern = re.compile(r"(?<=-)\w+")

    match = pattern.search("spam-egg")
    assert match and match.group() == "egg"

    match = pattern.search("aim--shoot")
    assert match and match.group() == "shoot"

    match = pattern.search("ready-set-go")
    assert match and match.group() == "set"

    assert not pattern.search("spamegg")


def test_negative_lookbehind() -> None:
    """Negative lookbehind assertion."""
    pattern = re.compile(r"(?<!abc|bbc)def")

    match = pattern.search("cbcdef")
    assert match and match.group() == "def"

    assert not pattern.search("abcdef")
    assert not pattern.search("bbcdef")
    assert not pattern.search("cbcde")


def test_sub() -> None:
    """Search and replace."""
    assert (
        re.sub(r"blue|white|red", "color", "blue socks and red shoes")
        == "color socks and color shoes"
    )


def test_replacement_function() -> None:
    """Search and replace using a replacement function."""

    def hexrepl(match: Match[str]) -> str:
        """Return the hex string for a decimal number."""
        return hex(int(match.group()))

    assert (
        re.sub(r"\d+", hexrepl, "65490: printing, 49152: user code")
        == "0xffd2: printing, 0xc000: user code"
    )


def test_group_backreference() -> None:
    """Search and replace using group and backreference."""
    assert re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat") == "cat in the hat"


@pytest.mark.parametrize(
    "replacement", [r"heading{\1}", r"heading{\g<1>}", r"heading{\g<name>}"]
)
def test_backreference_variants(replacement: str) -> None:
    """Search and replace using variants of backreferences."""
    assert (
        re.sub("section{(?P<name>[^}]*)}", replacement, "section{One} section{Two}")
        == "heading{One} heading{Two}"
    )
