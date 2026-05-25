# AI Agent Workflow

Conventions for working with AI coding assistants (Cursor, Claude, and similar tools)
in AKLab repositories.

---

## Principles

- **Incremental only** — one focused change per session; review before proceeding
- **Preserve structure** — do not rename files, reorganize directories, or change URLs without explicit intent
- **No unnecessary abstraction** — add indirection only when it removes real repetition; prefer readable over clever
- **History is an asset** — keep commit history intact; avoid amending old commits
- **Figure-led docs** — when adding documentation, lead with diagrams or screenshots; prose fills context

---

## Before Any Edit Session

Activate the project venv and verify the build passes cleanly before touching anything:

=== "macOS / Linux"

    ```bash
    source ~/.venvs/<repo>/bin/activate
    mkdocs build --strict
    ```

=== "Windows (PowerShell)"

    ```powershell
    & "$env:USERPROFILE/.venvs/<repo>/Scripts/Activate.ps1"
    mkdocs build --strict
    ```

If the build fails before you start, fix it first.
Do not begin editing on a broken baseline.

---

## During Edits

- Make one logical change at a time
- Run `mkdocs build --strict` after each meaningful change
- Fix any warnings or errors before moving to the next change
- Do not add a page to `docs/` without adding it to `nav:` in `mkdocs.yml`
- Do not add a `nav:` entry without a corresponding file in `docs/`

---

## Link and Path Stability

Stable URLs are a feature. Existing links in issues, emails, notebooks, and
external references should keep working.

- Prefer filenames that will not need to change: `venv.md` rather than `python-env-complete-guide.md`
- If a page must be renamed, leave a short note at the old path pointing to the new location
- Do not silently remove anchors (`## Section Heading`) that may already be linked

---

## What to Avoid

| Avoid | Reason |
|---|---|
| Bulk renames or restructures | Breaks URLs and the site search index |
| Deleting sections without archiving | Loses historical context |
| Deep nesting in nav | Navigation becomes harder to scan |
| New abstractions without justification | Increases cognitive load |
| Large multi-topic commits | Hard to review and hard to revert |
| Undocumented changes in CI config | Makes the workflow opaque to new contributors |
| Committing `site/` | It is a build artifact; it is gitignored for a reason |

---

## Commit Style

Follow the existing commit style for the repository.
Use conventional commit prefixes where the project uses them:

| Prefix | Use for |
|---|---|
| `docs:` | Documentation changes |
| `chore:` | Maintenance: CI, config, dependencies |
| `fix:` | Corrections to existing content |
| `feat:` | New pages or sections |

---

## Build Check Reference

```bash
mkdocs build --strict
```

`--strict` promotes warnings to errors. It catches:

- Pages referenced in `nav:` but missing from `docs/`
- Internal links pointing to non-existent anchors
- Plugin or extension configuration errors

Always pass before committing.

---

## Venv Reference

For this repository:

=== "macOS / Linux"

    ```bash
    python -m venv ~/.venvs/explainers
    source ~/.venvs/explainers/bin/activate
    python -m pip install -e ".[docs]"
    ```

=== "Windows (PowerShell)"

    ```powershell
    python -m venv "$env:USERPROFILE/.venvs/explainers"
    & "$env:USERPROFILE/.venvs/explainers/Scripts/Activate.ps1"
    python -m pip install -e ".[docs]"
    ```

For other AKLab repos, replace `explainers` with the repo name.
