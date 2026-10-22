# Architecture

folio is a small Gradio application split into focused modules with the
presentation assets kept out of Python.

## Module

```
hf/
├── app.py           # lean Gradio Blocks wiring and callbacks
├── bookshelf.py     # scan books/, render the shelf as HTML
├── reader.py        # render PDF pages with PyMuPDF (+ cache)
└── static/
    ├── reader.css   # reader/overlay styling (was inline in app.py)
    ├── shelf.css    # bookshelf styling (was inline in bookshelf.py)
    └── reader.js    # keyboard, fullscreen, and overlay behavior
```

### Data flow

1. `bookshelf.list_books()` scans `books/` for `*.pdf`, pairing each with an
   optional cover and `<stem>.meta.json` sidecar.
2. `bookshelf.build_library_html()` renders the shelf grid and returns HTML plus
   its stylesheet, injected into a Gradio `gr.HTML` component.
3. Clicking a spine triggers `selectBook()` (`static/reader.js`), which writes
   the filename into a hidden textbox. Gradio's `change` event calls
   `app.open_reader()`, which switches to the reader and renders page 1.
4. `reader.render_page()` rasterizes a page to a Pillow image; open documents
   are cached so navigation stays fast.

## Static assets

The reader and shelf CSS/JS live in `static/` and are read at runtime via
`Path(__file__).parent / "static"`. This keeps the Python modules lean, makes the
styles reviewable on their own, and avoids shipping large inline blobs.

## Rendering notes

- Pages are rasterized at a configurable `scale` (default 2.0) for crisp output.
- `reader` catches all rendering errors and returns `None`, so a corrupt PDF
  degrades gracefully instead of crashing the UI.
- `app` monkey-patches Gradio's `get_type` so boolean state values serialize as
  `"boolean"` rather than being coerced to strings.

## Deployment

The Hugging Face Space is assembled by `.github/workflows/sync.yml`: it copies
`hf/` to the Space root, so the Space receives `app.py`, `bookshelf.py`,
`reader.py`, `requirements.txt`, `README.md`, and `static/` at the Space root.
Book assets come from GitHub Release attachments. See [hf-spaces.md](hf-spaces.md).