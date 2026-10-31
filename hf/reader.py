"""PDF page rendering with PyMuPDF.

Renders a PDF page to a Pillow image and caches open documents so that
repeated navigation over the same file does not re-open it.
"""

from __future__ import annotations

import os

import pymupdf
from PIL import Image

_pdf_cache: dict[str, pymupdf.Document] = {}


def _get_doc(pdf_path: str) -> pymupdf.Document:
    """Return a cached, open PyMuPDF document for *pdf_path*."""
    if pdf_path not in _pdf_cache:
        _pdf_cache[pdf_path] = pymupdf.open(pdf_path)
    return _pdf_cache[pdf_path]


def render_page(pdf_path: str | None, page_num: int, scale: float = 2.0) -> Image.Image | None:
    """Render page *page_num* (0-indexed) of *pdf_path* to an RGB image.

    Returns ``None`` when the file is missing, the index is out of range, or
    rendering fails for any reason.
    """
    if not pdf_path or not os.path.isfile(pdf_path):
        return None
    try:
        doc = _get_doc(pdf_path)
        if page_num < 0 or page_num >= len(doc):
            return None
        page = doc[page_num]
        pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale))
        return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    except Exception:
        return None


def get_page_count(pdf_path: str | None) -> int:
    """Return the number of pages in *pdf_path*, or ``0`` if unreadable."""
    if not pdf_path or not os.path.isfile(pdf_path):
        return 0
    try:
        doc = _get_doc(pdf_path)
        return len(doc)
    except Exception:
        return 0


def clear_cache() -> None:
    """Close and forget every cached document."""
    for doc in _pdf_cache.values():
        try:
            doc.close()
        except Exception:
            pass
    _pdf_cache.clear()
