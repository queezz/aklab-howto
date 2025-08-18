# Git Intro

## What is Git?

Git is a **version control system** — it keeps a timeline of your project. Every *commit* is a snapshot you can revisit, compare, or branch off. Think of it as a **time machine for code and docs**.

## What is GitHub?

GitHub is a service that hosts Git repositories and adds:

* **Collaboration** (issues, pull requests, reviews).
* **Automation** (GitHub Actions).
* **Hosting** (GitHub Pages — what powers this site).

There are alternatives: **GitLab, Bitbucket, Gitea, SourceHut…**.
We’re living on GitHub because it’s the standard, and GitHub Pages makes publishing easy.

## First steps

When you create a repo on GitHub, it shows you a block of ready-to-use commands (init, add remote, push). Copy those into your shell the first time. After that, your daily flow is just:

```bash
git add -A
git commit -m "message"
git push
```

---