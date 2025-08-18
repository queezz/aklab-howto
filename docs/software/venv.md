# Virtual Environments (venv) — Quick Intro

## What is a venv?

A **virtual environment** is a self-contained folder with its own Python interpreter and libraries.
It keeps each project’s dependencies isolated — so updating one project won’t break another.

👉 [Official docs](https://docs.python.org/3/library/venv.html)

---

## When to use it

* **Always** if a project needs extra Python packages.
* **Collaboration**: teammates install the same dependencies in their own venv.
* **Deployment**: reproducible installs.

---

## Basic usage

### 1. Create and activate

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

**macOS / Linux (bash)**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Upgrade pip

```bash
python -m pip install -U pip
```

### 3. Install dependencies

**Case A: `pyproject.toml`**

```toml
[project]
dependencies = ["numpy", "requests"]

[project.optional-dependencies]
dev = ["pytest", "black"]
```

Install both runtime + dev tools:

```bash
python -m pip install -e ".[dev]"
```

💡 `".[dev]"` means: install this project (`"."`) + optional dev dependencies (`[dev]`).

**Case B: `requirements.txt`**

```bash
python -m pip install -r requirements.txt
```

### 4. Deactivate

```bash
deactivate
```

---

## External venv in VS Code

1. **Create venv outside repo**, e.g. `~/.venvs/example-app`.

   * Windows: `C:\Users\<you>\.venvs\example-app\Scripts\python.exe`
   * macOS/Linux: `/home/<you>/.venvs/example-app/bin/python`

2. **Point VS Code to it** via `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${env:USERPROFILE}\\.venvs\\example-app\\Scripts\\python.exe"
}
```

(on Windows)

```json
{
  "python.defaultInterpreterPath": "${env:HOME}/.venvs/example-app/bin/python"
}
```

(on macOS/Linux)

3. **Result**: VS Code uses that interpreter for terminals, debugging, and Jupyter — without hardcoding usernames.

---


## Daily workflow

### Windows

**Inside repo venv**

```powershell
.\\.venv\\Scripts\\Activate.ps1
python -m pip install -e ".[dev]"   # only once or when deps change
```

**Using external venv**

```powershell
& $env:USERPROFILE\.venvs\example-app\Scripts\Activate.ps1
```

---

### macOS / Linux

**Inside repo venv**

```bash
source .venv/bin/activate
python -m pip install -e ".[dev]"   # only once or when deps change
```

**Using external venv**

```bash
source ~/.venvs/example-app/bin/activate
```
Then run Python as usual (`python`, `pytest`, etc.).
Exit with `deactivate`.



