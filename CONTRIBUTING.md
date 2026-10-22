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
