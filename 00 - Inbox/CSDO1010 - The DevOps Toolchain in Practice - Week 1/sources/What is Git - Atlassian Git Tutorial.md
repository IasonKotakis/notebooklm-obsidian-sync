---
title: "What is Git | Atlassian Git Tutorial"
url: https://www.atlassian.com/git/tutorials/what-is-git
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
[[Git]] is a free, open-source [[distributed version control system]] (DVCS) originally created by [[Linus Torvalds]] in 2005 for managing Linux kernel development. Unlike older [[centralised version control systems]], Git gives every developer a full local copy of the repository, including its complete history. Git has become the de facto standard for [[version control]] in modern software development.

## Key Points
- **Distributed architecture**: Every developer's working copy is a full repository backup, enabling offline work and eliminating single points of failure — unlike centralised systems such as [[SVN]] or [[CVS]].
- **Performance**: Git operations (commits, branches, merges) are performed locally, making them extremely fast; its [[branching and merging]] model is lightweight and efficient.
- **Branching model**: Git's cheap local branching encourages [[feature branch workflows]], enabling teams to isolate work, experiment, and merge safely without disrupting the main codebase.
- **Data integrity**: Every file and commit is checksummed with [[SHA-1]] hashing, ensuring the history cannot be silently corrupted.
- **Wide adoption**: Git underpins major platforms like [[GitHub]], [[Bitbucket]], and [[GitLab]], and integrates tightly into modern [[CI/CD]] pipelines and [[DevOps]] toolchains.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].