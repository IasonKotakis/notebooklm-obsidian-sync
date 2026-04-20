---
title: "CSDO1010 - The DevOps Toolchain in Practice - Week 5"
tags: [seedling, notebooklm]
source: notebooklm
date: 2026-04-20
status: seedling
---

## Core Idea
CI/CD pipelines automate the integration, testing, and deployment of software to eliminate "merge hell" and accelerate delivery. The three leading tools — [[Jenkins]], [[GitHub Actions]], and [[GitLab CI]] — each represent distinct architectural philosophies: maximum flexibility, developer velocity, and integrated security respectively. Choosing between them is less about raw capability and more about Total Cost of Ownership, where human maintenance costs typically outweigh infrastructure costs.

## Key Concepts

- **[[Continuous Integration]] vs. [[Continuous Delivery]] vs. [[Continuous Deployment]]:** CI automates builds and tests on each commit; CD ensures code is always deployable to a staging environment pending manual approval; Continuous Deployment removes that final manual gate entirely.
- **[[Pipeline as Code]]:** Defining pipelines in version-controlled files (e.g., `Jenkinsfile`, `.github/workflows/*.yml`) provides a single source of truth, enables code review of pipeline logic, and maintains an audit trail.
- **Jenkins Controller-Agent model:** A central Controller handles scheduling and configuration while Agents (VMs, containers, or Kubernetes pods) execute jobs. Ephemeral agents are spun up per job and destroyed immediately after, improving isolation and resource efficiency.
- **[[GitLab CI]] Merge Trains:** Queue merge requests and test each against the combined state of all preceding items in the queue, preventing race conditions where individually passing branches break `main` on merge.
- **[[DevSecOps]] and Shifting Left:** GitLab CI embeds SAST, DAST, and Secret Detection directly into the pipeline, moving security review into the development loop rather than a separate post-build gate.
- **Total Cost of Ownership (TCO):** Self-hosted Jenkins requires 1–2 FTE for plugin and OS maintenance; SaaS options (GitHub Actions, GitLab CI) shift cost to per-minute or per-user pricing with minimal maintenance overhead — a critical distinction for smaller teams.
- **Supply Chain Risk in [[GitHub Actions]]:** Third-party Marketplace actions have access to repository secrets; best practice is to pin actions to a specific commit SHA rather than a floating tag to prevent dependency hijacking.

## Connections
The CI/CD pipeline is a practical instantiation of [[DevOps]] culture — it operationalises the feedback loops described in [[The Three Ways of DevOps]]. The TCO analysis connects to [[FinOps]] principles, and the security-embedding approach links directly to [[Shift Left Testing]] and broader [[Supply Chain Security]] concerns increasingly tracked via [[SBOM]] (Software Bill of Materials).

## Questions This Raises

- At what team size does the operational overhead of self-hosted Jenkins become justified over SaaS alternatives — and how does that calculation change with Kubernetes-native Jenkins?
- How should a migration from Jenkins to GitHub Actions handle pipelines that require access to on-premises databases or internal network resources?
- As [[Auto DevOps]] matures, does zero-config CI/CD risk obscuring pipeline logic from developers who then can't debug or optimise it?
- What governance model should an organisation adopt for approving and auditing third-party [[GitHub Actions]] from the Marketplace?
- How do "elite performer" metrics from the [[State of DevOps Report]] translate into concrete pipeline design decisions for teams currently at "low performer" status?