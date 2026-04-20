---
title: "Git Flow vs. Trunk Based Development | Toptal®"
url: https://www.toptal.com/developers/software/trunk-based-development-git-flow
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
This article compares two major [[version control]] branching strategies: [[Git Flow]] and [[Trunk-Based Development]]. Git Flow uses multiple long-lived branches for features, releases, and hotfixes, while Trunk-Based Development keeps all developers committing frequently to a single shared branch (trunk/main). The choice between them significantly impacts a team's ability to achieve [[Continuous Integration]] and [[Continuous Delivery]].

## Key Points
- **[[Git Flow]]** uses dedicated branches (`feature`, `develop`, `release`, `hotfix`, `main`) and suits teams with scheduled release cycles and multiple versions in production simultaneously.
- **[[Trunk-Based Development]]** requires all developers to commit small, frequent changes directly to the main branch, reducing [[merge conflicts]] and enabling faster feedback loops.
- Trunk-Based Development is the preferred model for [[CI/CD pipelines]] as it promotes short-lived branches and rapid integration, used by high-performing teams like Google and Facebook.
- [[Feature flags]] (feature toggles) are a key enabler of Trunk-Based Development, allowing incomplete features to be merged safely without being exposed to end users.
- Git Flow can lead to "merge hell" with long-lived branches, making it less suited for teams practising [[DevOps]] and aiming for frequent, automated deployments.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].