#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, subprocess, sys
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
  "mkdocs-material>=9.6",
  "mkdocstrings[python]>=0.25",
  "pymdown-extensions>=10.0",
  "mdx_truly_sane_lists>=1.3",
  "mkdocs-glightbox",
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
site_description: ${desc}
repo_url: ${repo_url}
repo_name: ${repo_name}
docs_dir: docs

theme:
  name: material
  icon:
    repo: fontawesome/brands/github
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.tabs
    - navigation.top
    - content.code.copy
    - content.image.zoom
  palette:
    - scheme: custom-dark
      primary: custom
      accent: yellow
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/weather-night
        name: Switch to dark mode

plugins:
  - search
  - glightbox
  - mkdocstrings:
      handlers:
        python:
          options:
            show_source: true

markdown_extensions:
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - pymdownx.details
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - mdx_truly_sane_lists:
      nested_indent: 4
  - toc:
      permalink: true

extra_javascript:
  - javascripts/mathjax.js
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

extra_css:
  - styles/brand.css

nav:
  - Home: index.md
  - API Reference: reference.md
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


BRAND_CSS = """/* =========================================================
   Custom dark scheme: custom-dark
   See https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/
   ========================================================= */

[data-md-color-scheme="custom-dark"] {

  color-scheme: dark;

  /* ===== Brand ===== */

  --md-primary-fg-color: #d98e04;
  --md-primary-fg-color--light: #ffb84d;
  --md-primary-fg-color--dark: #b37400;
  --md-typeset-a-color: #ffcc66;

  /* ===== Backgrounds ===== */

  --md-default-bg-color: #0d1117;
  --md-code-bg-color: #1e2228;

  /* ===== Text ===== */

  --md-default-fg-color: rgba(255,255,240,.92);
  --md-default-fg-color--light: rgba(255,255,240,.70);
  --md-default-fg-color--lighter: rgba(255,255,240,.50);
  --md-default-fg-color--lightest: rgba(255,255,240,.30);
  --md-typeset-color: var(--md-default-fg-color);

  /* ===== Code ===== */

  --md-code-fg-color: rgba(255,255,240,.95);
  --md-typeset-code-color: var(--md-code-fg-color);
  --md-typeset-code-bg: rgba(255,255,255,.08);

  --md-code-hl-operator-color: #f0f0d0;
  --md-code-hl-keyword-color: #f4c542;
  --md-code-hl-string-color: #f9e076;
  --md-code-hl-number-color: #f2b56b;
  --md-code-hl-name-color: #7acf42;
  --md-code-hl-attr-color: #9df0b2;
  --md-code-hl-builtin-color: #a1ebea;
  --md-code-hl-variable-color: #ffcc66;
  --md-code-hl-comment-color: rgba(226,196,161,.718);
  --md-code-hl-punctuation-color: rgba(255,255,240,.75);
  --md-code-selection-bg-color: rgba(0,0,0,.359);

  /* ===== Misc ===== */

  --md-shadow-z1: 0 2px 4px rgba(0,0,0,.5);
  --md-accent-fg-color: #66ffa8;

}


/* =========================================================
   Layout elements
   ========================================================= */

[data-md-color-scheme="custom-dark"] .md-header,
[data-md-color-scheme="custom-dark"] .md-tabs {
  background-color: var(--md-primary-fg-color);
}

[data-md-color-scheme="custom-dark"] .md-search__form {
  background-color: rgba(255,255,255,.06);
}


/* =========================================================
   Code
   ========================================================= */

[data-md-color-scheme="custom-dark"] .md-typeset code {
  background-color: var(--md-typeset-code-bg);
  color: var(--md-typeset-code-color);
}

[data-md-color-scheme="custom-dark"] .md-typeset pre > code,
[data-md-color-scheme="custom-dark"] pre code {
  background-color: var(--md-code-bg-color);
  color: var(--md-code-fg-color);
}

/* punctuation + operators */

[data-md-color-scheme="custom-dark"] .md-typeset pre .p,
[data-md-color-scheme="custom-dark"] .md-typeset pre .o {
  color: var(--md-code-hl-punctuation-color);
}

/* shell builtins */

[data-md-color-scheme="custom-dark"] .md-typeset pre .nb {
  color: var(--md-code-hl-builtin-color);
}


/* =========================================================
   Blockquotes
   ========================================================= */

[data-md-color-scheme="custom-dark"] .md-typeset blockquote {
  background-color: #282d35;
  border-left: .25rem solid #d7ae3b;
  color: var(--md-default-fg-color);
  padding: .8em 1em .8em 1.2em;
  border-radius: 6px;
}


/* =========================================================
   Keyboard keys
   ========================================================= */

[data-md-color-scheme="custom-dark"] .md-typeset kbd {
  background: rgba(255,255,255,.08);
  color: var(--md-default-fg-color);
  border: 1px solid rgba(255,255,255,.20);
  border-bottom-width: 2px;
  border-radius: .35rem;
  padding: .1em .45em;
  font-size: .85em;
  font-weight: 600;
  box-shadow: inset 0 -2px 0 rgba(0,0,0,.35);
}

[data-md-color-scheme="custom-dark"] .md-typeset kbd + kbd {
  margin-left: .15rem;
}

[data-md-color-scheme="custom-dark"] .md-typeset kbd + kbd::before {
  content: " + ";
  color: var(--md-default-fg-color--light);
}


/* =========================================================
   Admonitions
   ========================================================= */

[data-md-color-scheme="custom-dark"] .md-typeset .admonition,
[data-md-color-scheme="custom-dark"] .md-typeset details {
  background-color: rgba(255,255,255,.04);
  color: var(--md-default-fg-color);
  border: 1px solid rgba(255,255,255,.12);
}

[data-md-color-scheme="custom-dark"] .md-typeset .admonition-title {
  background-color: rgba(255,255,255,.06);
}

[data-md-color-scheme="custom-dark"] .md-typeset .admonition.info    { border-color: #66b3ff; }
[data-md-color-scheme="custom-dark"] .md-typeset .admonition.warning { border-color: #ffb84d; }
[data-md-color-scheme="custom-dark"] .md-typeset .admonition.tip     { border-color: #66ffa8; }
[data-md-color-scheme="custom-dark"] .md-typeset .admonition.note    { border-color: #8ab4ff; }


/* =========================================================
   Tables
   ========================================================= */

[data-md-color-scheme="custom-dark"] .md-typeset table {
  background-color: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 6px;
  overflow: hidden;
}

[data-md-color-scheme="custom-dark"] .md-typeset thead {
  background-color: rgba(255,255,255,.05);
}

[data-md-color-scheme="custom-dark"] .md-typeset tbody tr {
  border-top: 1px solid rgba(255,255,255,.06);
}

[data-md-color-scheme="custom-dark"] .md-typeset td,
[data-md-color-scheme="custom-dark"] .md-typeset th {
  border: none;
}

[data-md-color-scheme="custom-dark"] .md-typeset tbody tr:nth-child(even) {
  background-color: rgba(255,255,255,.02);
}

[data-md-color-scheme="custom-dark"] .md-typeset tbody tr:hover {
  background: linear-gradient(
    to right,
    rgba(255,255,255,.06),
    rgba(255,255,255,.03)
  );
}
"""


