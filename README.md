# Lab How-To

A practical, copy-pasteable handbook of workflows and recipes organized as a MkDocs documentation site.

## PyProject scaffolding

```bash
python scaffold.py my-new-project --author "Your Name" --email you@example.com --desc "Short one-liner." --git --docs
```

## Building docs
- Prerequisites: Python 3.11+, MkDocs, and MkDocs Material theme.
- Install documentation tooling:


  ```bash
  pip install mkdocs mkdocs-material pymdown-extensions mdx_truly_sane_lists mkdocs-glightbox
  ```
- Run locally:
  ```bash
  mkdocs serve
  ```
- Build the site for distribution:
  ```bash
  mkdocs build
  ```
- Open the site in your browser (default URL: http://127.0.0.1:8000).

## Repository structure (docs)
- `docs/software/` — coding & software topics
- `docs/analysis/` — data wrangling and visualization
- `docs/hardware/` — electronics & equipment
- `docs/lab/` — shared lab practices
- `docs/cheatsheets/` — quick refs
- `mkdocs.yml` — MkDocs configuration and navigation

## Contributing
- Follow conventional commit styles as demonstrated in `docs/software/git.md`.
- Add content under the appropriate section (software, analysis, hardware, lab, cheatsheets).
- Run `mkdocs serve` to preview changes locally before pushing.

## Documentation site
- The content is organized under `docs/` and exposed via the MkDocs navigation defined in `mkdocs.yml`.

## Venv
```powershell
python -m venv "$env:USERPROFILE/.venvs/explainers" 
```

```powershell
& "$env:USERPROFILE/.venvs/explainers/Scripts/Activate.ps1"
```

```powershell
python -m pip install -e ".[docs]"
```