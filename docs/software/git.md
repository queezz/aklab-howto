# Commits & Tags

## Minimal commit style (Conventional Commits lite)
- `feat(vis133m): pixel/band maps + explicit time vector`
- `fix(wavecal): accept 0-based channel index`
- `docs: add quickstart`
- `chore(version): bump to 0.1.1`

Keep subjects short (≤72 chars).

## Tag a release
```
git add -A
git commit -m "chore(version): bump to 0.1.1"
git tag -a v0.1.1 -m "v0.1.1"
git push --follow-tags
```

## Install from a Git tag (no PyPI)
```
pip install "git+https://github.com/you/yourrepo@v0.1.1"
```

## Fix a mistaken tag
```
git tag -d v0.1.1
git push origin :refs/tags/v0.1.1
# re-tag the right commit, then push again
git tag -a v0.1.1 -m "v0.1.1" <commit>
git push origin v0.1.1
```

