---
title: "Fork a repository - GitHub Docs"
url: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
A [[GitHub]] fork is a personal copy of another user's repository that shares code and visibility settings with the original [[upstream repository]]. Forking allows developers to freely experiment with changes without affecting the original project, and is fundamental to open-source [[collaborative development]] workflows.

## Key Points
- A [[fork]] creates a new repository under your account that is linked to the original upstream repository, enabling you to propose changes back via [[pull requests]].
- After forking on GitHub, you typically [[clone]] the fork locally using `git clone` to begin working with the code.
- It is best practice to configure the original repository as a [[remote]] (called `upstream`) so you can sync future changes from the source project into your fork.
- Forks are commonly used in [[open-source contribution]] workflows: fork → clone → branch → commit → pull request.
- [[GitHub CLI]] (`gh repo fork`) can be used as an alternative to the web browser to fork and clone a repository in one step.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].