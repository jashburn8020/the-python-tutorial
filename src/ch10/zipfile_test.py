"""The `zipfile` module."""

import shutil
import zipfile
from pathlib import Path
from typing import Final

import pytest


@pytest.fixture(name="tmp_zipfile")
def fixture_tmp_zipfile(tmp_path: Path) -> Path:
    """Path of the ZIP file in the temporary directory."""
    return tmp_path.joinpath("zipfile_samples.zip")


@pytest.fixture(name="samples_zipfile")
def fixture_samples_zipfile() -> Path:
    """Path of the samples ZIP file."""
    return Path(__file__).parent.joinpath("zipfile_samples.zip")


def test_create_zip_direct(tmp_zipfile: Path) -> None:
    """Create a ZIP file directly."""
    data: Final = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do"

    assert not zipfile.is_zipfile(tmp_zipfile)

    with zipfile.ZipFile(
        tmp_zipfile, mode="w", compression=zipfile.ZIP_DEFLATED
    ) as zip_write:
        zip_write.writestr("lorem_ipsum.txt", data)

    assert zipfile.is_zipfile(tmp_zipfile)


def test_create_zip_from_file(tmp_zipfile: Path) -> None:
    """Create a ZIP file from a file, and add another archive member."""
    sample_file_path: Final = Path(__file__).parent.joinpath("zipfile_sample1.txt")

    assert not zipfile.is_zipfile(tmp_zipfile)

    with zipfile.ZipFile(
        tmp_zipfile, mode="w", compression=zipfile.ZIP_DEFLATED
    ) as zip_write:
        zip_write.write(sample_file_path, arcname=sample_file_path.name)

    assert zipfile.is_zipfile(tmp_zipfile)


def test_add_archive_member(tmp_zipfile: Path, samples_zipfile: Path) -> None:
    """Add an archive member to an existing ZIP file.

    Also test a ZIP file, and list archive members.
    """
    shutil.copy(samples_zipfile, tmp_zipfile)
    to_add_file_path: Final = Path(__file__).parent.joinpath("zipfile_sample3.txt")

    with zipfile.ZipFile(
        tmp_zipfile, mode="a", compression=zipfile.ZIP_DEFLATED
    ) as zip_append:
        zip_append.write(to_add_file_path, to_add_file_path.name)
        assert zip_append.testzip() is None
        assert zip_append.namelist() == [
            "zipfile_sample1.txt",
            "zipfile_sample2.txt",
            "zipfile_sample3.txt",
        ]


def test_read_archive_member(samples_zipfile: Path) -> None:
    """Read an archive member from a ZIP file."""
    with zipfile.ZipFile(samples_zipfile) as zip_read:
        data = zip_read.read("zipfile_sample2.txt").decode("utf-8")

    assert data == "eiusmod tempor incididunt ut labore et dolore magna aliqua"


def test_extract_archive_member(tmp_path: Path, samples_zipfile: Path) -> None:
    """Extract one archive member."""
    with zipfile.ZipFile(samples_zipfile) as zip_read:
        zip_read.extract("zipfile_sample2.txt", str(tmp_path))

    with open(tmp_path.joinpath("zipfile_sample2.txt")) as file:
        data = file.read()

    assert data == "eiusmod tempor incididunt ut labore et dolore magna aliqua"


def test_extract_all_members(tmp_path: Path, samples_zipfile: Path) -> None:
    """Extract all archive members."""
    with zipfile.ZipFile(samples_zipfile) as zip_read:
        zip_read.extractall(str(tmp_path))

    (extracted_files := [path.name for path in tmp_path.glob("*.txt")]).sort()
    assert extracted_files == ["zipfile_sample1.txt", "zipfile_sample2.txt"]
