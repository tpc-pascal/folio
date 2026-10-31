# Hugging Face Spaces

folio runs as a Gradio Space at
**[huggingface.co/spaces/tpc-pascal/folio](https://huggingface.co/spaces/tpc-pascal/folio)**.

## How the Space is built

The Space is not maintained by hand. The
[`sync`](../.github/workflows/sync.yml) workflow assembles it on every push to
`main` and on every published release:

1. Downloads the latest Release and extracts `materials.zip` into `books/` and
   `images/` (if present).
2. Copies `hf/` to the Space root. The Space receives `app.py`, `bookshelf.py`,
   `reader.py`, `requirements.txt`, `README.md`, and `static/` at the Space root.
3. Commits with Git LFS enabled (for PDFs and images) and force-pushes to the
   Space repository.

## Updating books

Books are **release assets**, never committed to git:

1. Zip your `books/` and `images/` folders into `materials.zip`.
2. Create a [GitHub Release](https://github.com/tpc-pascal/folio/releases) and
   attach `materials.zip`.
3. The `sync` workflow runs on the release and pushes the books to the Space.

## Keep-alive

The [`wake`](../.github/workflows/wake.yml) workflow restarts the Space once a
day so the free tier does not sleep indefinitely.

## Secrets

Both workflows require a repository secret **`HF_TOKEN`** — a Hugging Face
access token with write access to the Space.