"""Tests for the PDF page renderer."""

from __future__ import annotations

from PIL import Image

from reader import clear_cache, get_page_count, render_page


def test_get_page_count(sample_pdf):
    assert get_page_count(str(sample_pdf)) == 3


def test_get_page_count_missing(tmp_path):
    assert get_page_count(str(tmp_path / "nope.pdf")) == 0
    assert get_page_count(None) == 0


def test_render_page_returns_image(sample_pdf):
    img = render_page(str(sample_pdf), 0)
    assert isinstance(img, Image.Image)


def test_render_page_out_of_range(sample_pdf):
    assert render_page(str(sample_pdf), 99) is None
    assert render_page(str(sample_pdf), -1) is None


def test_render_page_missing_file(tmp_path):
    assert render_page(str(tmp_path / "nope.pdf"), 0) is None
    assert render_page(None, 0) is None


def test_clear_cache(sample_pdf):
    get_page_count(str(sample_pdf))
    clear_cache()
    assert get_page_count(str(sample_pdf)) == 3
