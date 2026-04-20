---
title: "Atlassian Git Cheat Sheet"
url: 
source_type: pdf
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
This cheat sheet from [[Atlassian]] provides a concise reference for essential [[Git]] commands across core workflows including configuration, branching, logging, diffing, undoing changes, and working with remote repositories. It covers both everyday commands and more advanced operations like rebasing and history rewriting.

## Key Points
- **Git Basics & Config**: Commands like `git init`, `git clone`, `git config --global` establish repos and set author identity; aliases can be created to shorten frequently used commands.
- **Branching & Merging**: `git branch`, `git checkout -b`, and `git merge` manage [[Git Branching]] workflows; `git rebase <base>` and `git rebase -i <base>` enable linear history rewriting via [[Git Rebase]].
- **Staging & Committing**: `git add`, `git commit -m`, and `git commit --amend` control the [[Git Staging Area]] and snapshot workflow; `git status` and `git diff` provide visibility into working directory state.
- **Undoing Changes**: [[Git Reset]] variants (`--soft`, `--hard`, per-commit) and `git revert` offer different levels of history rollback; `git reflog` helps recover lost commits.
- **Remote Repositories**: `git remote add`, `git fetch`, `git pull`, and `git push` (with flags `--force`, `--all`, `--tags`) manage synchronisation with [[Remote Git Repositories]].

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].