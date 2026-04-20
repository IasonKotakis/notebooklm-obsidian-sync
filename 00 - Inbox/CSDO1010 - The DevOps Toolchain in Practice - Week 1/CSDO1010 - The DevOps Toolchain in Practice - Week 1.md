---
title: "CSDO1010 - The DevOps Toolchain in Practice - Week 1"
tags: [seedling, notebooklm]
source: notebooklm
date: 2026-04-20
status: seedling
---

## Core Idea
Version control is the invisible scaffolding of modern software development. [[Git]], built by [[Linus Torvalds]] in 2005 as a distributed system, solved the chaos of centralized file-locking workflows by giving every developer a complete local history secured by a cryptographic chain of SHA1 hashes. The choice of branching workflow — from [[Git Flow]] to [[Trunk-Based Development]] — reflects not just technical preference but a team's culture, risk tolerance, and engineering maturity.

## Key Concepts

- **Evolution of VCS generations:** Systems moved from single-file locking (RCS) → multi-file merging with centralized servers (SVN, CVS) → distributed commit-before-merge architectures (Git, Mercurial). The critical shifts were abandoning file locks in favour of merging, and distributing the full repository history to every developer.
- **Git's immutable ledger:** Every commit is a complete snapshot of the project tree, chained via a [[Directed Acyclic Graph]] where each node stores the SHA1 hash of its parent. Altering any past commit breaks the hash chain, making tampering immediately detectable — an "unhackable chain of custody."
- **The staging area as curation:** The index is not bureaucratic overhead but a deliberate space to assemble atomic, focused commits from a messy working directory. Clean commits create readable history, which is critical for post-incident debugging in a [[CI/CD]] pipeline.
- **Branching as a lightweight pointer:** A Git branch is simply a 40-character SHA1 checksum in a text file — a Post-it note on the graph. Creating one costs zero bytes, making parallel development instantaneous rather than a multi-gigabyte copy operation.
- **[[Git Flow]] vs [[Trunk-Based Development]]:** Git Flow uses two eternal branches (`main` + `develop`) plus support branches, making it suitable for scheduled enterprise releases and regulated software but incompatible with continuous delivery. Trunk-Based Development collapses this to a single `main` branch with tiny, frequent commits, requiring [[Feature Flags]] to decouple deployment from release and ironclad automated testing as the safety net.
- **[[GitHub Flow]] as middle ground:** Short-lived feature branches, [[Pull Requests]] for review, and an assumption that `main` is always production-ready. Pull requests are not just gatekeeping — they are asynchronous mentorship and shared code ownership baked into the workflow.
- **The Forking Workflow and zero-trust open source:** Contributors copy the entire repository server-side (a fork) rather than receiving write access to the central repo. This is the architecture that enabled large open-source projects like Linux and Kubernetes to accept contributions from strangers safely.

## Connections

The shift from [[Git Flow]] to [[Trunk-Based Development]] is inseparable from the rise of [[CI/CD]] pipelines and [[DevOps]] culture — continuous integration only works if developers are actually integrating continuously. The underlying cryptographic structure of Git (Merkle trees, SHA1 hashing) also connects directly to [[Blockchain]] architecture, raising questions about applying version-controlled, tamper-evident ledgers beyond code to legal documents and legislation.

## Questions This Raises

- At what team size or codebase complexity does Trunk-Based Development become impractical, even with mature automation?
- How should a team manage the technical debt of accumulated [[Feature Flags]] as a product scales — when do they become more dangerous than long-lived branches?
- What level of automated test coverage is actually the minimum viable threshold before a team can safely adopt trunk-based workflows?
- Could the Git DAG / Merkle tree model be meaningfully applied to legal or governmental document management, and what would the governance layer look like?
- How do organisations transitioning from Git Flow to Trunk-Based Development manage the cultural shift, particularly around relinquishing the review-gate safety net?

## Resources

- Video Overview: [[07 - Sources/CSDO1010 - The DevOps Toolchain in Practice - Week 1/video_overview.mp4]]