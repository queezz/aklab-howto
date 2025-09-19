# Installation Guide

Follow these steps to install the package into a virtual environment.

## 1. Create a virtual environment

Let's call it "explainers".
Local:
```powershell
python -m venv explainers
```

Or in central `~/.venvs/`:
```powershell
python -m venv "$env:USERPROFILE/.venvs/explainers"
```

Activate your environment:

```powershell
& "$env:USERPROFILE/.venvs/explainers/Scripts/Activate.ps1"
```

## 2. Update pip

```powershell
python -m pip install -U pip
```

## 3. Install this package (editable mode)

```powershell
python -m pip install -e ".[dev]"
```



## Usage
For this, you don't need to install the package, just copy the scaffolding.py to your folder and run it.

```bash
python scaffold.py NAME [--author AUTHOR] [--email EMAIL]
                    [--desc DESCRIPTION]
                    [--repo-url URL]
                    [--license MIT]
                    [--git] [--docs] [--overwrite]
```

### Arguments

* `name` (required) — project name (used for folder + package)
* `--author` — project author (default: `Your Name`)
* `--email` — author email (default: `you@example.com`)
* `--desc` — short description (default: `"A short description."`)
* `--repo-url` — repository URL (default: `https://github.com/your/repo`)
* `--license` — license type (currently only `MIT`)
* `--git` — initialize Git repo and make first commit
* `--docs` — include MkDocs configuration and docs folder
* `--overwrite` — overwrite existing files if present

---

## Example

Scaffold a new project called `ramanechelle` with Git and Docs enabled:

```bash
python .\scaffold.py  --author "John Doe" --desc "Echelle for Raman" --docs "ramanechelle"
```

---

## Output Structure

Generated project tree (with `--docs`):

```
project-name/
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
├── .pre-commit-config.yaml
├── pyrightconfig.json
├── .vscode/settings.json
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── _version.py
│       └── hello.py
├── tests/
│   └── test_hello.py
├── docs/
│   ├── index.md
│   ├── reference.md
│   └── stylesheets/extra.css
├── mkdocs.yml
└── .github/workflows/
    ├── ci.yml
    └── docs.yml
```

---

## Next Steps

* Customize `README.md` and `pyproject.toml` with project details.
* Add your own modules under `src/<project_name>/`.
* Expand test suite under `tests/`.
* Deploy docs with `mkdocs gh-deploy` if using GitHub Pages.


