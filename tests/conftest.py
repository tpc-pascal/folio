"""Shared fixtures for the folio test-suite."""

from __future__ import annotations

import sys
from pathlib import Path

import pymupdf
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "hf"))


def _make_pdf(path: Path, pages: int = 3) -> Path:
    doc = pymupdf.open()
    for i in range(pages):
        page = doc.new_page(width=200, height=200)
        page.insert_text((20, 100), f"folio test page {i + 1}")
    doc.save(path)
    doc.close()
    return path


@pytest.fixture
def sample_pdf(tmp_path: Path) -> Path:
    """A 3-page PDF written into a temporary directory."""
    return _make_pdf(tmp_path / "sample.pdf", pages=3)


@pytest.fixture
def book_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, sample_pdf: Path) -> Path:
    """Point the bookshelf module at a temp books/ dir holding one PDF."""
    import bookshelf

    books = tmp_path / "books"
    images = tmp_path / "images"
    books.mkdir()
    images.mkdir()
    (books / "sample.pdf").write_bytes(sample_pdf.read_bytes())
    (books / "sample.meta.json").write_text(
        '{"title": "Sample Book", "author": "Tester", "pages": 3}', encoding="utf-8"
    )
    monkeypatch.setattr(bookshelf, "BOOKS_DIR", books)
    monkeypatch.setattr(bookshelf, "IMAGES_DIR", images)
    return books
