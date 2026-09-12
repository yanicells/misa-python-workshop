---
title: Put your work online
description: Make your own copy on GitHub, upload your quiz branch, and share its page.
---

GitHub gives your project a page that other people can open in a browser. They can read the README, browse the files, and inspect earlier commits. Your local files appear there only after you push them.

Before publishing, read through the project for names, student IDs, tokens, passwords, or anything else you did not mean to share.

## Make your copy on the GitHub website

1. Sign in to [GitHub](https://github.com/).
2. Open the [MISA Python workshop repository](https://github.com/yanicells/misa-python-workshop).
3. Select **Fork** near the upper-right corner of the repository page.
4. Choose your account as the owner. You can keep the suggested repository name or choose a new one.
5. Create the fork and wait for GitHub to open its page.

A **fork** is a repository under your account that begins with another repository's history. Look at the owner name near the top of the page to confirm that you are viewing your copy.

The main parts of a GitHub repository page are:

- **Code**, where you browse files and copy the repository URL;
- **Commits**, where you inspect saved versions; and
- the **README**, which explains what the project does and how to run it.

Add a short README to your version after the quiz is online. Tell people what it asks, how to run `quiz.py`, and which Python version they need.

## Connect your local project to your fork

The workshop repository is already named `origin` on your laptop. Keep that connection so the checkpoint recovery instructions still work.

Check it from the terminal:

```bash
git remote -v
```

On your fork's GitHub page, select the green **Code** button and copy the HTTPS URL. It looks like `https://github.com/YOUR_USERNAME/misa-python-workshop.git`.

Add that URL under the name `mine`:

```bash
git remote add mine https://github.com/YOUR_USERNAME/misa-python-workshop.git
git remote -v
```

Replace the example URL with the exact one copied from your page. `origin` should still point to the workshop, while `mine` should point to your fork.

## Upload your quiz branch

Check that you are on your own branch and that the work you want is committed:

```bash
git branch --show-current
git status
```

If your branch is named `my-quiz`, push it with:

```bash
git push -u mine my-quiz
```

GitHub may open a browser sign-in or use your computer's credential manager. Your account password is not used directly as an HTTPS Git credential.

Return to your fork's page and refresh it. GitHub may show a banner for the recently pushed `my-quiz` branch. You can also open the branch menu above the file list and select `my-quiz`.

The `-u` option remembers the connection between the local and GitHub branches. Later, while you are on `my-quiz`, this shorter command uploads new commits:

```bash
git push
```

## Share and keep building

Copy the browser URL while the `my-quiz` branch is selected. Send it to a friend and ask them to follow your README. Their questions can show which instruction needs more detail.

Commit local changes before bringing down work from GitHub. The [GitHub push guide](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository) covers the browser and command-line workflow in more detail. The free [Pro Git book](https://git-scm.com/book/en/v2) is useful when you want to understand branches and remotes beyond this workshop.
