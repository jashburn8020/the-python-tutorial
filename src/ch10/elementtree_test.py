"""Processing XML using `xml.etree.ElementTree`."""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Optional, Tuple, Union
from xml.dom import minidom

import pytest


def test_parse_string_pretty_print() -> None:
    """Parse XML from a string.

    - Pretty-print using `xml.dom.minidom`
    """
    root: ET.Element = ET.fromstring(
        '<data><country name="Liechtenstein"/><country name="Panama"/></data>'
    )

    xml_string = ET.tostring(root, encoding="unicode")
    assert (
        xml_string
        == '<data><country name="Liechtenstein" /><country name="Panama" /></data>'
    )

    minidom_doc: minidom.Document = minidom.parseString(xml_string)
    assert (
        minidom_doc.toprettyxml(indent="  ")
        == """\
<?xml version="1.0" ?>
<data>
  <country name="Liechtenstein"/>
  <country name="Panama"/>
</data>
"""
    )


def test_parse_file() -> None:
    """Parse XML from a file."""
    sample_path = Path(__file__).parent.joinpath("elementtree_sample1.xml")
    with open(sample_path) as xml_file:
        tree: ET.ElementTree = ET.parse(xml_file)

    root: ET.Element = tree.getroot()
    assert root.tag == "data"


def test_traverse_all() -> None:
    """Traverse through all elements in a tree."""
    root = ET.fromstring(
        '<data><country name="Liechtenstein"/><country name="Panama"/></data>'
    )

    assert [elem.tag for elem in root.iter()] == ["data", "country", "country"]


def test_find() -> None:
    """Find elements in a tree."""
    sample_path = Path(__file__).parent.joinpath("elementtree_sample1.xml")
    with open(sample_path) as xml_file:
        tree = ET.parse(xml_file)

    assert [neighbor.get("name") for neighbor in tree.findall(".//neighbor")] == [
        "Austria",
        "Switzerland",
        "Costa Rica",
        "Colombia",
    ]

    ranks = []
    for country in tree.findall("country"):
        rank: Optional[ET.Element] = country.find("rank")
        ranks.append((country.get("name"), rank.text if rank is not None else ""))
    assert ranks == [("Liechtenstein", "1"), ("Panama", "68")]


XMLType = Union[str, ET.Element, ET.ElementTree]


def assert_xml_equal(actual: XMLType, expected: XMLType) -> None:
    """Assert that the XML canonical forms of `expected` and `actual` are equal."""

    def to_string(xml_data: XMLType) -> str:
        if isinstance(xml_data, str):
            return xml_data

        if isinstance(xml_data, ET.ElementTree):
            xml_data = xml_data.getroot()

        return ET.tostring(xml_data, encoding="unicode")

    assert ET.canonicalize(to_string(actual), strip_text=True) == ET.canonicalize(
        to_string(expected), strip_text=True
    )


def test_modify() -> None:
    """Modify elements and attributes in an XML document."""
    sample_path = Path(__file__).parent.joinpath("elementtree_sample1.xml")
    with open(sample_path) as xml_file:
        tree = ET.parse(xml_file)

    remove_neighbors(tree)
    insert_country(tree)
    append_country(tree)
    replace_rank_text_with_attribute(tree)


def remove_neighbors(tree: ET.ElementTree) -> None:
    """Remove `neighbor` elements from `tree`."""
    for country in tree.findall("country"):
        for neighbor in country.findall("neighbor"):
            country.remove(neighbor)

    expected = """\
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
    </country>
</data>"""

    assert_xml_equal(tree, expected)


def insert_country(tree: ET.ElementTree) -> None:
    """Insert a `country` element after 'Liechtenstein'."""
    monaco: ET.Element = ET.XML('<country name="Monaco"><rank>2</rank></country>')
    tree.getroot().insert(1, monaco)

    expected = """\
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
    </country>
    <country name="Monaco">
        <rank>2</rank>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
    </country>
</data>"""

    assert_xml_equal(tree, expected)


def append_country(tree: ET.ElementTree) -> None:
    """Append a `country` element to `tree`."""
    malaysia = ET.XML('<country name="Malaysia"><rank>69</rank></country>')
    tree.getroot().append(malaysia)

    expected = """\
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
    </country>
    <country name="Monaco">
        <rank>2</rank>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
    </country>
    <country name="Malaysia">
        <rank>69</rank>
    </country>
</data>"""

    assert_xml_equal(tree, expected)