GH_PAGES = """name: Deploy MkDocs site

on:
  push:
    branches: [main, master]

permissions:
  contents: write

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"

      - name: Install MkDocs + plugins
        run: |
          pip install \\
            mkdocs \\
            mkdocs-material \\
            pymdown-extensions \\
            mdx_truly_sane_lists \\
            "mkdocstrings[python]>=0.25" \\
            mkdocs-glightbox

      - name: Build site
        run: mkdocs build --strict

      - name: Deploy to gh-pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
"""


BRAND_CSS_AKLAB = BRAND_CSS.replace('"custom-dark"', '"bh-dark"')


MKDOCS_AKLAB = """site_name: ${project}
site_description: ${desc}
repo_url: ${repo_url}
repo_name: ${repo_name}
docs_dir: docs

theme:
  name: material
  icon:
    repo: fontawesome/brands/github
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.tabs
    - navigation.top
    - content.code.copy
    - content.image.zoom
  palette:
    - scheme: bh-dark
      primary: custom
      accent: yellow
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
    - scheme: default
      primary: amber
      accent: red
      toggle:
        icon: material/weather-night
        name: Switch to dark mode

plugins:
  - search
  - glightbox

markdown_extensions:
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - pymdownx.details
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - mdx_truly_sane_lists:
      nested_indent: 4
  - toc:
      permalink: true

extra_javascript:
  - javascripts/mathjax.js
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
  - https://unpkg.com/mermaid@10/dist/mermaid.min.js

extra_css:
  - styles/brand.css

nav:
  - Home: index.md
  - Software:
      - 🤖 AI Agent Workflow: software/ai-agent-workflow.md
"""


