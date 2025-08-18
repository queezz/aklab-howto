# Python Package

Overview of Python basics, environments, and packaging used in this handbook.

Key topics:
- Python basics and syntax
- Dependency management
- Project scaffolding and packaging

## Minimal `pyproject.toml`
````toml
[project]
name = "yourpkg"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["numpy>=1.26"]

[project.urls]
Repository = "https://github.com/you/yourpkg"

[project.optional-dependencies]
dev = [
  "mkdocs>=1.6",
  "mkdocs-material>=9.5",
  "pymdown-extensions>=10.0",
  "mdx_truly_sane_lists>=1.0",
]
````

## Git dependency (PEP 508)
````toml
[project]
dependencies = [
  "specdata @ git+https://github.com/you/specdata@v0.2.0",
]
````

