---
title: When something doesn't run
description: Find the next step for common Python, Git, and Colab problems.
---

Read the last line of the error first. It names the kind of problem. Then look for your filename and the line number above it. Show a helper the command you ran and the full error message.

## Python or Git isn't found

Close and reopen the terminal after installation. On Windows, try `py --version`; on macOS, use `python3 --version`. If Git isn't found, check its installation too. Use [Colab](../setup/#use-colab-if-setup-gets-in-the-way) if troubleshooting is taking you away from the lesson.

If Windows has `python` but no `py`, check `python --version`. If it reports Python 3.10 or newer, use `python quiz.py` for this workshop. Avoid running an unverified Python 2 installation.

## Python can't find quiz.py

Your terminal is probably in another folder. `pwd` on macOS or PowerShell shows your current folder. `ls` on macOS or `dir` on Windows lists its files. In Windows Command Prompt, `cd` without an argument shows the current folder.

From the repository root, run `cd workshop`, then your Python command. Check that the editor saved `quiz.py`, not `quiz.py.txt`. A path containing spaces must be quoted, such as `cd "My Projects"`.

## SyntaxError or IndentationError

Check for a missing colon after `if`, `while`, `for`, or `def`, a missing quote or bracket, and inconsistent indentation. Use four spaces per level. Read the previous line too: an unclosed quote can cause the next line to be flagged.

Copy code using the copy button, not a screenshot. It copies executable text without line numbers or terminal prompts.

## NameError, KeyError, or ModuleNotFoundError

`NameError` often means a name is misspelled or used before assignment. `scores` and `Scores` are different names.

`KeyError` means the key isn't in that dictionary. Use the cluster names exactly as written in `CLUSTERS`. The validation loop must run before you look up `choices[answer]`.

For `ModuleNotFoundError: No module named 'questions'`, put `questions.py` beside `quiz.py`. You don't install this file with pip; copy the question bank from the loops lesson.

## The program keeps asking

A `while` loop repeats until its condition becomes false. Make sure the second `input()` is inside the loop and assigns to `answer`. Press Ctrl+C to stop a local program if needed, then fix and rerun it.

In Colab, use the cell's stop button. Wait for it to stop before running a different milestone.

## Git refuses a commit or branch switch

If Git asks who you are, follow the name and email setup on the [setup page](../setup/#if-git-needs-your-name).

If it warns that local changes would be overwritten, follow [safe recovery](../checkpoints/). Preserve your files before trying again. If a checkpoint isn't found, run `git fetch origin` and check its exact spelling. A facilitator must publish the checkpoint branches before workshop day.

If the branch name already exists, choose a new local recovery name. Don't delete the earlier branch; it may hold work you want back.

## Colab lost its runtime

Your saved notebook can remain in Drive even when its running Python session disconnects. Reconnect, then rerun the milestone code cell you're working on. Each cell includes its required data. Unsaved edits still need saving; a connected runtime is not a backup.

## The result looks surprising

Every cluster tied at a displayed score level appears, so you may see more than three clusters. A percentage is a share of awarded points. Different answer choices can award different total numbers of points. Check the [results explanation](../build/results/) before changing the ranking code.
