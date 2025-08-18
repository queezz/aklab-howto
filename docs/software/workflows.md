# Workflows

This page consolidates release and development workflows.

## Releases without PyPI
Flow
- Bump version in `pyproject.toml` (SemVer).
- Commit and tag:
  ```bash
  git commit -am "chore(version): bump to X.Y.Z"
  git tag -a vX.Y.Z -m "vX.Y.Z"
  git push --follow-tags
  ```
- Install from tag where needed:
  ```bash
  pip install "git+https://github.com/you/yourrepo@vX.Y.Z"
  ```

Pre-releases
- Tags like `v0.2.0-alpha.1`, `v0.2.0-rc.1` are fine.
- Consumers can pin those tags explicitly.

Optional: auto-version from tags
Use `setuptools_scm`:
```toml
[project]
dynamic = ["version"]

[tool.setuptools_scm]
write_to = "yourpkg/_version.py"
```


