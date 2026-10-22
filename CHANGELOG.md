# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions follow
[Semantic Versioning](https://semver.org/).

## [v1.0.0] - 2026-10-21

First release of **folio**, a complete rebuild of the former `libracal` project
with a clean, focused history and a professional layout.

### Added

- `folio` Python package (`hf/`) with a lean Gradio Blocks app, a book
  shelf renderer, and a PyMuPDF page renderer.
- Static assets extracted from the previous inline blobs: `reader.css`,
  `shelf.css`, and `reader.js` (loaded on demand at runtime).
- Runtime dependencies pinned in `hf/requirements.txt`; Ruff and pytest run
  through a single `scripts/check` wrapper shared by CI and contributors.
- Pytest suite covering the bookshelf renderer and the PDF page renderer, with
  a generated-PDF fixture (no binaries committed).
- CI workflow running Ruff lint/format checks and the test suite on every push
  and pull request.
- Hugging Face Space workflow that assembles the Space from `hf/`, pushes book
  assets from GitHub Releases, and restarts the Space daily (keep-alive).
- Full documentation set: README, contributing guide, code of conduct,
  security policy, and credits.
- Google Colab notebook for one-click launch.

### Changed

- Books and cover images remain release assets (`books/`, `images/`) and are
  never committed to the repository.
- The Hugging Face Space is now `tpc-pascal/folio` (formerly `tpc-pascal/libracal`).

### Removed

- The previous inline CSS/HTML/JS blobs and the ad-hoc repository-keepalive
  workflow.
