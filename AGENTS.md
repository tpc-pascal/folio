# AGENTS.md

Agent-facing notes for working in this repository.

## Setup

```bash
pip install -r hf/requirements.txt
```

## Common commands

| Task | Command |
|---|---|
| Run the app locally | `python hf/app.py` (serves on `http://localhost:7860`) |
| Lint | `ruff check hf tests` |
| Format | `ruff format hf tests` |
| Test | `pytest` |

CI runs lint, format check, and tests on every push and PR.

## Layout

- `hf/` — self-contained app. `app.py` is the lean Gradio wiring; heavy logic
  lives in `bookshelf.py` and `reader.py`.
- `hf/static/` — CSS/JS loaded on demand at runtime (never inline the
  blobs back into Python).
- `tests/` — pytest suite; PDF fixtures are generated at runtime, not committed.
- `docs/` — usage, architecture, and HF Spaces notes.

## Conventions

- Keep `app.py` free of styling — put CSS/JS in `static/` and load via `Path`.
- Books/covers (`books/`, `images/`) are release assets and are git-ignored.
- The Hugging Face Space is assembled by `.github/workflows/sync.yml` from
  `hf/`; the Space root receives `app.py`, `bookshelf.py`, `reader.py`,
  `requirements.txt`, `README.md`, and `static/`. Keep this contract intact.
- Version bumps go in `pyproject.toml`, with a matching `CHANGELOG.md` section.