# Usage Guide

## Requirements

- Python 3.10+
- PDF files in a `books/` directory
- Optional cover images in `images/` (PNG/JPG, same stem as the PDF)
- Optional `<name>.meta.json` sidecar per book with `title`, `author`, `year`,
  `pages`, `description`

## Project layout

```
folio/
├── hf/                 # self-contained: app.py, bookshelf.py, reader.py,
│   ├── requirements.txt,
│   ├── README.md,      # static/ CSS/JS loaded on demand at runtime
│   └── static/
│       ├── reader.css
│       ├── shelf.css
│       └── reader.js
├── tests/
├── docs/
├── assets/logo.svg
└── colab.ipynb
```

`books/` and `images/` are **not** stored in the repository — they are attached
as **release assets** (`materials.zip`). The `sync` workflow downloads and pushes
them to the Hugging Face Space.

## Run locally

```bash
git clone https://github.com/tpc-pascal/folio.git
cd folio
pip install -r hf/requirements.txt
python hf/app.py
```

Open <http://localhost:7860>.

## Run on Hugging Face Spaces

Visit **[huggingface.co/spaces/tpc-pascal/folio](https://huggingface.co/spaces/tpc-pascal/folio)**.

Create a [GitHub Release](https://github.com/tpc-pascal/folio/releases) with a
`materials.zip` containing `books/` and `images/`; the workflow syncs them
automatically. See [hf-spaces.md](hf-spaces.md).

## Run on Google Colab

Open [colab.ipynb](../colab.ipynb) and run the cells in order. The final cell
prints a public Gradio share link.

## Reading controls

- Click a book spine to open the reader.
- Page with the on-screen buttons or the **←** / **→** arrow keys.
- Press **F** (or the ⛶ button) for fullscreen.
- Press **Esc** (or "Back to shelf") to return to the bookshelf.