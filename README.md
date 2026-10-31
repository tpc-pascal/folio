<p align="center">
  <img src="assets/logo.svg" alt="Folio — PDF library" width="560"/>
</p>

<p align="center">
  <a href="https://github.com/tpc-pascal/folio/stargazers"><img src="https://img.shields.io/github/stars/tpc-pascal/folio?label=stars" alt="Stars"></a>
  <a href="https://github.com/tpc-pascal/folio/releases"><img src="https://img.shields.io/github/v/release/tpc-pascal/folio" alt="Release"></a>
  <a href="https://github.com/tpc-pascal/folio/actions/workflows/ci.yml"><img src="https://github.com/tpc-pascal/folio/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://huggingface.co/spaces/tpc-pascal/folio"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Space-Folio-yellow" alt="Hugging Face Space"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
</p>

Folio turns a folder of PDFs into an interactive 3D bookshelf in your browser.
Select a book to read it, navigate pages with the controls or arrow keys, and
switch to fullscreen when you want a focused reading view.

## Run locally

```bash
git clone https://github.com/tpc-pascal/folio.git
cd folio
pip install -r hf/requirements.txt
mkdir -p books images
python hf/app.py
```

Open <http://localhost:7860>. Add PDF files to `books/` and optional matching
cover images to `images/`; restart Folio to load changes.

## Hugging Face Space

Visit the hosted [Folio Space](https://huggingface.co/spaces/tpc-pascal/folio).
To update its library, publish a GitHub Release containing `materials.zip` with
`books/` and `images/`. The
[`Hugging Face Space` workflow](.github/workflows/hf-space.yml) deploys the app
and syncs those assets to the Space.

## Project structure

| Path | Purpose |
|---|---|
| [`hf/app.py`](hf/app.py) | Gradio app and reader interactions |
| [`hf/bookshelf.py`](hf/bookshelf.py) | PDF discovery and bookshelf rendering |
| [`hf/reader.py`](hf/reader.py) | PDF page rendering with PyMuPDF |
| [`hf/static/`](hf/static/) | Reader and bookshelf styles and scripts |
| [`tests/`](tests/) | Bookshelf and reader tests |
| [`scripts/check`](scripts/check) | Lint, format, and test commands |

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Please
follow the [Code of Conduct](CODE_OF_CONDUCT.md). For security issues, see
[SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE) © tpc-pascal. See [CREDITS.md](CREDITS.md) for acknowledgements.
