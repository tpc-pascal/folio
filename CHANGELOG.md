# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions follow
[Semantic Versioning](https://semver.org/). Each `vX.Y.Z` tag publishes a
GitHub Release using the matching section below; run `scripts/release.sh
vX.Y.Z` to cut a release.

## [Unreleased]

### Added

- Add an annotated SemVer release script and a GitHub Actions workflow that
  publishes release notes from this changelog.
- Add the Folio app, bookshelf, and PDF page renderer under `hf/`.
- Add a pytest suite for bookshelf listings and PDF reader behavior.
- Add CI checks for Ruff linting, formatting, and pytest.
- Add a Hugging Face Space workflow for deployment, library asset sync,
  keep-alive, and hardware requests.

### Changed

- Shorten the Folio logo tagline and streamline the root README with clearer
  setup instructions and project links.
- Keep books and cover images in release assets (`books/`, `images/`) rather
  than committing them to the repository.
- Host the Hugging Face Space at `tpc-pascal/folio` (formerly
  `tpc-pascal/libracal`).

### Removed

- Google Colab notebook and launch instructions; Folio is supported for local
  use and Hugging Face Spaces.

- The previous inline CSS/HTML/JS blobs and the ad-hoc repository-keepalive
  workflow.

## [v1.0.0] - 2026-10-21

First release of **folio**, a complete rebuild of the former `libracal` project
with a clean, focused history and a professional layout.