DOCS_AI_AGENT_PLACEHOLDER = """# AI Agent Workflow

Conventions for working with AI coding assistants in this repository.

---

## Before Any Edit Session

Activate the project venv and verify the build passes:

=== "macOS / Linux"

    ```bash
    source ~/.venvs/${repo}/bin/activate
    mkdocs build --strict
    ```

=== "Windows (PowerShell)"

    ```powershell
    & "$$env:USERPROFILE/.venvs/${repo}/Scripts/Activate.ps1"
    mkdocs build --strict
    ```

---

## Principles

- Incremental changes only — one focused change per session
- Do not rename files or reorganize directories without explicit intent
- Add pages to `nav:` in `mkdocs.yml` when adding files to `docs/`
- Run `mkdocs build --strict` after every meaningful change

---

## Commit Style

- `docs:` — documentation changes
- `chore:` — CI, config, maintenance
- `fix:` — corrections
- `feat:` — new pages or sections
"""


DOCS_CONTRIBUTING = """# Contributing

## Setup

=== "macOS / Linux"

    ```bash
    python -m venv ~/.venvs/${repo}
    source ~/.venvs/${repo}/bin/activate
    python -m pip install -e ".[docs]"
    ```

=== "Windows (PowerShell)"

    ```powershell
    python -m venv "$$env:USERPROFILE/.venvs/${repo}"
    & "$$env:USERPROFILE/.venvs/${repo}/Scripts/Activate.ps1"
    python -m pip install -e ".[docs]"
    ```

## Build

```bash
mkdocs build --strict
mkdocs serve
```

## Guidelines

- Keep navigation shallow
- Stable URLs — do not rename pages without leaving a redirect
- No unnecessary sections or nesting
- Prefer figures and diagrams over dense prose
"""


