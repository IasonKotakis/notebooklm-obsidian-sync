---
title: "What Is a Git Fork? | Atlassian Git Tutorial"
url: https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow
source_type: web_page
tags: [seedling, source]
date: 2026-04-20
status: seedling
notebook: "[[CSDO1010 - The DevOps Toolchain in Practice - Week 1]]"
---

## Core Content
A [[Git Fork]] is a server-side copy of a repository, distinct from a [[Git Branch]], allowing developers to work independently without affecting the original project. The [[Forking Workflow]] is commonly used in open-source projects and enables contributors to propose changes via [[Pull Request]] without needing direct write access to the upstream repository.

## Key Points
- **Forking vs. Cloning**: Forking creates a copy on the server (e.g., [[Bitbucket]] or [[GitHub]]), while cloning creates a local copy; both are needed to work on a forked project.
- **No direct write access required**: Contributors fork a repo, make changes in their copy, then submit a [[Pull Request]] to the original maintainer for review and merging.
- **Isolation and safety**: The [[Forking Workflow]] keeps the official codebase clean — contributors cannot push directly to it, making it ideal for large-scale [[Open Source Collaboration]].
- **Integration with CI/CD**: Forks work alongside tools like [[Bitbucket Pipelines]] to enable automated testing before changes are merged into the main repository.
- **Common in [[DevOps]] workflows**: Forking supports distributed team collaboration and is a foundational pattern in modern [[Version Control]] practices.

## Back to Notebook
Part of [[CSDO1010 - The DevOps Toolchain in Practice - Week 1]].