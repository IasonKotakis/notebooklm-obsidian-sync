---
title: "CSDO1010 - The DevOps Toolchain in Practice - Week 2"
tags: [seedling, notebooklm]
source: notebooklm
date: 2026-04-20
status: seedling
---

## Core Idea
[[HashiCorp Terraform]] operationalises [[Infrastructure as Code]] by letting engineers declare a desired end-state in HCL files and then automatically reconciling real-world cloud resources to match that state. This declarative, idempotent approach replaces fragile manual workflows and mutable server management with a reproducible write → plan → apply cycle that scales from a solo developer to an enterprise of hundreds via remote state, reusable modules, and policy-as-code guardrails.

## Key Concepts
- **Declarative vs. imperative provisioning:** Terraform describes *what* the infrastructure should look like, not *how* to build it step-by-step. Like hailing a taxi rather than driving yourself, you declare the destination and the engine figures out the route — making runs safely [[idempotent]].
- **The core workflow — Write, Plan, Apply:** `terraform plan` acts as a "shopping cart review", diffing desired state against reality before a human approves; `terraform apply` then fires the API calls. `terraform init`, `fmt`, `validate`, `output`, and `destroy` round out the essential CLI surface.
- **State file and configuration drift:** `terraform.tfstate` is Terraform's source of truth. During the hidden *refresh* phase before every plan, Terraform queries live APIs to detect [[configuration drift]] (e.g., a VM deleted via the cloud portal) and corrects it on apply. State files can contain secrets and must never sit in public version control.
- **Mutable vs. [[immutable infrastructure]]:** Rather than patching a running server in-place (risking "version 1.56" Frankenstein states), immutable infrastructure destroys the old resource and provisions a clean replacement. This only works safely when compute is kept stateless and data is externalised to a shared persistent store.
- **Providers and modules:** [[Terraform Providers]] are plugins that translate HCL into vendor-specific API calls (AWS, Azure, GitHub, Cloudflare, etc.). [[Terraform Modules]] are reusable black-box templates that let non-expert developers consume pre-approved architectural patterns by supplying a handful of input variables.
- **Remote state and collaboration:** [[HCP Terraform]] stores the state file centrally, encrypts secrets, and applies state locking so concurrent `apply` runs queue rather than collide — solving the "Alice and Bob" race-condition problem.
- **[[Policy as Code]] with Sentinel:** [[Sentinel]] intercepts the JSON execution plan before apply and evaluates it against organisation-wide rules (region restrictions, cost caps, firewall prohibitions). Compliant plans are auto-approved; violations are hard-blocked, enabling developer self-service without sacrificing governance.

## Connections
The write/plan/apply workflow parallels [[GitOps]] pull-request review cycles, and the workspace-per-environment pattern mirrors [[microservices]] ownership boundaries in software architecture. Sentinel's automated policy gates connect directly to [[DevSecOps]] practices, where security is shifted left into the pipeline rather than enforced after the fact by human ticket queues.

## Questions This Raises
- How should teams handle *data migration* when adopting fully immutable infrastructure — particularly stateful workloads like relational databases that cannot simply be destroyed and recreated?
- At what point does module abstraction become a liability? If junior developers never read the underlying HCL, do they lose the conceptual understanding needed to debug production incidents?
- [[Sentinel]] stops bad plans before apply, but what mechanisms exist for *detecting and alerting* on drift that occurs between Terraform runs in a long-lived environment?
- How do version constraints in `required_providers` interact with an organisation's internal module registry — who owns the upgrade lifecycle across dozens of workspace consumers?
- If the declarative-reset-button philosophy extends beyond IT (smart buildings, HR processes, legal contracts as mentioned in the audio), what are the ethical and governance risks of treating human-facing systems as infrastructure to be "snapped back" to a desired state?