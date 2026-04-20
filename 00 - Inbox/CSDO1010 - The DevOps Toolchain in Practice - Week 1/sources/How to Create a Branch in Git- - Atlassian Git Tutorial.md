---
title: "How to Create a Branch in Git? | Atlassian Git Tutorial"
url: https://www.atlassian.com/git/tutorials/using-branches
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
Git branches allow developers to work on isolated lines of development without affecting the main codebase. Each branch represents an independent snapshot of changes, enabling parallel workflows for features, bug fixes, and experiments. Branches are lightweight and cheap to create, making them a core part of everyday [[Git]] workflows.

## Key Points
- A [[Git branch]] is essentially a pointer to a specific commit, allowing divergent development paths to coexist in the same repository.
- The `git branch` command is used to create, list, rename, and delete branches; `git checkout` or `git switch` is used to navigate between them.
- [[Feature branching]] isolates new work from the stable codebase, reducing risk and enabling [[code review]] before merging.
- [[git merge]] and [[git rebase]] are the two primary strategies for integrating branch changes back into the main line.
- Deleting a branch after merging is considered best practice to keep the repository clean; the `-d` flag safely deletes only merged branches.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].