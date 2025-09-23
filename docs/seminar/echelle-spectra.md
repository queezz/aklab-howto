# Echelle Project: Overview & Playbook

## 1. The problem — why your current workflow hurts

### Typical anti-patterns (“BS”) we keep seeing

```python
# ❌ BS
sen10 = S(cb_ylist[0]); sen11 = S(cb_ylist[1]); ... sen23 = S(cb_ylist[13])
# ✅ Do
sen_by_order = [S(wl) for wl in cb_ylist]
```

```python
# ❌ BS
coef_10 = sen10/(sphere[10]-back[10]); coef_11 = ...
# ✅ Do
coef_by_order = [sen/(s-b) for sen, s, b in zip(sen_by_order, sphere_list, back_list)]
```

* **Calibration logic shoved into a notebook** (polyfit, borders, stitching) → impossible to reuse/test.
* **Calibration data hardcoded in a notebook** (e.g., wave/sen arrays) instead of a **file with metadata**:

```text
# data/calibration/sphere_2025-01-23.csv
# instrument: Fujii Echelle A
# sphere: Labsphere XYZ, SN12345
# date: 2025-01-23
# location: Room 301 dark lab
# author: K. Student
wavelength_nm,sensitivity_W_m2_sr_nm_per_count
300,1.85e4
310,2.8e4
...
```

Then read with:

```python
arr = np.loadtxt(path, delimiter=",", comments="#", skiprows=0)
```

## 2. The sane project shape — mix notebooks + package

Use **notebooks for exploration**, **package for logic**.

```text
echelle-project/
  pyproject.toml
  src/echelle_pkg/                 # ← all reusable code lives here
    __init__.py
    calibration.py                 # sensitivity, borders, stitching
    io.py                          # loaders
    profiles.py                    # per-instrument settings
  data/
    calibration/                   # CSVs with comment headers
  examples/                        # shareable demo notebooks
    01_quickstart.ipynb
    02_absolute_calibration.ipynb
  local/                           # ignored scratch area (in .gitignore)
    2025-09-poster/                # your day’s work, ad hoc plots
  docs/                            # add after code steadies
  .gitignore                       # includes /local/
```

### Install the package in editable mode

Choose venv or poetry; venv is fine.

```bash
python -m venv ~/.venvs/echelle
source ~/.venvs/echelle/bin/activate  # (Windows: Scripts/Activate.ps1)
python -m pip install -U pip wheel
pip install -e ".[dev]"               # uses pyproject.toml
```

Poetry (if a student prefers):

```bash
poetry install
poetry shell
```

Because it’s **editable**, you can work **anywhere** (e.g., `~/workbench/2025-09-poster/`) and still:

```python
from echelle_pkg.calibration import fit_sensitivity_poly, stitch_orders
```

## 3. Daily usage pattern — what students should do

* **Prototype in `local/`** or any external folder → import the installed package.
* Keep notebooks **thin**: plotting, quick checks, and calls like:

```python
from echelle_pkg.profiles import load_profile
from echelle_pkg.calibration import run_absolute_calibration

prof = load_profile("data/calibration/profiles/fujii-2025.json")
factors = run_absolute_calibration(images, profile=prof)
```

* New spectrometer / camera / processing?

  1. **Prototype** in `local/`
  2. **Wrap** into a function/class in `src/echelle_pkg/`
  3. Add/adjust a **profile JSON** (orders, pixel geometry, poly degree, file paths)
  4. Add a **minimal test** in `tests/`
  5. Add a **usage notebook** in `examples/`

## 4. Git hygiene — small, readable history

* **Branches** per task:
  `git switch -c feat/abs-calibration-profiles`
* **Commits** are small and named for the change:
  `feat(calib): add profile loader`
  `fix(stitch): skip orders without λ-calibration`
  `docs(calib): note sphere CSV header fields`
* **Tags** for stable points:
  `git tag -a v0.3.0 -m "absolute calibration rework"`
* You **don’t** have to push every commit. Push at the end of the day or when a unit of work is done.

## 5. Docs when it stabilizes — mkdocs, minimal

Add docs after the dust settles:

* `docs/` with short pages:

  * **Quickstart** (install, one example)
  * **Calibration data spec** (CSV header, units, example)
  * **Profiles** (how orders/geometry are encoded)
  * **API** (one page, function signatures)
* `mkdocs.yml` nav that links examples notebooks (rendered or linked).

## 6. Side-by-side — BS vs possible

### Manual notebook soup (BS)

```python
# fit poly, hand-pick orders, repeat slices, concatenate, sort...
sen_10 = S(cb_ylist[0]); sen_11 = S(cb_ylist[1]); ...
coef_10 = sen_10/(sphere[10]-back[10]); ...
x = np.concatenate((raman[0][171:1749], raman[1][188:1431], ...))
y = np.concatenate((cb10[171:1749], cb11[188:1431], ...))
```

### Package-first (possible)

```python
# src/echelle_pkg/calibration.py
def sensitivity_from_csv(path, deg=6):
    arr = np.loadtxt(path, delimiter=",", comments="#")
    return np.poly1d(np.polyfit(arr[:,0], arr[:,1], deg))

def coefficients(image, background, S, orders=None):
    # auto-borders + skip NaN-λ orders inside
    x, s = stitch_orders(image, orders=orders)
    _, b = stitch_orders(background, orders=orders)
    y = s - b
    return x, S(x) / np.clip(y, 1e-12, None)

# examples/02_absolute_calibration.ipynb
S = sensitivity_from_csv("data/calibration/sphere_2025-01-23.csv", deg=6)
x_nm, coef = coefficients(sphere_img, back_img, S, orders=[10,11,12,13,14,15,16,17,18,19,20,21,22])
```

## 7. Message

* **Notebooks are for exploration and visualization.**
  All reusable logic must live in `src/echelle_pkg/`.
* **Calibration data is a file with a header**, not literals in a cell.
  If it isn’t in `data/calibration/…csv` with a comment header, it doesn’t exist.
* **Instrument differences go into a profile JSON**, not into copied code.
* **Commit small, often;** tag stable points; push when a unit of work is complete.
* **If you wrote the same line twice, you need a loop or a function.**

## 8. Minimal `pyproject.toml` you can reuse

```toml
[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "echelle-pkg"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["numpy", "scipy", "matplotlib", "tifffile", "pillow"]

[project.optional-dependencies]
dev = ["pytest", "ruff", "black"]

[project.scripts]
echelle-cli = "echelle_pkg.cli:main"

[tool.setuptools.packages.find]
where = ["src"]
include = ["echelle_pkg*"]
```

## Encouragement

> **شُوَيَّة شُوَيَّة تبني جبل**
> 
> *Shuyyat shuyyat tabni jabal* — Little by little, you build a mountain.
