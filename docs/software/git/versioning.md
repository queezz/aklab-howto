
# Versioning & Releases

## Semantic Versioning (SemVer)

We use **MAJOR.MINOR.PATCH**:

* **MAJOR** → breaking changes.
  *Remove a function, change API.*
* **MINOR** → new features, backwards-compatible.
  *Add function, optional args, new docs.*
* **PATCH** → bug fixes, backwards-compatible.
  *Fix bug, typo, refactor.*

Examples:

* `1.4.2` → major 1, minor 4, patch 2.
* `2.0.0` → breaking changes.
* `2.1.0` → new features.
* `2.1.1` → bug fix.

---

## Tagging a release

```bash
git add -A
git commit -m "chore(version): bump to 0.1.1"
git tag -a v0.1.1 -m "v0.1.1"
git push --follow-tags
```

👉 Keep tag = version in `pyproject.toml`.

---

## Installing from a Git tag

```bash
pip install "git+https://github.com/you/yourrepo@v0.1.1"
```

---

## Fixing a mistaken tag

```bash
git tag -d v0.1.1
git push origin :refs/tags/v0.1.1
# re-tag the correct commit
git tag -a v0.1.1 -m "v0.1.1" <commit>
git push origin v0.1.1
```