---
title: "Git Quiz - Quiz"
tags: [seedling, notebooklm, quiz]
source: notebooklm
date: 2026-04-20
status: seedling
---

# Git Quiz - Quiz

## Question 1

Which generation of version control systems introduced the 'commit before merge' distributed philosophy seen in tools like Git?

- **A.** First Generation
- **B.** Second Generation
- **C.** Third Generation
- **D.** Fourth Generation

> [!answer]- Answer
> **C.** Third Generation
>
> **Hint:** Think about the progression from file locking to centralized merging, and finally to distributed systems.

## Question 2

In the Git Flow development model, what is the primary purpose of the 'develop' branch?

- **A.** To store the official, production-ready release history
- **B.** To serve as the main integration branch for all completed features
- **C.** To provide a dedicated space for urgent production bug fixes
- **D.** To act as a short-lived branch for individual developer experimentation

> [!answer]- Answer
> **B.** To serve as the main integration branch for all completed features
>
> **Hint:** Consider which branch acts as the ongoing 'staging' area for the next scheduled release.

## Question 3

Why is trunk-based development often recommended for senior-heavy teams working on a Minimum Viable Product (MVP)?

- **A.** It provides strict access control to prevent mistakes by inexperienced staff
- **B.** It ensures a long and thorough code review process for every line of code
- **C.** It offers maximum development speed by reducing bureaucratic processes
- **D.** It is the standard requirement for running large-scale open-source projects

> [!answer]- Answer
> **C.** It offers maximum development speed by reducing bureaucratic processes
>
> **Hint:** Focus on the balance between team autonomy and the need for rapid iteration in a startup context.

## Question 4

What condition must be met for Git to perform a 'fast-forward' merge?

- **A.** The branches must have diverged histories with unique commits on both sides
- **B.** There must be a linear path from the current branch tip to the target branch tip
- **C.** The merge must be performed on a remote repository rather than a local one
- **D.** The developer must manually resolve all conflicts before the merge begins

> [!answer]- Answer
> **B.** There must be a linear path from the current branch tip to the target branch tip
>
> **Hint:** Consider the geometric relationship between two branch pointers that haven't branched away from each other's path.

## Question 5

Which Git command is functionally a combination of `git fetch` and `git merge`?

- **A.** `git push`
- **B.** `git pull`
- **C.** `git checkout`
- **D.** `git remote`

> [!answer]- Answer
> **B.** `git pull`
>
> **Hint:** Identify the command that handles both the synchronization of data and the updating of the local branch history in one step.

## Question 6

In the context of Git configuration, which scope should be used to define settings that apply to all repositories for a specific user on a machine?

- **A.** Local
- **B.** Global
- **C.** System
- **D.** Remote

> [!answer]- Answer
> **B.** Global
>
> **Hint:** Think about the flag used to set your name and email when you first install Git.

## Question 7

When a 3-way merge fails due to conflicting changes, which marker does Git use to separate the content from the 'receiving' branch and the 'merging' branch within the file?

- **A.** `*******`
- **B.** `=======`
- **C.** `-------`
- **D.** `|||||||`

> [!answer]- Answer
> **B.** `=======`
>
> **Hint:** Look for the visual indicator that acts as a horizontal line between the two versions of the code.

## Question 8

What is the primary benefit of using 'annotated' tags (`git tag -a`) instead of 'lightweight' tags?

- **A.** Annotated tags are stored as full objects containing the tagger's name, email, and date
- **B.** Annotated tags allow the developer to delete the branch history while keeping the tag
- **C.** Only annotated tags can be used to trigger automated deployment pipelines
- **D.** Annotated tags are required to perform a fast-forward merge

> [!answer]- Answer
> **A.** Annotated tags are stored as full objects containing the tagger's name, email, and date
>
> **Hint:** Consider which tag type provides more metadata for official release documentation.

## Question 9

In the legacy Git Flow model, which branch is the only one that should fork directly off of the 'main' branch?

- **A.** Feature branch
- **B.** Release branch
- **C.** Hotfix branch
- **D.** Develop branch

> [!answer]- Answer
> **C.** Hotfix branch
>
> **Hint:** Think about which branch type is designed to patch a live production release immediately.

## Question 10

What is the function of the `git stash` command in a developer's daily workflow?

- **A.** It permanently deletes all uncommitted changes to clean up the workspace
- **B.** It takes dirty uncommitted changes and saves them for later use, reverting the directory to a clean state
- **C.** It moves commits from a local repository to a remote 'stash' on the server
- **D.** It organizes the staging area by grouping similar file changes together automatically

> [!answer]- Answer
> **B.** It takes dirty uncommitted changes and saves them for later use, reverting the directory to a clean state
>
> **Hint:** Imagine you need to fix an urgent bug on another branch but aren't ready to commit your current progress.

## Question 11

Git ensures the integrity of managed source code and prevents accidental or malicious alteration by using which cryptographic algorithm?

- **A.** MD5
- **B.** SHA1
- **C.** AES-256
- **D.** RSA

> [!answer]- Answer
> **B.** SHA1
>
> **Hint:** Recall the name of the 40-character hexadecimal strings used to identify commits.

## Question 12

Which workflow model is characterized by having only one long-lived branch where all changes are small, incremental, and deployed frequently via CI/CD?

- **A.** Git Flow
- **B.** GitHub Flow
- **C.** Forking Workflow
- **D.** Centralized Workflow

> [!answer]- Answer
> **B.** GitHub Flow
>
> **Hint:** Think of the 'middle ground' workflow that preserves pull requests but eliminates 'develop' and 'release' branches.

## Question 13

What occurs when you execute `git init` within an existing project directory that is not yet under version control?

- **A.** All files in the directory are automatically committed to a new 'main' branch
- **B.** A new `.git` subdirectory is created, transforming the directory into a Git repository
- **C.** Git creates a copy of the project in a new folder named after the user's name
- **D.** The directory is instantly synchronized with a new repository on Bitbucket or GitHub

> [!answer]- Answer
> **B.** A new `.git` subdirectory is created, transforming the directory into a Git repository
>
> **Hint:** Focus on the hidden folder Git uses to manage your project's history.

## Question 14

In 2026, Git is estimated to have a market share of approximately what percentage among version control systems?

- **A.** $50\%$
- **B.** $85\%$
- **C.** $99\%$
- **D.** $70\%$

> [!answer]- Answer
> **B.** $85\%$
>
> **Hint:** Consider the term 'de facto standard' and how ubiquitous Git has become for developers.

## Question 15

What is the main difference between 'merging' and 'rebasing' when integrating changes from one branch into another?

- **A.** Merging deletes the target branch, while rebasing preserves it for future use
- **B.** Merging creates a new commit to join histories, while rebasing moves the entire branch to begin on the tip of another
- **C.** Merging is only for local changes, while rebasing is required for remote collaboration
- **D.** Merging is a feature of Git, while rebasing was inherited from older systems like SVN

> [!answer]- Answer
> **B.** Merging creates a new commit to join histories, while rebasing moves the entire branch to begin on the tip of another
>
> **Hint:** Think about which operation 'rewrites history' to make it look like a straight line.
