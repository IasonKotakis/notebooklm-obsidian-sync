---
title: "Set up Git - GitHub Docs"
url: https://docs.github.com/en/get-started/git-basics/set-up-git
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
This GitHub Docs page provides a step-by-step guide to installing and configuring [[Git]] on a local machine for use with [[GitHub]]. It covers downloading Git, setting a global username and email, and choosing an authentication method to connect to GitHub from the command line.

## Key Points
- [[Git]] must be installed locally before interacting with GitHub repositories via the terminal or command line.
- Global configuration requires setting a username and email using `git config --global` so commits are correctly attributed.
- Authentication to GitHub can be handled via [[HTTPS]] with a credential helper or via [[SSH keys]], with HTTPS recommended for beginners.
- [[GitHub CLI]] can also be used to authenticate and simplify interactions with GitHub from the command line.
- The [[Git credential manager]] can cache credentials to avoid repeated login prompts when pushing or pulling from remote repositories.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].