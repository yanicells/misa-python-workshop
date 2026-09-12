---
title: "Project: question-bank editor"
description: Build a tool for drafting quiz questions and checking the data behind them.
---

## The project

Build a terminal tool that creates and reviews personality-quiz questions. It will not run the quiz itself at first. Its job is to help an author write prompts, add answer choices, attach result labels, and catch incomplete data before that data reaches the quiz.

Use your own result categories for this project. If you work with MISA cluster information, keep the supplied names and descriptions accurate rather than inventing official claims.

## What the finished program should do

The core editor should:

- keep more than one question;
- store a prompt and several answer choices for each question;
- attach two allowed result labels and small positive weights to every choice;
- display one question in a readable preview;
- reject empty prompts, empty choices, unknown labels, and choices with no award;
- report how many scoring opportunities each label receives.

The editor does not need a visual interface. A reliable text preview is enough to prove the data has the right shape.

## Milestone 0: choose the data before the interface

Create an empty `editor.py` and make it run. In a README or comment, sketch one question in plain language: its prompt, answer text, and associated result labels.

Then decide how that question will be represented with lists and dictionaries. Use named dictionary keys for pieces you will need to retrieve later. Keep all allowed labels in one separate collection so validation has a single source of truth.

Checkpoint question: can you point to the exact place where the prompt, one answer's text, and its labels are stored?

## Milestone 1: preview one fixed question

Write one question directly in the file. Print its prompt and choices in the same order a player would see them. Include the attached labels in an author-only preview so you can inspect the scoring data.

Keep previewing separate from asking for an answer. This project is about editing data, so do not let quiz behavior distract from the first goal.

Test choices whose primary and related labels receive different weights. The display should make the difference easy to notice.

## Milestone 2: validate the fixed data

Write checks for the question you already have. A valid question needs a non-empty prompt, enough choices to be meaningful, non-empty answer text, and two different known labels per choice. Keep the weights positive integers with a fixed total, such as 2 points and 1 point.

Decide how validation reports problems. A boolean says whether the data passed, while a list of messages can tell the author what to fix. The second takes more work but becomes more useful as the editor grows.

Create broken copies on purpose. Remove a prompt, misspell a label, and give one choice an empty point dictionary. Confirm that each problem is reported.

## Milestone 3: create a prompt through input

Ask the author for a question prompt and reject blank input. Store the new question in a collection, even if it has no choices yet. Then preview what currently exists.

It is acceptable for a question to be incomplete while the author is editing it. Your validation should distinguish "still being drafted" from "ready for the quiz."

Checkpoint question: if the author cancels halfway through, is the partial question kept, discarded, or marked as a draft? Choose one behavior and make the message clear.

## Milestone 4: add choices and labels

Let the author add answer text to the selected question. Then ask for a primary label and a related label from the allowed collection. Validate each label before storing the choice, and reject a repeated label.

You decide how choices receive identifiers. Letters match the workshop quiz, while numbers are easier to generate as the list grows. The data shape should not depend on manually writing a long chain of conditions.

Do not ask for every field in one large block before checking anything. Validate the text, then the labels, then show the newly created choice.

## Milestone 5: manage several questions

Add a menu for creating a question, listing question titles or short previews, opening one question, adding a choice, validating, and quitting.

Break these actions into functions. Pass the question bank and allowed labels instead of hiding them in several unrelated global variables. A function that searches for a selected question should return the matching record or a clear no-result value.

Use numbers or stable IDs when two prompts begin with the same words.

## Milestone 6: count scoring opportunities

Produce a report that adds the possible points for each result label across all answer choices. A choice with 2 primary points and 1 related point contributes those weights to their matching labels.

This report catches structural imbalances such as one label receiving ten possible points while another receives two. It cannot show whether real answer patterns or question wording make the quiz fair. Explain that limit in the output or README.

Test the totals by hand on a tiny bank before using a larger one. Report the highest and lowest totals so a large structural imbalance is easy to spot.

## Milestone 7: save the bank

Save the question collection as JSON and reload it when the editor starts. Validate loaded data too. A file can have correct JSON syntax while still missing the fields your quiz expects.

Keep a backup before testing destructive actions such as deleting a question. Decide whether the editor saves after every change or through an explicit command.

The official tutorial introduces [saving structured data with JSON](https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json).

## Decisions that belong to you

- How many choices a ready question needs.
- Whether duplicate prompts or duplicate answer text are allowed.
- Whether labels are typed, selected from a numbered list, or both.
- Whether an incomplete question stays as a draft.
- What a short question preview should show.
- Whether the opportunity report sorts by label, highest count, or lowest count.

Write these rules where another quiz author can find them.

## Test the finished version

Create two questions with weighted primary and related labels. Save, quit, and reopen the editor. Preview both questions and compare the opportunity report with a manual count.

Then try blank text, an unknown label, repeated labels on one choice, a zero or negative weight, and a saved question missing a required field. The editor should explain the problem without silently changing the author's data.

## If you want to take it further

Possible additions include editing existing text, duplicating a question as a starting point, searching prompts, filtering drafts, or exporting a Python data file for a quiz. Treat export as a separate format with its own validation. Never use `eval(input())` to read author data because it runs the entered text as Python code.

The project is ready to share when another author can create, inspect, validate, save, and reopen a small question bank without reading your source code first.
