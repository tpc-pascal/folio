# Contributing to folio

Thanks for your interest in contributing. Please read this guide before
opening a pull request.

## Development setup

```bash
git clone https://github.com/tpc-pascal/folio.git
cd folio
pip install -r hf/requirements.txt
pip install "pytest>=8.0" "ruff>=0.6"
```

Run the app locally:

```bash
python hf/app.py
```

Open <http://localhost:7860>.

## Checks

Run the linter and the test-suite before opening a PR — the same wrapper CI
runs:

```bash
./scripts/check all
```

CI runs the same checks (`lint`, `format`, `test`) on every push and pull
request.

## Workflow

1. Fork the project and create a branch:
   - feature: `git checkout -b feat/short-description`
   - fix: `git checkout -b fix/short-description`
   - docs: `git checkout -b docs/short-description`
2. Make your changes with clear commit messages.
3. Ensure the checks above pass.
4. Open a **Pull Request** describing the change and its motivation.

## Coding standards

- Follow the existing style; Ruff enforces the mechanical rules.
- Keep modules focused — put reusable logic in `hf/`, not in the app
  wiring.
- Add or update tests for behavior changes.
- Prefer small, reviewable PRs.

## Reporting issues

- Open an [Issue](https://github.com/tpc-pascal/folio/issues) for bugs or
  feature requests.
- Report security issues privately — see [SECURITY.md](SECURITY.md).

## Releases

Folio uses immutable SemVer tags (`vX.Y.Z`). To prepare a release:

1. Move the relevant `[Unreleased]` entries in `CHANGELOG.md` into a dated
   `## [vX.Y.Z] - YYYY-MM-DD` section and commit the change.
2. Push the commit to `main` and ensure the working tree is clean and matches
   `origin/main`.
3. Run `./scripts/release.sh vX.Y.Z`. The script creates and pushes an
   annotated tag; GitHub Actions publishes the Release from that changelog
   section.

Published version tags are immutable. The Hugging Face Space workflow deploys
when the GitHub Release is published.
