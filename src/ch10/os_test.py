"""Operating System Interface and File Wildcards."""

import glob
import os
import shutil
from pathlib import Path
from typing import Generator, List


def test_environ() -> None:
    """Setting and getting environment variables."""
    os.environ["TEST"] = "tester"
    assert os.getenv("TEST") == "tester"


def test_copy_delete_file(tmp_path: Path) -> None:
    """Copying and deleting a file."""
    sample_file = Path(__file__).parent.joinpath("sample.txt")

    sample_file_tmp = tmp_path.joinpath("sample.txt")
    assert not os.path.exists(sample_file_tmp)

    shutil.copyfile(sample_file, sample_file_tmp)
    assert os.path.isfile(sample_file_tmp)
    # pathlib.Path equivalent
    assert sample_file_tmp.is_file()

    os.remove(sample_file_tmp)
    assert not os.path.exists(sample_file_tmp)
    # pathlib.Path equivalent
    assert not sample_file_tmp.exists()


def test_glob(tmp_path: Path) -> None:
    """Listing files using glob wildcards."""
    sample_original = Path(__file__).parent.joinpath("sample.txt")

    tmp_sample1 = tmp_path.joinpath("sample1.txt")
    shutil.copyfile(sample_original, tmp_sample1)
    tmp_sample2 = tmp_path.joinpath("sample2.txt")
    shutil.copyfile(sample_original, tmp_sample2)

    tmp_sub_dir = tmp_path.joinpath("subdir")
    tmp_sub_dir.mkdir()
    tmp_sample3 = tmp_sub_dir.joinpath("sample3.txt")
    shutil.copyfile(sample_original, tmp_sample3)

    files: List[str] = glob.glob(str(tmp_path.joinpath("**/*.txt")), recursive=True)
    assert files == [str(tmp_sample1), str(tmp_sample2), str(tmp_sample3)]

    # pathlib.Path equivalent
    file_paths: Generator[Path, None, None] = tmp_path.glob("**/*.txt")
    assert [str(path) for path in file_paths] == files
