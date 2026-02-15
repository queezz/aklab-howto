# `scaffold.py` usage

This script is a **one-shot project scaffolding tool**. It is not installed. You download it and run it directly.

---

## Workflow

### 1: Go to your new project dir

```bash
cd ~/work/your-new-project
```

The project will be created relative to your current directory (or relative to the path you pass with `--path`).

### 2: Download the `scaffold.py`

```bash
curl -o scaffold.py \
  https://raw.githubusercontent.com/queezz/aklab-howto/master/src/scaffold.py
```

No Git clone, no installation — just a single file.

### 3: Project properties

This scaffold defines the following project properties:

- **Creation path** — `--path` option; default is the current directory (`.`). The project is created at `<path>/<name>`.
- **Project name** — Used for the folder name, `pyproject.toml`, and the package under `src/<package_name>`.
- **Documentation** — `--docs` enables MkDocs structure (docs folder, mkdocs.yml, GitHub Pages workflow).
- **Git integration** — `--git` initializes a Git repository and includes the MkDocs build recipe in CI.

### 4: Run the scaffold

One canonical example:

```bash
python scaffold.py my-new-project \
  --author "Montbell" \
  --desc "How to hike" \
  --docs \
  --git
```

This creates `./my-new-project` with a ready-to-use structure.

---

## Command-line options

| Option | Description |
|--------|-------------|
| `name` | Project name (positional, required) |
| `--path PATH` | Where to create the project (default: current directory `.`) |
| `--author TEXT` | Project author (default: `Your Name`) |
| `--email TEXT` | Author email (default: `you@example.com`) |
| `--desc TEXT` | Short description (default: `A short description.`) |
| `--repo-url URL` | Repository URL (default: `https://github.com/your/repo`) |
| `--license {MIT}` | License type (default: `MIT`) |
| `--git` | Initialize Git repo and make first commit |
| `--docs` | Include MkDocs configuration and docs folder |
| `--overwrite` | Overwrite existing files if present |