MATHJAX_JS = """window.MathJax = {
  tex: {
    inlineMath: [["\\\\(", "\\\\)"]],
    displayMath: [["\\\\[", "\\\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

document$.subscribe(() => {
  MathJax.typesetPromise();
});
"""


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("name")
    p.add_argument("--author", default="Your Name")
    p.add_argument("--email", default="you@example.com")
    p.add_argument("--desc", default="A short description.")
    p.add_argument("--repo-url", dest="repo_url", default="https://github.com/your/repo")
    p.add_argument("--license", choices=["MIT"], default="MIT")
    p.add_argument("--path", type=Path, default=None, help="Directory to create the project in (default: current directory)")
    p.add_argument("--here", action="store_true", help="Scaffold into the target directory itself (no subdirectory)")
    p.add_argument("--git", action="store_true")
    p.add_argument("--docs", action="store_true")
    p.add_argument("--aklab", action="store_true", help="Emit full AKLab MkDocs setup (implies --docs)")
    p.add_argument("--overwrite", action="store_true")
    args = p.parse_args()

    if args.aklab:
        args.docs = True

    project = args.name.strip()
    module = slugify(project)
    repo_name = args.repo_url.replace("https://github.com/", "").rstrip("/")
    base = Path(args.path).expanduser().resolve() if args.path is not None else Path.cwd()
    root = base if args.here else base / project
    if args.here and root.exists():
        allowed = {"scaffold.py", ".gitignore", "README.md"}
        existing = {
            p.name for p in root.iterdir()
            if not p.name.startswith(".") or p.name == ".gitignore"
        }
        if existing - allowed:
            print("Target directory contains existing files. Refusing to scaffold in-place.", file=sys.stderr)
            sys.exit(1)
    root.mkdir(parents=True, exist_ok=True)
    year = str(datetime.now().year)

    write(root / "pyproject.toml", tmpl(PYPROJECT, project=project, desc=args.desc, author=args.author, email=args.email, repo_url=args.repo_url), overwrite=args.overwrite)
    write(root / "README.md", tmpl(README, project=project, desc=args.desc), overwrite=args.overwrite)
    write(root / "LICENSE", tmpl(MIT, project=project, author=args.author, year=year), overwrite=args.overwrite)
    gitignore_content = GITIGNORE
    if args.here and args.git and (root / "scaffold.py").exists():
        if "scaffold.py" not in gitignore_content.splitlines():
            gitignore_content = gitignore_content.rstrip() + "\nscaffold.py\n"
    write(root / ".gitignore", gitignore_content, overwrite=args.overwrite)
    write(root / "pyrightconfig.json", PYRIGHT, overwrite=args.overwrite)
    write(root / ".pre-commit-config.yaml", PRECOMMIT, overwrite=args.overwrite)

    write(root / "src" / module / "__init__.py", PKG_INIT, overwrite=args.overwrite)
    write(root / "src" / module / "_version.py", PKG_VERSION, overwrite=args.overwrite)
    write(root / "src" / module / "hello.py", SAMPLE_MOD, overwrite=args.overwrite)
    write(root / "tests" / "test_hello.py", tmpl(TEST_SAMPLE, module=f"{module}.hello"), overwrite=args.overwrite)

    write(root / ".vscode" / "settings.json", tmpl(VSCODE_SETTINGS, userHome="${userHome}"), overwrite=args.overwrite)

    if args.docs:
        if args.aklab:
            mkdocs_content = tmpl(MKDOCS_AKLAB, project=project, desc=args.desc, repo_url=args.repo_url, repo_name=repo_name)
            brand_css_content = BRAND_CSS_AKLAB
        else:
            mkdocs_content = tmpl(MKDOCS, project=project, desc=args.desc, repo_url=args.repo_url, repo_name=repo_name, module=module)
            brand_css_content = BRAND_CSS
        write(root / "mkdocs.yml", mkdocs_content, overwrite=args.overwrite)
        write(root / "docs" / "index.md", tmpl(DOCS_INDEX, project=project, module=module), overwrite=args.overwrite)
        write(root / "docs" / "styles" / "brand.css", brand_css_content, overwrite=args.overwrite)
        write(root / "docs" / "javascripts" / "mathjax.js", MATHJAX_JS, overwrite=args.overwrite)
        write(root / ".github" / "workflows" / "gh-pages.yml", GH_PAGES, overwrite=args.overwrite)
        if not args.aklab:
            write(root / "docs" / "reference.md", tmpl(DOCS_REF, module=module), overwrite=args.overwrite)

    if args.aklab:
        repo = slugify(project)
        write(root / "docs" / "software" / "ai-agent-workflow.md", tmpl(DOCS_AI_AGENT_PLACEHOLDER, repo=repo), overwrite=args.overwrite)
        write(root / "CONTRIBUTING.md", tmpl(DOCS_CONTRIBUTING, repo=repo), overwrite=args.overwrite)

    if args.git:
        if not (root / ".git").exists():
            run(["git", "init", "-b", "main"], cwd=root)
        run(["git", "add", "."], cwd=root)
        run(["git", "commit", "-m", "chore: initial scaffold"], cwd=root)

    print(f"Scaffolded {project} at {root}")
    print("Next:")
    print("  python -m pip install -e \".[dev]\"")
    if args.aklab:
        print("  python -m pip install -e \".[docs]\" && mkdocs build --strict && mkdocs serve")
    elif args.docs:
        print("  python -m pip install -e \".[docs]\" && mkdocs serve")


if __name__ == "__main__":
    main()
