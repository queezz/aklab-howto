# `scaffold.py` usage

This script is a **one-shot project scaffolding tool**. It is not installed. You download it and run it directly.

---

## Workflow

### 1: Go to your new project dir

=== "macOS / Linux"

    ```bash
    mkdir ~/work/spectroview && cd ~/work/spectroview
    ```

=== "Windows (PowerShell)"

    ```powershell
    mkdir $HOME\work\spectroview; cd $HOME\work\spectroview
    ```

The project will be created relative to your current directory (or relative to the path you pass with `--path`).

### 2: Download the `scaffold.py`

=== "macOS / Linux"

    ```bash
    curl -o scaffold.py \
      https://raw.githubusercontent.com/queezz/aklab-howto/master/src/scaffold.py
    ```

=== "Windows (PowerShell)"

    ```powershell
    Invoke-WebRequest `
      -Uri https://raw.githubusercontent.com/queezz/aklab-howto/master/src/scaffold.py `
      -OutFile scaffold.py
    ```

No Git clone, no installation — just a single file.

### 3: Project properties

This scaffold defines the following project properties:

- **Creation path** — `--path` option; default is the current directory (`.`). The project is created at `<path>/<name>`. With `--here`, files go into `<path>` itself (no subdirectory).
- **In-place mode** — `--here` scaffolds into the target directory. Allowed only if the directory is empty or contains only `scaffold.py`, `.gitignore`, or `README.md`. With `--git`, `scaffold.py` is added to `.gitignore` so you can download → run once → leave the script out of the repo.
- **Project name** — Used for the folder name (unless `--here`), `pyproject.toml`, and the package under `src/<package_name>`.
- **Documentation** — `--docs` enables MkDocs structure (docs folder, mkdocs.yml, GitHub Pages workflow).
- **Git integration** — `--git` initializes a Git repository and includes the MkDocs build recipe in CI.

### 4: Run the scaffold

=== "macOS / Linux"

    ```bash
    python scaffold.py spectroview \
      --here \
      --author "Arseniy Kuzmin" \
      --email "arseniy@example.com" \
      --desc "Spectroscopic data viewer" \
      --repo-url "https://github.com/queezz/spectroview" \
      --docs
    ```

=== "Windows (PowerShell)"

    ```powershell
    python scaffold.py spectroview `
      --here `
      --author "Arseniy Kuzmin" `
      --email "arseniy@example.com" `
      --desc "Spectroscopic data viewer" `
      --repo-url "https://github.com/queezz/spectroview" `
      --docs
    ```

This scaffolds into the current directory; `.gitignore` will include `scaffold.py`.

### 5: Point agents at the fleet

Give the new project's `AGENTS.md` one fleet-context line: `RULES.md` (house rules) and `MAP.md` (sibling map) live in the `fleet` repo at `../fleet` for a project under `20-Code` ([github.com/queezz/fleet](https://github.com/queezz/fleet)).

---

## Command-line options

| Option | Description |
|--------|-------------|
| `name` | Project name (positional, required) |
| `--path PATH` | Where to create the project (default: current directory `.`) |
| `--here` | Scaffold into the target directory (no `<name>` subdirectory) |
| `--author TEXT` | Project author (default: `Your Name`) |
| `--email TEXT` | Author email (default: `you@example.com`) |
| `--desc TEXT` | Short description (default: `A short description.`) |
| `--repo-url URL` | Repository URL (default: `https://github.com/your/repo`) |
| `--license {MIT}` | License type (default: `MIT`) |
| `--git` | Initialize Git repo and make first commit |
| `--docs` | Include MkDocs configuration and docs folder |
| `--overwrite` | Overwrite existing files if present |