def replace_rank_text_with_attribute(tree: ET.ElementTree) -> None:
    """Replace `rank` element text with a `value` attribute."""
    for country in tree.findall("country"):
        rank_elem = country.find("rank")
        assert rank_elem is not None

        rank_elem.set("value", rank_elem.text if rank_elem.text else "")
        rank_elem.text = None

    expected = """\
<data>
    <country name="Liechtenstein">
        <rank value="1"/>
        <year>2008</year>
        <gdppc>141100</gdppc>
    </country>
    <country name="Monaco">
        <rank value="2"/>
    </country>
    <country name="Panama">
        <rank value="68"/>
        <year>2011</year>
        <gdppc>13600</gdppc>
    </country>
    <country name="Malaysia">
        <rank value="69"/>
    </country>
</data>"""

    assert_xml_equal(tree, expected)


def test_build() -> None:
    """Build an XML document."""
    root = ET.Element("data")
    root.append(ET.Comment("GDP per capita ranking"))

    country = ET.SubElement(root, "country", {"name": "Liechtenstein"})
    rank = ET.SubElement(country, "rank")
    rank.text = "1"

    def create_country(name: str, rank: str) -> ET.Element:
        country = ET.Element("country", {"name": name})
        ET.SubElement(country, "rank").text = rank

        return country

    country_ranks: List[Tuple[str, str]] = [("Monaco", "2"), ("Panama", "68")]
    root.extend([create_country(cr[0], cr[1]) for cr in country_ranks])

    expected = """\
<data>
    <!-- GDP per capita ranking -->
    <country name="Liechtenstein">
        <rank>1</rank>
    </country>
    <country name="Monaco">
        <rank>2</rank>
    </country>
    <country name="Panama">
        <rank>68</rank>
    </country>
</data>"""

    assert_xml_equal(root, expected)


def test_write(tmp_path: Path) -> None:
    """Write an XML document to a file."""
    root = ET.fromstring(
        '<data><country name="Liechtenstein"><rank>1</rank></country></data>'
    )

    tmp_xml_path: Path = tmp_path.joinpath("gdp.xml")
    ET.ElementTree(root).write(tmp_xml_path, "UTF-8", True)

    with open(tmp_xml_path) as xml_file:
        xml_data = xml_file.read()

    assert (
        xml_data
        == """\
<?xml version='1.0' encoding='UTF-8'?>
<data><country name="Liechtenstein"><rank>1</rank></country></data>"""
    )


def test_pretty_write(tmp_path: Path) -> None:
    """Write a pretty XML document to a file."""
    root = ET.fromstring(
        '<data><country name="Liechtenstein"><rank>1</rank></country></data>'
    )

    minidom_doc: minidom.Document = minidom.parseString(
        ET.tostring(root, encoding="unicode")
    )

    tmp_xml_path = tmp_path.joinpath("gdp_pretty.xml")
    with open(tmp_xml_path, mode="w") as pretty_xml_file:
        minidom_doc.writexml(pretty_xml_file, addindent="  ", newl="\n")

    with open(tmp_xml_path) as pretty_read:
        pretty_data = pretty_read.read()

    assert (
        pretty_data
        == """\
<?xml version="1.0" ?>
<data>
  <country name="Liechtenstein">
    <rank>1</rank>
  </country>
</data>
"""
    )


def test_namespace_manual() -> None:
    """Search elements with namespace by manually adding the URI to every tag."""
    sample_path = Path(__file__).parent.joinpath("elementtree_sample2.xml")
    with open(sample_path) as xml_file:
        tree = ET.parse(xml_file)

    actor = tree.find("{http://people.example.com}actor")
    assert actor is not None

    name = actor.find("{http://people.example.com}name")
    assert name is not None

    characters = [
        char.text for char in actor.findall("{http://characters.example.com}character")
    ]
    actor_chars = {name.text: characters}
    assert actor_chars == {"John Cleese": ["Lancelot", "Archie Leach"]}


def test_namespace_dict() -> None:
    """Search elements with namespace added to a dictionary."""
    sample_path = Path(__file__).parent.joinpath("elementtree_sample2.xml")
    with open(sample_path) as xml_file:
        tree = ET.parse(xml_file)

    namespaces = {
        "people": "http://people.example.com",
        "role": "http://characters.example.com",
    }

    actor = tree.find("people:actor", namespaces)
    assert actor is not None

    name = actor.find("people:name", namespaces)
    assert name is not None

    characters = [char.text for char in actor.findall("role:character", namespaces)]
    actor_chars = {name.text: characters}
    assert actor_chars == {"John Cleese": ["Lancelot", "Archie Leach"]}
