---
title: "Gitflow Workflow | Atlassian Git Tutorial"
url: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
Gitflow is a [[Git branching strategy]] originally proposed by Vincent Driessen that defines a strict branching model designed around project releases. It assigns specific roles to different branches and defines how and when they should interact, making it well-suited for projects with scheduled release cycles.

## Key Points
- **Two primary branches**: `main` (production-ready code) and `develop` (integration branch for features), both with infinite lifetimes.
- **Supporting branch types**: [[Feature branches]] branch off `develop` and merge back into it; [[Release branches]] branch from `develop` and merge into both `main` and `develop`; [[Hotfix branches]] branch directly from `main` for urgent production fixes.
- **Version tagging**: Every merge into `main` is tagged with a version number, providing a clear audit trail of production releases.
- **Isolation of work**: Feature branches keep new development isolated from the stable `develop` branch until ready, supporting parallel development without interference.
- **Gitflow is less suited for [[Continuous Delivery]]** workflows; simpler strategies like [[Trunk-Based Development]] may be preferred for teams deploying frequently.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].