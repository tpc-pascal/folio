"""Scan a book directory and render a 3D virtual bookshelf as HTML.

Books are ``*.pdf`` files in a books directory, optionally paired with a cover
image in an images directory and a ``<stem>.meta.json`` sidecar. The rendered
bookshelf markup plus its stylesheet is returned as a single HTML string that
can be dropped into a Gradio ``gr.HTML`` component.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

BOOKS_DIR = Path("books")
IMAGES_DIR = Path("images")
META_EXT = ".meta.json"

SLOTS = 10

_STATIC = Path(__file__).parent / "static"

BOOK_COLORS = [
    "#6B1A1A",  # wine red
    "#1B3B3B",  # teal
    "#3B1B4B",  # plum
    "#4B3010",  # wood brown
    "#1B1B4B",  # navy
    "#7B6B10",  # gold
    "#1B4B1B",  # green
    "#4B3060",  # lilac
    "#4B4B5B",  # stone grey
    "#6B3020",  # brick red
    "#1B3B5B",  # steel blue
    "#6B4B20",  # amber
]


def _read_meta(stem: str) -> dict:
    meta_file = BOOKS_DIR / f"{stem}{META_EXT}"
    if not meta_file.is_file():
        return {}
    try:
        with open(meta_file, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def list_books() -> list[dict]:
    """Return one descriptor dict per ``.pdf`` in the books directory."""
    books: list[dict] = []
    if not BOOKS_DIR.is_dir():
        return books
    for f in sorted(BOOKS_DIR.iterdir()):
        if f.suffix.lower() != ".pdf":
            continue
        cover = None
        for ext in (".png", ".jpg", ".jpeg"):
            candidate = IMAGES_DIR / f"{f.stem}{ext}"
            if candidate.is_file():
                cover = str(candidate)
                break
        meta = _read_meta(f.stem)
        books.append(
            {
                "filename": f.name,
                "title": meta.get("title") or f.stem,
                "author": meta.get("author"),
                "year": meta.get("year"),
                "pages": meta.get("pages"),
                "description": meta.get("description"),
                "path": str(f),
                "cover": cover,
            }
        )
    return books


def book_color(title: str) -> str:
    """Pick a deterministic spine colour from the title."""
    return BOOK_COLORS[hash(title) % len(BOOK_COLORS)]


def _book_slot(b: dict | None) -> str:
    if b is None:
        return '<div class="book empty"><span>📖</span></div>'
    tooltip_cover_html = '<div class="tip-cover placeholder">📖</div>'
    if b["cover"] and os.path.isfile(b["cover"]):
        cover_url = f"/file={b['cover']}"
        tooltip_cover_html = (
            f'<div class="tip-cover" style="background-image: url(\'{cover_url}\')"></div>'
        )
    color = book_color(b["title"])
    tip_meta = ""
    if b.get("author"):
        tip_meta += f'<div class="tip-author">✍️ {b["author"]}</div>'
    if b.get("pages"):
        tip_meta += f'<div class="tip-pages">📄 {b["pages"]} trang</div>'
    if b.get("description"):
        tip_meta += f'<div class="tip-desc">{b["description"]}</div>'
    return f"""
                <div class="book" onclick="selectBook('{b["filename"]}')"
                     style="background-color: {color};">
                    <div class="book-body">
                        <div class="band band-top"></div>
                        <span class="book-title">{b["title"]}</span>
                        <div class="band band-bottom"></div>
                    </div>
                    <div class="pages-edge"></div>
                    <div class="book-tip">
                        {tooltip_cover_html}
                        <div class="tip-title">{b["title"]}</div>
                        <div class="tip-meta">{tip_meta}</div>
                    </div>
                </div>"""


def build_library_html(books: list[dict]) -> str:
    """Render *books* into a shelf grid and return the HTML plus its CSS."""
    shelves_html = ""
    for i in range(0, len(books), SLOTS):
        row = list(books[i : i + SLOTS])
        row += [None] * (SLOTS - len(row))
        books_html = "".join(_book_slot(b) for b in row)
        shelves_html += f"""
        <div class="shelf">
            <div class="books-row">{books_html}</div>
            <div class="shelf-board"></div>
        </div>"""

    if not shelves_html:
        empty_row = '<div class="book empty"><span>📖</span></div>' * SLOTS
        shelves_html = f"""
        <div class="shelf">
            <div class="books-row">{empty_row}</div>
            <div class="shelf-board"></div>
        </div>"""

    shelf_css = (_STATIC / "shelf.css").read_text(encoding="utf-8")
    return f"""<div class="library-wrapper">
    <div class="library">
        <div class="library-title">🏛️ folio</div>
        <div class="library-inner">
            {shelves_html}
        </div>
    </div>
</div>
<style>
{shelf_css}
</style>"""
