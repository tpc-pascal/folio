"""Gradio wiring for the folio bookshelf and PDF reader.

The heavy lifting lives in :mod:`bookshelf` (shelf rendering) and
:mod:`reader` (page rendering); this module only builds the Blocks UI
and connects the callbacks.
"""

from __future__ import annotations

import os
from pathlib import Path

import gradio as gr
import gradio_client.utils as gc_utils

from bookshelf import build_library_html, list_books
from reader import get_page_count, render_page

# Workaround: serialize bool state values as "boolean" so Gradio does not
# coerce them to strings on the client.
_orig_get_type = gc_utils.get_type
gc_utils.get_type = lambda s: "boolean" if isinstance(s, bool) else _orig_get_type(s)

_STATIC = Path(__file__).parent / "static"

books_cache: list[dict] = []

# This Space runs on ZeroGPU hardware (free accounts cannot downgrade to
# cpu-basic), which refuses to start an app with no @spaces.GPU function bound
# to a Gradio event handler. The reader needs no GPU at all, so this is a no-op
# probe wired to a hidden component that never fires: the startup scan finds it,
# but no GPU is ever requested and no quota is burned.
try:
    import spaces

    @spaces.GPU(duration=5)
    def _gpu_probe() -> None:
        return None

except ImportError:  # running locally, where the spaces package is absent

    def _gpu_probe() -> None:
        return None


def _shell_html() -> str:
    """Return the hidden shell that carries the reader CSS and JS."""
    css = (_STATIC / "reader.css").read_text(encoding="utf-8")
    js = (_STATIC / "reader.js").read_text(encoding="utf-8")
    return f"""
<div style="display:none;height:0;width:0;overflow:hidden;position:absolute;pointer-events:none;"
     aria-hidden="true">
<style>
{css}
</style>
<script>
{js}
</script>
</div>
"""


def refresh_shelf() -> str:
    global books_cache
    books_cache = list_books()
    return build_library_html(books_cache)


def open_reader(filename: str):
    hidden_state = (gr.update(visible=True), gr.update(visible=False), None, "", "", "", 0, 0)
    if not filename:
        return hidden_state
    for b in books_cache:
        if b["filename"] == filename:
            total = get_page_count(b["path"])
            if total == 0:
                return hidden_state
            img = render_page(b["path"], 0)
            return (
                gr.update(visible=False),
                gr.update(visible=True),
                img,
                b["title"],
                f"1 / {total}",
                b["path"],
                1,
                total,
            )
    return hidden_state


def _nav(pdf_path: str, page: int, delta: int):
    if not pdf_path or not os.path.isfile(pdf_path):
        return None, "", 1, 0
    total = get_page_count(pdf_path)
    if total == 0:
        return None, "", 1, 0
    new_page = max(1, min(page + delta, total))
    img = render_page(pdf_path, new_page - 1)
    return img, f"{new_page} / {total}", new_page, total


def prev(pdf_path: str, page: int):
    return _nav(pdf_path, page, -1)


def nxt(pdf_path: str, page: int):
    return _nav(pdf_path, page, 1)


def back_to_shelf():
    return gr.update(visible=True), gr.update(visible=False)


def build_demo() -> gr.Blocks:
    with gr.Blocks(theme=gr.themes.Soft(), title="folio") as demo:
        current_pdf = gr.State("")
        current_page = gr.State(1)
        total_pgs = gr.State(0)
        hidden = gr.Textbox(value="", elem_id="hf-hidden", container=True, label="")

        # Hidden, never-fired handler so ZeroGPU's startup scan detects the
        # @spaces.GPU probe above (see comment at _gpu_probe).
        probe = gr.Textbox(value="", visible=False, elem_id="gpu-probe")
        probe.change(_gpu_probe, inputs=[], outputs=[])

        gr.HTML(_shell_html(), visible=True)

        with gr.Column(visible=True, elem_id="shelf-col") as shelf_col:
            gr.HTML(value=refresh_shelf(), elem_id="shelf-html")

        with gr.Column(visible=True, elem_id="reader-col") as reader_col:
            with gr.Row(elem_id="reader-topbar"):
                back_btn = gr.Button("◀  Back to shelf", elem_id="reader-back")
                title_md = gr.Markdown("", elem_id="reader-title")
                page_info = gr.Markdown("", elem_id="reader-page-info")
            with gr.Column(elem_id="reader-view"):
                page_img = gr.Image(type="pil", show_label=False, elem_id="reader-image")
                with gr.Row(elem_id="reader-floating-controls"):
                    prev_btn = gr.Button("◀", elem_id="pg-prev")
                    gr.Button("⛶", elem_id="fullscreen-btn")
                    next_btn = gr.Button("▶", elem_id="pg-next")

        hidden.change(
            open_reader,
            inputs=[hidden],
            outputs=[
                shelf_col,
                reader_col,
                page_img,
                title_md,
                page_info,
                current_pdf,
                current_page,
                total_pgs,
            ],
        )
        back_btn.click(back_to_shelf, outputs=[shelf_col, reader_col])
        prev_btn.click(
            prev,
            inputs=[current_pdf, current_page],
            outputs=[page_img, page_info, current_page, total_pgs],
        )
        next_btn.click(
            nxt,
            inputs=[current_pdf, current_page],
            outputs=[page_img, page_info, current_page, total_pgs],
        )

    return demo


demo = build_demo()


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
