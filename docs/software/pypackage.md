# Python Package

A Python package is a folder of Python code that can be installed, imported, tested, and reused in a controlled way.

For lab work this is useful even for small tools. A package can hold analysis helpers, device-control utilities, plotting functions, file converters, or command-line scripts. Once the code is packaged, it can be installed into a virtual environment, used from notebooks, tested automatically, and shared with other machines or collaborators.

## Package structure

A common modern layout:

```text
your-project/
├── pyproject.toml
├── README.md
├── src/
│   └── yourpkg/
│       ├── __init__.py
│       └── core.py
└── tests/
    └── test_core.py
```

`yourpkg` is the actual Python package. This is the name used in imports:

```python
import yourpkg
```

The outer project folder is the repository — it may contain docs, tests, notebooks, and configuration. The package itself lives under `src/`.

Using `src/` helps avoid a common mistake: accidentally importing code directly from the project folder instead of importing the installed package. This makes tests and real use behave more similarly.

## `pyproject.toml`

`pyproject.toml` describes the package: its name, version, required Python version, runtime dependencies, optional dev dependencies, CLI entry points, and build-system info.

A minimal example:

```toml
[project]
name = "yourpkg"
version = "0.1.0"
description = "Short description of the package"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
  "numpy>=1.26",
]

[project.urls]
Repository = "https://github.com/you/yourpkg"

[project.optional-dependencies]
dev = [
  "pytest>=8",
  "ruff>=0.6",
  "mkdocs>=1.6",
  "mkdocs-material>=9.6",
  "pymdown-extensions>=10.0",
  "mdx_truly_sane_lists>=1.3",
]
```

The most useful result: the whole project installs with one command:

```bash
python -m pip install -e ".[dev]"
```

## Environments

An environment is an isolated Python installation with its own installed packages — a standard `venv`, a Conda environment, or another tool-managed environment.

The package itself does not care which one is used. `pyproject.toml` describes what is needed; the environment provides a clean place to install those requirements.

Benefits:

- different projects can use different dependency versions
- the system Python stays clean
- setup can be repeated on another machine
- collaborators can install the same project identically
- scripts, notebooks, and tests all use the same installation

## Why `venv` is usually enough

For single-user lab tools and ordinary Python packages, `venv` is the simplest choice. It is built into Python, lightweight, easy to delete, and works directly with `pip` and `pyproject.toml`.

=== "macOS / Linux"

    ```bash
    python -m venv ~/.venvs/yourpkg
    source ~/.venvs/yourpkg/bin/activate
    python -m pip install -e ".[dev]"
    ```

=== "Windows (PowerShell)"

    ```powershell
    python -m venv "$env:USERPROFILE/.venvs/yourpkg"
    & "$env:USERPROFILE/.venvs/yourpkg/Scripts/Activate.ps1"
    python -m pip install -e ".[dev]"
    ```

Conda is useful when the project depends on complex binary scientific libraries, non-Python dependencies, GPU stacks, or packages that are easier to install from Conda channels. For a small package, `venv` is usually enough.

## Editable install

During development, use an editable install:

```bash
python -m pip install -e ".[dev]"
```

The `-e` flag means Python imports the package from the working directory. After editing the source, there is no need to reinstall. This is especially useful when developing alongside notebooks or analysis scripts.

## Git dependency — PEP 508

A package can depend directly on another Git repository:

```toml
[project]
dependencies = [
  "specdata @ git+https://github.com/you/specdata@v0.2.0",
]
```

Use a tag or commit hash when possible. Depending on a moving branch such as `main` is convenient, but less reproducible.

## Console scripts

Small command-line tools can be exposed from `pyproject.toml`:

```toml
[project.scripts]
yourpkg-info = "yourpkg.cli:main"
```

After installation, the command is available inside the environment:

```bash
yourpkg-info
```
