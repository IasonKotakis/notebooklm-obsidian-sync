---
title: "GitHub Git Cheat Sheet"
url: 
source_type: PDF
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
A quick-reference cheat sheet for commonly used [[Git]] command line instructions, covering setup, repository management, branching, synchronisation, and undoing changes. Also introduces key [[GitHub]] concepts and the [[GitHub Flow]] branching workflow.

## Key Points
- **Configure & Create**: Use `git config` to set user identity, `git init` to create a new [[Git Repository]], and `git clone` to copy an existing remote repository including all branches and commits.
- **Branching**: [[Git Branches]] are lightweight pointers to commits; use `git branch`, `git checkout`, and `git merge` to create, switch, and combine branches — central to the [[GitHub Flow]] model.
- **Synchronise Changes**: `git fetch` downloads remote history, `git merge` integrates it, and `git push` uploads local commits — `git pull` combines fetch and merge in one step.
- **Staging & Committing**: `git add` snapshots files into the [[Staging Area]], and `git commit` permanently records them in version history with a descriptive message.
- **Undo & History**: `git reset` can undo commits (preserving or discarding local changes), while `git log` and `git diff` allow inspection of project history; the [[.gitignore]] file excludes specified files from tracking.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].