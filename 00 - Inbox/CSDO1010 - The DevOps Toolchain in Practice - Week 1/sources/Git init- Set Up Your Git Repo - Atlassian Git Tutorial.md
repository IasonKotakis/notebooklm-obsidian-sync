---
title: "Git init: Set Up Your Git Repo | Atlassian Git Tutorial"
url: https://www.atlassian.com/git/tutorials/setting-up-a-repository
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
This Atlassian tutorial covers the foundational commands for setting up a [[Git]] repository, including `git init`, `git clone`, `git config`, and `git alias`. It explains how to initialise a new local repository, clone an existing one, and configure user settings essential for version control workflows.

## Key Points
- `git init` creates a new [[Git repository]] in the current directory, generating a hidden `.git` folder that tracks all version history and configuration.
- `git clone <url>` copies an existing [[remote repository]] (e.g., from [[Bitbucket]] or GitHub) to your local machine, including its full commit history.
- `git config` is used to set identity details (name, email) and preferences at the local, global, or system level — critical for attributing [[commits]] correctly.
- [[Git aliases]] can be defined via `git config` to create shortcuts for frequently used commands, improving developer workflow efficiency.
- Initialising or cloning a repo are the two standard entry points before using [[version control]] in any project.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].