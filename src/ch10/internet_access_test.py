"""Internet Access."""

import re
import requests
from http import HTTPStatus
from http.client import HTTPResponse
from pathlib import Path
from urllib.request import urlopen

import pytest


def test_extract_string_urllib() -> None:
    """Extract some string from a web page using `urllib.request`."""
    with urlopen("https://commons.wikimedia.org/wiki/Main_Page", timeout=2) as response:
        assert isinstance(response, HTTPResponse)
        assert response.status == HTTPStatus.OK
        assert response.reason == HTTPStatus.OK.phrase
        assert response.getheader("Content-Type") == "text/html; charset=UTF-8"

        for line_bytes in response:
            assert isinstance(line_bytes, bytes)
            line = line_bytes.decode("utf-8")  # Decoding the binary data to text.
            if "mf-picture-title" in line:  # look for "Picture of the day"'s div id
                # <div id="mf-picture-title" ...>Picture of the day</div>
                match = re.search(
                    r'<[^>]+ id="mf-picture-title" [^>]+>([^<]+)</div>', line
                )
                assert match and match.group(1) == "Picture of the day"
                break
        else:
            pytest.fail("Unable to find div id")


def test_download_image_urllib(tmp_path: Path) -> None:
    """Download an image from a URL using `urllib.request`."""
    with urlopen(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Teriberka.jpg/500px-Teriberka.jpg",
        timeout=2,
    ) as response:
        assert response.status == HTTPStatus.OK
        content_length = response.getheader("Content-Length")

        image_data: bytes = response.read()
        assert len(image_data) == int(content_length)

    image_path = tmp_path.joinpath("image.jpg")
    with open(image_path, "wb") as file:
        file.write(image_data)

    assert image_path.stat().st_size == int(content_length)


def test_extract_string_requests() -> None:
    """Extract some string from a web page using `requests`."""
    with requests.get(
        "https://commons.wikimedia.org/wiki/Main_Page", stream=True, timeout=2
    ) as response:
        assert isinstance(response, requests.Response)
        assert response.status_code == requests.codes["OK"]
        assert response.reason == "OK"
        assert response.headers["content-type"] == "text/html; charset=UTF-8"

        # When using decode_unicode=True, provide a fallback encoding in the event the
        # server doesn't provide one.
        if response.encoding is None:
            response.encoding = "utf-8"

        for line in response.iter_lines(decode_unicode=True):
            assert isinstance(line, str)
            if "mf-picture-title" in line:  # look for "Picture of the day"'s div id
                # <div id="mf-picture-title" ...>Picture of the day</div>
                match = re.search(
                    r'<[^>]+ id="mf-picture-title" [^>]+>([^<]+)</div>', line
                )
                assert match and match.group(1) == "Picture of the day"
                break
        else:
            pytest.fail("Unable to find div id")


def test_download_image_requests(tmp_path: Path) -> None:
    """Download an image from a URL using `requests`."""
    with requests.get(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Teriberka.jpg/500px-Teriberka.jpg",
        timeout=2,
    ) as response:
        assert response.status_code == requests.codes["OK"]
        content_length = response.headers["content-length"]

        image_data: bytes = response.content
        assert len(image_data) == int(content_length)

    image_path = tmp_path.joinpath("image.jpg")
    with open(image_path, "wb") as file:
        file.write(image_data)

    assert image_path.stat().st_size == int(content_length)
