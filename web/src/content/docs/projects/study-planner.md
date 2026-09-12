---
title: "Project: study planner"
description: Build a task planner that grows from one printed task into a saved, usable list.
---

## The project

Build a terminal program that keeps track of schoolwork. A user should be able to add a task, see unfinished work, and mark something complete. A later version can save the tasks so they are still there the next time the program runs.

The planner does not need accounts, notifications, or a calendar interface. One student using one program is enough for the first complete version.

## What the finished program should do

At minimum, the planner should:

- keep more than one task;
- record a title and whether each task is finished;
- show tasks in a readable list;
- let the user add a task and complete one;
- reject an empty title or an invalid menu choice without crashing.

You may also store a subject, due-date label, estimated time, or priority. Pick fields that you would actually use. Every extra field adds another input to validate and another detail to display.

## Milestone 0: begin with a blank file

Create a new folder and an empty `planner.py`. Make it print the name of your planner and run it from the terminal.

This first run checks the folder, filename, and command before the program has enough code to hide a setup problem. Save the file and run it again after changing the title.

## Milestone 1: show one fixed task

Write one example task directly in the file. Store enough information to print its title and status. The program only needs to display that task.

Decide what an unfinished and finished task should look like. You might use words, brackets, or your own labels. Keep the data separate from the display text so you can change the appearance later.

Checkpoint question: can you change the example task in one place and see the new version everywhere it is displayed?

## Milestone 2: keep several tasks

Replace the single task with a collection. A list of dictionaries is a good starting shape because the order matters and each task has named fields. Loop through the collection to display every task with a number.

Test an empty list as well. Choose a useful message instead of showing nothing.

Checkpoint question: does each displayed number clearly match the task a user would select?

## Milestone 3: add a task

Ask the user for a title and place the new task in the collection. Trim outside spaces and reject an empty title. Show the list afterward so the result of the action is visible.

Begin with one add operation per run. Do not build the full menu yet. This keeps the input, validation, and list change easy to inspect.

You decide whether duplicate titles are allowed. If they are, selecting by number will be safer than selecting by title.

## Milestone 4: complete a task

Ask which task should be marked done. Convert and validate the selection before using it as a list index. Remember that the user sees numbering from 1 while Python list indexes begin at 0.

Decide what happens when the task is already complete. The program can explain that nothing changed, or it can let the user toggle the status back to unfinished.

Checkpoint question: can an invalid number, text instead of a number, or an empty list break the program?

## Milestone 5: keep the program open

Add a menu loop with actions for showing, adding, completing, and quitting. Each pass through the loop should perform one action and return to the menu.

Move each action into a small function after it works. Pass the task list where it is needed. Keep input and printing close to the user-facing action, while calculations or searches can return values for the caller to use.

Your menu wording and commands are up to you. Letters are easier to validate; numbers may feel more natural for a numbered menu.

## Milestone 6: save and reload

So far, the collection disappears when Python stops. Store it in a JSON file and load that file when the program starts. JSON fits lists, dictionaries, strings, numbers, booleans, and `None`.

Treat saving as a separate milestone because files add new failure cases. Decide what the program should do on its first run when no save file exists. Write after every change or provide a save command, then test by closing and reopening the program.

The official tutorial shows how Python's [`json` module](https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json) writes and reads structured data.

## Decisions that belong to you

- Whether completed tasks stay visible, move to a separate view, or can be deleted.
- Whether subjects and priorities are free text or selected from allowed choices.
- Whether the default view keeps insertion order, groups by subject, or sorts by another field.
- Whether saving happens automatically or only when requested.

Make one choice at a time. Write down why it helps the person using your planner.

## Test the finished version

Start with no save file. Add two tasks with different titles. Complete the second one. Quit and reopen the program. Both tasks and the correct status should remain.

Also try an empty title, an invalid menu command, a task number that is too high, and text where a number is expected. A useful error message should return the user to the program without losing the current tasks.

## If you want to take it further

Possible directions include deadlines, subject filters, search, progress counts, or a `Task` class. Pick one that changes how you would use the planner. Avoid adding five half-working options just to make the menu longer.

The project is ready to share when a new user can add, complete, save, and reload a task by following your README.
