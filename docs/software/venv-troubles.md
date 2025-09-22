# VS Code + `venv` auto‑detection (Windows)

A quick memo for making VS Code reliably find your Python virtual environments.

## TL;DR
1. **Use User settings for discovery**, keep workspace settings minimal.  
2. Put global virtual envs in `C:\Users\<you>\.venvs\...` **or** use a per‑project `.venv`.  
3. Refresh: *Python: Clear Cache and Reload* → *Python: Select Interpreter* → *Refresh*.

---

## 1) User settings (discovery lives here)
Open **User** settings JSON and add only this:

```json
{
  "python.venvPath": "${env:USERPROFILE}/.venvs",
  "python.venvFolders": [".venv", "venv", "${env:USERPROFILE}/.venvs"],
  "python.terminal.activateEnvironment": true
}
```

> Keep `python.defaultInterpreterPath` **unset** if you want auto‑detection. Set it only when you want to **force** a specific interpreter.

---

## 2) Workspace settings (keep it clean)
In your project’s `.vscode/settings.json`, use a minimal config:

```json
{
  "python.terminal.activateEnvironment": true,
  "python.analysis.typeCheckingMode": "off",
  "editor.rulers": [100],
  "files.exclude": { "**/__pycache__": true }
}
```

Remove any of these if present (they often break discovery):
```json
"python.pythonPath": "...",
"python.defaultInterpreterPath": "...",
"python.testing.*": "...",
"python-envs.*": "..."
```

---

## 3) Create/activate an env

### Option A — global env under `~/.venvs` (good if you share one env across projects)
```powershell
# PowerShell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.venvs" | Out-Null
py -3.11 -m venv "$env:USERPROFILE\.venvs\myenv"
& "$env:USERPROFILE\.venvs\myenv\Scripts\Activate.ps1"
python -m pip install -e ".[dev]"
```

### Option B — per‑project `.venv` (zero‑config, most reliable)
```powershell
# In the project root
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

> VS Code auto‑detects a workspace‑local `.venv` without any extra settings.

---

## 4) Jupyter kernel (optional but handy)
If you use notebooks, register the env as a kernel once:

```powershell
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

Then in VS Code notebooks choose kernel **Python (myenv)**.

---

## 5) Refresh environments
- **Python: Clear Cache and Reload**  
- **Python: Select Interpreter** → **Refresh** → pick your env

If it still doesn’t show, use **Enter interpreter path…** and browse to:
```
C:\Users\<you>\.venvs\myenv\Scripts\python.exe
```
(After picking once, VS Code remembers per‑workspace.)

---

## Troubleshooting

- **Dropbox/OneDrive paths**: open the folder using its **canonical path** (e.g., `C:\Users\<you>\Dropbox\...`) to avoid cache confusion from symlinks/junctions.
- **Paths in JSON**: use `/` or escape backslashes (`\\`).
- **Old settings lingering**: remove any `python-envs.*`, legacy `python.pythonPath`, or `python.testing.*` entries from workspace settings.
- **Terminal doesn’t auto‑activate**: ensure `"python.terminal.activateEnvironment": true` and open a **new** terminal.
- **Pinning on purpose**: when you want to force an interpreter, set
  ```json
  "python.defaultInterpreterPath": "C:/Users/<you>/.venvs/myenv/Scripts/python.exe"
  ```

---

## Why this works
Discovery is handled at the **User** level via `python.venvPath` / `python.venvFolders`. Keeping the **Workspace** settings clean prevents overrides and lets the Python extension enumerate envs reliably. A project‑local `.venv` is the most robust because VS Code picks it up automatically.

