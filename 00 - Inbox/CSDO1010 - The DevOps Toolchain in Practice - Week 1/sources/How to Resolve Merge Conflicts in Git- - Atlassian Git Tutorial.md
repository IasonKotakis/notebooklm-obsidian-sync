---
title: "How to Resolve Merge Conflicts in Git? | Atlassian Git Tutorial"
url: https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
[[Git merge conflicts]] occur when two branches have made competing changes to the same part of a file, and Git cannot automatically determine which version to keep. Conflicts must be manually resolved by the developer before the merge can be completed. Understanding how to identify, interpret, and resolve conflicts is an essential skill for collaborative version control.

## Key Points
- [[Git merge conflicts]] arise most commonly when two developers edit the same line of a file, or when one deletes a file that another has modified.
- Git marks conflicted areas in files using conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), indicating the changes from each [[branch]].
- To resolve a conflict, the developer must manually edit the file to choose or combine the conflicting changes, then stage the file with `git add` and complete the [[git merge]] with `git commit`.
- Tools like `git status` help identify which files are in conflict, and visual [[merge tools]] (e.g., `git mergetool`) can assist in resolution.
- The best way to minimise conflicts is through good team communication, frequent integration via [[feature branching]], and keeping branches short-lived.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].