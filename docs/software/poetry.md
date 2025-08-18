# Poetry

Poetry is a modern tool for managing Python projects. It combines **dependencies, virtual environments, packaging, and publishing** in one workflow.

* Tracks dependencies in `pyproject.toml`
* Creates & manages virtual environments automatically
* Produces reproducible installs with `poetry.lock`
* Builds and publishes packages to PyPI

---

## Why use it

* Cleaner than juggling `pip` + `requirements.txt` + `setup.py`
* Built-in dependency resolver avoids version conflicts
* One file (`pyproject.toml`) describes your whole project
* Straightforward publishing with `poetry build` and `poetry publish`

---

## When to use

* **Libraries or apps you’ll distribute**
* **Collaborative projects** where reproducibility matters
* **Projects with dependencies** you want tracked cleanly

For quick one-off scripts → a bare venv with `pip install` is simpler.
For real, long-lived projects → use Poetry.

---

## Quickstart

```bash
# install (recommended via pipx)
pipx install poetry

# create a project
poetry new myproject
cd myproject

# add dependencies
poetry add requests pandas

# run inside Poetry’s venv
poetry run python main.py

# build & publish
poetry build
poetry publish
```

---

## venv + pip vs Poetry

**TL;DR**

* **venv + pip** → quick scripts, small projects, teaching basics
* **Poetry** → distributable packages, reproducible installs, CI/CD, publishing

| Topic           | venv + pip                                               | Poetry                                    |
| --------------- | -------------------------------------------------------- | ----------------------------------------- |
| Dependency file | `requirements.txt` or `pyproject.toml` (PEP 621 support) | `pyproject.toml` + `poetry.lock`          |
| Env management  | You create/activate manually                             | Poetry auto-creates and manages           |
| Resolver        | pip resolver, fewer safeguards                           | strict resolver prevents conflicts        |
| Build/publish   | `build`, `twine` (extra tools)                           | `poetry build`, `poetry publish` built-in |
| Reproducibility | Pin manually with `pip freeze` or constraints            | Lockfile by default                       |
| Learning curve  | Very low                                                 | Moderate                                  |

---

## Typical workflow

**1) Create project**

venv + pip

```bash
py -3.12 -m venv .venv   # Windows
.\.venv\Scripts\Activate.ps1

python3 -m venv .venv    # macOS/Linux
source .venv/bin/activate

python -m pip install -U pip
pip install requests pandas
pip freeze > requirements.txt
```

Poetry

```bash
pipx install poetry
poetry new myproject
cd myproject
poetry add requests pandas
```

---

**2) Run code**

venv + pip

```bash
python app.py
```

Poetry

```bash
poetry run python app.py
poetry shell   # optional subshell
```

---

**3) Pin / reproduce**

venv + pip

```bash
pip freeze > requirements.txt
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Poetry

```bash
poetry lock
poetry install
```

---

**4) Build / publish**

venv + pip

```bash
pip install build twine
python -m build
twine upload dist/*
```

Poetry

```bash
poetry build
poetry publish
```

---

## VS Code integration

* venv + pip

  * Pick `.venv` manually (`Python: Select Interpreter`).
  * Example `.vscode/settings.json`:

    ```json
    { "python.defaultInterpreterPath": ".venv/bin/python" }
    ```

    On Windows:

    ```json
    { "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe" }
    ```

* Poetry

  ```bash
  poetry env info --path
  ```

  Point VS Code there, or let it auto-detect.
  For project-local venvs:

  ```bash
  poetry config virtualenvs.in-project true
  poetry install
  ```

---

## Pros & cons

venv + pip

* ✅ Standard library only, minimal
* ✅ Great for teaching, tiny repos
* ❌ Manual pinning/version drift
* ❌ Extra tools needed for publishing

Poetry

* ✅ Single source of truth (`pyproject.toml`)
* ✅ Reproducible installs (`poetry.lock`)
* ✅ Built-in build/publish, extras, scripts
* ❌ Slight learning curve, heavy for small scripts

---

## Choosing guide

* One script, few deps → **venv + pip**
* Full project, team, CI/CD → **Poetry**
* Teaching basics → **venv + pip**
* Lab/course notebooks (many students) → **Poetry** (lockfile avoids drift)

---

## Migration

```bash
pipx install poetry
poetry init
poetry add $(sed 's/==.*//' requirements.txt)
poetry install
poetry config virtualenvs.in-project true  # optional
poetry install
```

Export a requirements file for legacy tools:

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

---

## Common pitfalls

* Multiple Pythons →

  ```bash
  poetry env use python3.12
  ```
* VS Code picking wrong interpreter → point to Poetry’s venv path
* Corporate firewall → configure `POETRY_HTTP_BASIC_*` creds or stay with pip
* Editable local installs →

  ```bash
  poetry add --editable .
  ```