---
title: "git-cheat-sheet.pdf"
url: 
source_type: PDF
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
A comprehensive reference sheet covering essential [[Git]] commands organised by workflow stage. It covers configuration, daily development tasks, branching, history inspection, and remote synchronisation. Key concepts include the [[Git Staging Area]], [[Git Branching]], and reverting changes safely.

## Key Points
- **Configuration & Setup**: Use `git config` to set user identity; `git init` or `git clone` to start a project.
- **Day-to-day workflow**: `git add`, `git commit`, `git status`, and `git diff` form the core loop; [[.gitignore]] controls untracked files.
- **Branching & Merging**: `git branch`, `git checkout`, `git merge`, and `git rebase` manage parallel lines of development; [[Git Rebase]] linearises history.
- **Stashing**: `git stash` / `git stash pop` temporarily shelves uncommitted work without committing it.
- **Remote Synchronisation**: `git fetch`, `git pull`, and `git push` manage communication with [[Remote Repositories]]; tags can be pushed with `--tags`.
- **Reverting Changes**: `git revert` safely undoes a commit by creating a new inverse commit; `git reset --hard` discards changes but is destructive.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].