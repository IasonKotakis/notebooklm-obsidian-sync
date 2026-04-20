---
title: "How to Install Git? | Atlassian Git Tutorial"
url: https://www.atlassian.com/git/tutorials/install-git
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
This Atlassian tutorial covers how to install [[Git]] across multiple operating systems including Windows, macOS, and Linux. It also explains essential post-installation configuration steps such as setting a username and email using `git config`, which are required before making commits.

## Key Points
- [[Git]] can be installed on **Linux** via package managers (e.g., `apt-get install git` on Debian/Ubuntu)
- On **macOS**, Git can be installed via [[Homebrew]] (`brew install git`) or via Xcode Command Line Tools
- On **Windows**, Git is installed using the [[Git for Windows]] installer (also called Git Bash), which provides a Unix-like terminal environment
- After installation, global identity configuration is required: `git config --global user.name` and `git config --global user.email`
- The `git config` command manages settings stored in a `.gitconfig` file, enabling consistent [[version control]] identity across all repositories on a machine

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].