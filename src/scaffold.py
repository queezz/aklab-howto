#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, subprocess
from pathlib import Path
from datetime import datetime
from string import Template


def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^\w\-]+", "-", s)
    s = s.strip("-")
    s = s.replace("-", "_")
    if not re.match(r"^[a-zA-Z_]", s):
        s = f"pkg_{s}"
    return s


def write(path: Path, content: str, *, overwrite: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return
    path.write_text(content, encoding="utf-8")


def run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def tmpl(s: str, **kw) -> str:
    return Template(s).substitute(**kw)


MIT = """${project} — ${year} ${author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


PYPROJECT = """[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "${project}"
version = "0.1.0"
description = "${desc}"
readme = "README.md"
requires-python = ">=3.10"
authors = [{ name = "${author}", email = "${email}" }]
license = { text = "MIT" }
classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
]
dependencies = [
  "numpy>=1.26",
  "scipy>=1.11",
  "matplotlib>=3.8",
  "plotly>=5.20",
  "pandas>=2.2",
  "astropy>=6.0",
]

[project.optional-dependencies]
dev = [
  "pytest>=8.0",
  "pytest-cov>=5.0",
  "ruff>=0.4.0",
  "black>=24.3.0",
  "mypy>=1.8.0",
  "ipython",
  "ipykernel",
]
docs = [
  "mkdocs>=1.6",
  "mkdocs-material>=9.5",
  "mkdocstrings[python]>=0.25",
  "mkdocs-jupyter>=0.25",
]

[project.urls]
Homepage = "${repo_url}"
Repository = "${repo_url}"
Issues = "${repo_url}/issues"

[tool.setuptools.packages.find]
where = ["src"]

[tool.black]
line-length = 100
target-version = ["py310"]

[tool.ruff]
line-length = 100
target-version = "py310"
lint.select = ["E","F","I","B","UP","W","C90"]
lint.ignore = ["E203","E266","E501"]
src = ["src"]

[tool.pytest.ini_options]
addopts = "-q"
testpaths = ["tests"]
"""


GITIGNORE = r"""# Python
__pycache__/
*.py[cod]
*.egg-info/
build/
dist/
.coverage
htmlcov/
.pytest_cache/
.mypy_cache/

# Jupyter
.ipynb_checkpoints/

# MkDocs
site/

# OS
.DS_Store
Thumbs.db

# Env
.env
.venv/
"""


README = """# ${project}

${desc}

## Quickstart

```bash
python -m pip install -e ".[dev]"
pytest
```

## Docs

```bash
python -m pip install -e ".[docs]"
mkdocs serve
```
"""


PKG_INIT = """from ._version import __version__

__all__ = ["__version__"]
"""


PKG_VERSION = """__version__ = "0.1.0"
"""


SAMPLE_MOD = """def hello(name: str) -> str:
    return f"Hello, {name}!"
"""


TEST_SAMPLE = """from ${module} import hello

def test_hello():
    assert hello("world") == "Hello, world!"
"""


PYRIGHT = """{
  "typeCheckingMode": "basic",
  "reportMissingTypeStubs": false,
  "pythonVersion": "3.10"
}
"""


VSCODE_SETTINGS = """{
  "python.venvPath": "${userHome}/.venvs",
  "python.testing.pytestEnabled": true,
  "python.analysis.typeCheckingMode": "basic",
  "editor.rulers": [100],
  "files.exclude": {
    "**/__pycache__": true
  }
}
"""


PRECOMMIT = """repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
        args: [--fix]
  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks:
      - id: black
"""


MKDOCS = """site_name: ${project}
repo_url: ${repo_url}
strict: true
theme:
  name: material
  features:
    - navigation.instant
    - navigation.tracking
    - content.code.copy
markdown_extensions:
  - admonition
  - toc:
      permalink: true
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            show_source: false
  - mkdocs-jupyter
nav:
  - Home: index.md
  - API: reference.md
extra_css:
  - stylesheets/extra.css
"""


DOCS_INDEX = """# ${project}

Welcome.

```python
from ${module} import hello
hello("world")
```
"""


DOCS_REF = """# API Reference

::: ${module}
"""


DOCS_CSS = ":root { --md-code-bg-color: rgba(0,0,0,.04); }\n"


GH_CI = """name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  tests:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [ "3.10", "3.11", "3.12" ]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m pip install -U pip
      - run: python -m pip install -e ".[dev]"
      - run: ruff --version && black --version
      - run: ruff check .
      - run: black --check .
      - run: pytest --maxfail=1 --disable-warnings -q
"""


GH_PAGES = """name: Deploy Docs

on:
  push:
    branches: [ main ]
    paths:
      - "mkdocs.yml"
      - "docs/**"
      - "src/**"
      - ".github/workflows/docs.yml"

permissions:
  contents: write

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install -U pip
      - run: python -m pip install -e ".[docs]"
      - run: mkdocs build --strict
      - name: Deploy to gh-pages
        run: mkdocs gh-deploy --force
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
"""


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("name")
    p.add_argument("--author", default="Your Name")
    p.add_argument("--email", default="you@example.com")
    p.add_argument("--desc", default="A short description.")
    p.add_argument("--repo-url", dest="repo_url", default="https://github.com/your/repo")
    p.add_argument("--license", choices=["MIT"], default="MIT")
    p.add_argument("--git", action="store_true")
    p.add_argument("--docs", action="store_true")
    p.add_argument("--overwrite", action="store_true")
    args = p.parse_args()

    project = args.name.strip()
    module = slugify(project)
    root = Path(project).resolve()
    year = str(datetime.now().year)

    write(root / "pyproject.toml", tmpl(PYPROJECT, project=project, desc=args.desc, author=args.author, email=args.email, repo_url=args.repo_url), overwrite=args.overwrite)
    write(root / "README.md", tmpl(README, project=project, desc=args.desc), overwrite=args.overwrite)
    write(root / "LICENSE", tmpl(MIT, project=project, author=args.author, year=year), overwrite=args.overwrite)
    write(root / ".gitignore", GITIGNORE, overwrite=args.overwrite)
    write(root / "pyrightconfig.json", PYRIGHT, overwrite=args.overwrite)
    write(root / ".pre-commit-config.yaml", PRECOMMIT, overwrite=args.overwrite)

    write(root / "src" / module / "__init__.py", PKG_INIT, overwrite=args.overwrite)
    write(root / "src" / module / "_version.py", PKG_VERSION, overwrite=args.overwrite)
    write(root / "src" / module / "hello.py", SAMPLE_MOD, overwrite=args.overwrite)
    write(root / "tests" / "test_hello.py", tmpl(TEST_SAMPLE, module=f"{module}.hello"), overwrite=args.overwrite)

    write(root / ".vscode" / "settings.json", tmpl(VSCODE_SETTINGS, userHome="${userHome}"), overwrite=args.overwrite)

    if args.docs:
        write(root / "mkdocs.yml", tmpl(MKDOCS, project=project, repo_url=args.repo_url, module=module), overwrite=args.overwrite)
        write(root / "docs" / "index.md", tmpl(DOCS_INDEX, project=project, module=module), overwrite=args.overwrite)
        write(root / "docs" / "reference.md", tmpl(DOCS_REF, module=module), overwrite=args.overwrite)
        write(root / "docs" / "stylesheets" / "extra.css", DOCS_CSS, overwrite=args.overwrite)
        write(root / ".github" / "workflows" / "docs.yml", GH_PAGES, overwrite=args.overwrite)

    write(root / ".github" / "workflows" / "ci.yml", GH_CI, overwrite=args.overwrite)

    if args.git:
        if not (root / ".git").exists():
            run(["git", "init", "-b", "main"], cwd=root)
        run(["git", "add", "."], cwd=root)
        run(["git", "commit", "-m", "chore: initial scaffold"], cwd=root)

    print(f"Scaffolded {project} at {root}")
    print("Next:")
    print("  python -m pip install -e \".[dev]\"")
    if args.docs:
        print("  python -m pip install -e \".[docs]\" && mkdocs serve")


if __name__ == "__main__":
    main()
