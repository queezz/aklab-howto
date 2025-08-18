# Git Commit Culture

## Why it matters

Commits are not just for you — they are the history your collaborators (and your future self) will read. A clean history makes debugging and reviewing easier.

## Conventional Commits (lite)

Use a short, structured format:

```
<type>(<scope>): <subject>
```

Examples:

* `feat(vis133m): pixel/band maps + explicit time vector`
* `fix(wavecal): accept 0-based channel index`
* `docs: add quickstart`
* `chore(version): bump to 0.1.1`

**Types**: feat, fix, docs, chore, refactor, test, build, ci.
**Scope**: optional, but helps (`venv`, `mkdocs`, `wavecal`).
**Subject**: imperative, ≤72 chars.

## Commit hygiene

* One logical change per commit (atomic).
* Tiny commits are fine — they show the story.
* Push when ready → avoids spamming CI (like GitHub Pages).
* Commit body (optional): explain *why*, not just *what*.
* Breaking changes →

  ```
  BREAKING CHANGE: old flag removed; use --foo instead
  ```
* Reference issues/PRs → `Fixes #123`.

## Daily flow

```bash
# work in small commits
git add -A
git commit -m "feat(venv): add explainer draft"
git commit -m "fix(venv): typos"
git commit -m "docs(venv): reorder sections"

# clean up before pushing
git rebase -i HEAD~3   # squash/fixup
git push
```

## Squash & Amend

* **Amend last commit**:

  ```bash
  git add <files>
  git commit --amend
  ```
* **Squash multiple commits**:

  ```bash
  git rebase -i HEAD~N
  ```
* **Fixup autosquash**:

  ```bash
  git commit --fixup=<sha>
  git rebase -i --autosquash HEAD~N
  ```

---
