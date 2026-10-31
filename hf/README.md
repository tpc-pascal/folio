---
title: folio
emoji: 📚
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 5.15.0
app_file: app.py
pinned: false
---

# folio

A virtual bookshelf and PDF reader built on Gradio.

## Files

- `app.py` — Gradio Blocks app
- `bookshelf.py` — 3D virtual bookshelf renderer
- `reader.py` — PDF page renderer
- `requirements.txt` — Python dependencies
- `static/` — CSS and JavaScript for the UI

## Running locally

```bash
pip install -r requirements.txt
python app.py
```

The app will be available at `http://localhost:7860`.
