---
title: Put your work online
description: Publish your branch to your own GitHub repository without losing the workshop remote.
---

Saving a file, committing it, and publishing it are separate actions. Git records commits on your computer. GitHub receives them only after you push to a remote repository.

## Make a repository for your version

Create a new empty repository on GitHub. Leave its README, license, and `.gitignore` options unchecked so GitHub does not create a separate first commit.

Before publishing, read through your files for names, IDs, tokens, passwords, or other information you did not mean to share. Add a short README that explains what your program does and how to run it.

## Keep the workshop remote

From the workshop repository, check the remotes you already have:

```bash
git remote -v
```

`origin` should still point to the workshop repository. Keep it there so checkpoint and recovery instructions continue to work.

Copy the HTTPS URL of your empty repository. Add it under a different name, such as `mine`:

```bash
git remote add mine https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git remote -v
```

Replace the example URL with the exact one GitHub gives you.

## Push your branch

Check your current branch and working files first:

```bash
git status
git branch --show-current
```

Commit any changes you want to publish. If your branch is named `my-quiz`, push it with:

```bash
git push -u mine my-quiz
```

The `-u` option connects your local branch to the remote branch. Later, while you are on the same branch, `git push` is enough.

GitHub may ask you to sign in through a browser or use a credential manager. Your account password is not used as an HTTPS Git credential.

## Bring down later changes carefully

Commit your local work before pulling. Then run:

```bash
git pull --ff-only mine my-quiz
```

`--ff-only` refuses to combine diverging histories automatically. If it stops, read the message and ask someone to help compare the local and remote commits. Do not erase either version just to make the command pass.

GitHub's [push guide](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository) explains the same workflow in more detail. The free [Pro Git book](https://git-scm.com/book/en/v2) is useful when you want to understand branches and remotes beyond the workshop.

## Share what you made

Send the repository link to a friend and ask them to run the program from your README. Their questions will show which instructions are missing. If you keep building with MISA, show the team what you tried and which part you want to learn next.
