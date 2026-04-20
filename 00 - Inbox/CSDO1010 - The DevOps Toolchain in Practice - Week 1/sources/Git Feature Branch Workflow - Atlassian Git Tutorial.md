---
title: "Git Feature Branch Workflow | Atlassian Git Tutorial"
url: https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
The [[Git Feature Branch Workflow]] is a branching strategy where all new features are developed in dedicated branches rather than directly on the `main` branch. This keeps the main codebase stable and enables collaboration through [[pull requests]] before any code is merged, making it a foundational practice in modern [[DevOps]] and software development teams.

## Key Points
- Each new feature or fix gets its own isolated [[Git branch]], preventing unstable code from affecting the main codebase.
- Developers push feature branches to a [[central repository]], enabling collaboration and code review without disrupting others' work.
- [[Pull requests]] (or merge requests) are used to initiate discussion, review, and approval before merging a feature branch into `main`.
- The workflow supports [[Continuous Integration]] by ensuring `main` always contains production-ready code.
- Feature branches should be descriptively named (e.g., `feature/login-page`) to communicate intent across the [[development team]].

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].