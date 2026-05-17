# Lab How-To

A practical handbook of lab workflows, notes, and recipes, published as a MkDocs documentation site.

The site collects reusable procedures for experimental and computational work: hardware, software, KiCad, devices, lab tools, project setup, and other things worth writing down once instead of rediscovering later.

[→ Open the docs site](https://queezz.github.io/aklab-howto/)

## Highlights

- Copy-pasteable workflows and setup notes
- Lab hardware and device documentation
- Software environment and tooling recipes
- KiCad and electronics notes
- Python project scaffolding helper

For Python project scaffolding, see:

[scaffold.py usage](https://queezz.github.io/aklab-howto/software/scaffold/)


## Venv
```powershell
python -m venv "$env:USERPROFILE/.venvs/explainers" 
```

```powershell
& "$env:USERPROFILE/.venvs/explainers/Scripts/Activate.ps1"
```

```powershell
python -m pip install -e ".[docs]"
```