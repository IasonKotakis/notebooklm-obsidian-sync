---
title: "Git Workflow | Atlassian Git Tutorial"
url: https://www.atlassian.com/git/tutorials/comparing-workflows#centralized-workflow
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
This Atlassian tutorial compares the major [[Git]] workflows used by software development teams, explaining how each structures collaboration around a shared codebase. It covers the [[Centralized Workflow]], [[Feature Branch Workflow]], [[Gitflow Workflow]], and [[Forking Workflow]], helping teams choose the right strategy based on their size and release process.

## Key Points
- The **[[Centralized Workflow]]** uses a single shared repository and `main` branch — simple but prone to conflicts in larger teams.
- The **[[Feature Branch Workflow]]** isolates new development on dedicated branches, enabling [[pull requests]] and code review before merging into `main`.
- The **[[Gitflow Workflow]]** introduces structured `develop`, `release`, and `hotfix` branches, suited for projects with scheduled release cycles.
- The **[[Forking Workflow]]** gives each developer their own server-side repository, common in open-source projects to maintain a clean authoritative codebase.
- Choosing the right workflow depends on team size, release cadence, and how much isolation between features is needed in the [[DevOps]] pipeline.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].