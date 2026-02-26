import pytest  # noqa: F401
from processor import is_image
from pymupdf import Document


class DummyDocument(Document):
    def __init__(self, metadata):
        self.metadata = metadata


def test_is_image_with_image_format():
    doc = DummyDocument(metadata={"format": "Image"})
    assert is_image(doc) is True


def test_is_image_with_non_image_format():
    doc = DummyDocument(metadata={"format": "PDF"})
    assert is_image(doc) is False


def test_is_image_with_missing_format_key():
    doc = DummyDocument(metadata={"author": "someone"})
    assert is_image(doc) is False


def test_is_image_with_none_metadata():
    doc = DummyDocument(metadata=None)
    assert is_image(doc) is False


def test_is_image_with_format_none():
    doc = DummyDocument(metadata={"format": None})
    assert is_image(doc) is False
