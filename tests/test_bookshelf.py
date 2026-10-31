"""Tests for the bookshelf renderer."""

from __future__ import annotations

from bookshelf import BOOK_COLORS, book_color, build_library_html, list_books


def test_list_books_reads_meta(book_dir):
    books = list_books()
    assert len(books) == 1
    b = books[0]
    assert b["filename"] == "sample.pdf"
    assert b["title"] == "Sample Book"
    assert b["author"] == "Tester"
    assert b["pages"] == 3


def test_list_books_empty_dir(tmp_path, monkeypatch):
    import bookshelf

    monkeypatch.setattr(bookshelf, "BOOKS_DIR", tmp_path / "missing")
    assert list_books() == []


def test_book_color_is_deterministic():
    assert book_color("Sample Book") == book_color("Sample Book")


def test_book_color_stays_in_palette():
    for title in ("a", "Sample Book", "Another Longer Title"):
        assert book_color(title) in BOOK_COLORS


def test_build_library_html_renders_title(book_dir):
    html = build_library_html(list_books())
    assert "Sample Book" in html
    assert "selectBook('sample.pdf')" in html
    assert "library-title" in html
    assert "<style>" in html


def test_build_library_html_empty():
    html = build_library_html([])
    assert "book empty" in html
