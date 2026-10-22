<p align="center">
  <img src="assets/logo.svg" width="360" alt="folio logo">
</p>

<p align="center">
  <strong>A virtual bookshelf and PDF reader, built on Gradio.</strong>
</p>

<p align="center">
  <a href="https://github.com/tpc-pascal/folio/actions/workflows/ci.yml"><img src="https://github.com/tpc-pascal/folio/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://huggingface.co/spaces/tpc-pascal/folio"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20%20Space-folio-yellow" alt="HF Space"></a>
  <a href="https://colab.research.google.com/github/tpc-pascal/folio/blob/main/colab.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
</p>

---

**folio** renders a collection of PDFs as a 3D bookshelf in your browser. Click a
spine to open the reader, then page through with on-screen controls, arrow keys,
or fullscreen. It runs locally, on [Google Colab](colab.ipynb), or as a
[Hugging Face Space](https://huggingface.co/spaces/tpc-pascal/folio).

## Quickstart

### Run locally

```bash
git clone https://github.com/tpc-pascal/folio.git
cd folio
pip install -r hf/requirements.txt
python hf/app.py
```

Open <http://localhost:7860>. Put your `*.pdf` files in a `books/` directory and
(optional) matching cover images in `images/`, then restart.

### Run on Hugging Face Spaces

Visit **[huggingface.co/spaces/tpc-pascal/folio](https://huggingface.co/spaces/tpc-pascal/folio)**.
Create a [GitHub Release](https://github.com/tpc-pascal/folio/releases) with a
`materials.zip` containing `books/` and `images/`; the
 [`sync`](.github/workflows/sync.yml) workflow pushes them to the Space
automatically. See [docs/hf-spaces.md](docs/hf-spaces.md).

### Run on Google Colab

Open [colab.ipynb](colab.ipynb) and run the cells in order.

## How it works

- `hf/` holds the self-contained app: `app.py`, `bookshelf.py`, `reader.py`,
  `requirements.txt`, `README.md`, and `static/` CSS/JS.
- The bookshelf and reader are rendered by the modules in `hf/`; the UI is a
  [Gradio Blocks](https://www.gradio.app/) app and pages are rasterized with
  [PyMuPDF](https://pymupdf.readthedocs.io/).

See [docs/architecture.md](docs/architecture.md) for the layout and
[docs/usage.md](docs/usage.md) for a full guide.

## Project layout

```
folio/
├── hf/                  # self-contained: app.py, bookshelf.py, reader.py,
│   ├── requirements.txt,
│   ├── README.md,       # static/ CSS/JS loaded on demand at runtime
│   └── static/
│       ├── reader.css
│       ├── shelf.css
│       └── reader.js
├── tests/               # pytest suite
├── docs/                # usage, architecture, HF Spaces
├── assets/              # logo
├── colab.ipynb
└── .github/workflows/   # CI + HF Space sync + keep-alive
```

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). By
participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

[MIT](LICENSE) © tpc-pascal. See [CREDITS.md](CREDITS.md) for acknowledgements.