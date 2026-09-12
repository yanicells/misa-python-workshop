---
title: Git and GitHub
description: Understand versions, repositories, branches, and the GitHub website before using commands.
---

Git and GitHub work together, but they are different tools.

**Git** runs on your computer and records versions of a project. A Git project is called a **repository**, or repo. Each saved version is a **commit**. A **branch** gives you a named line of work, so you can change your quiz without changing the workshop's reference version.

**GitHub** is a website that stores and shares Git repositories. You can browse files, read a README, inspect earlier commits, open issues, and share your project through its GitHub page.

## The Google Docs and Drive analogy

A Git commit is similar to a named point in Google Docs version history. GitHub is similar to a shared Google Drive folder where other people can find the project.

The analogy has a limit: Git does not record every keystroke, and GitHub does not receive every saved file automatically. You choose when to stage files, create a commit, and push that commit online.

```text title="Three separate places"
Working files  →  Staging area  →  Local commit  →  GitHub repository
     save            git add        git commit        git push
```

## How we will use them

The workshop repository contains the guide and several working checkpoints. On GitHub, a branch link lets you inspect the files at a particular checkpoint. On your laptop, you will:

1. clone the repository once;
2. start from the `00-start` checkpoint;
3. create your own `my-quiz` branch;
4. edit and run your Python files; and
5. commit versions that you want to keep.

You will stay on your own branch during the lesson. The checkpoint branches are references for recovery, not steps you need to switch through one by one.

Publishing your version can wait until the quiz works. The [publishing guide](../moving-forward/publishing/) starts on the GitHub website and then shows the few terminal commands needed to upload your branch.

[Next: set up the project →](../setup/)
