---
title: "Git Merge | Atlassian Git Tutorial"
url: https://www.atlassian.com/git/tutorials/using-branches/git-merge
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
`git merge` combines the history of two [[Git]] branches by integrating changes from a source branch into a target branch. Git supports two primary merge strategies — fast-forward and three-way (recursive) merges — chosen automatically based on branch history. Merge conflicts arise when competing changes exist in the same file and must be resolved manually before completing the merge.

## Key Points
- **Fast-forward merge**: occurs when the target branch has no divergent commits; Git simply moves the branch pointer forward, producing a linear [[Git Branch]] history.
- **Three-way merge**: used when branches have diverged; Git creates a new **merge commit** that ties together the two branch histories using a common ancestor commit.
- **Merge conflicts**: triggered when the same lines are edited differently in each branch; Git marks the file with conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) and halts until the developer resolves them.
- The standard workflow is `git checkout main` → `git merge feature-branch`; always ensure the working directory is clean (use [[git stash]] if needed) before merging.
- Merging preserves full [[version control]] history, making it easy to trace how features were integrated — contrasted with [[git rebase]], which rewrites history for a cleaner linear log.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].