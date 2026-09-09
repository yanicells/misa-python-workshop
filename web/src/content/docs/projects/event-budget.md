---
title: "Project: event budget checker"
description: Build a budget tool that records expenses and explains where the money went.
---

## The project

Build a terminal program for planning an event budget. The user enters a total budget and several expenses. The program calculates the amount spent, the amount left, and whether the plan is within budget.

Use fictional amounts while testing. A beginner project should not become the only copy of a real organization's financial records.

## What the finished program should do

The core version should:

- accept a budget greater than or equal to zero;
- keep several expenses with a label and amount;
- calculate the total spent and remaining amount;
- show a clear warning when expenses exceed the budget;
- handle invalid amounts without ending the program.

The first version does not need file saving or a complicated category system. Accurate calculations and understandable output matter more.

## Milestone 0: run a blank project

Create an empty `budget.py` in a new folder. Print a short program title and run it from the terminal. Add a README with one sentence describing the event your version is meant to plan.

Choose one currency for the whole program. Store amounts as plain numbers without a currency symbol, then add the symbol only when displaying output.

## Milestone 1: calculate one fixed expense

Write a budget and one expense directly in the file. Calculate the remaining amount and print a small summary.

Keep the input values, calculation, and display as separate steps. This makes it easier to change the source of the values later.

Test one expense below the budget, one equal to it, and one above it. Decide which message belongs to each case.

## Milestone 2: describe expenses

Store a label with each amount so the summary can say what the money is for. Then move from one expense to a list of expense records.

Loop through the list to calculate the total. Print each expense and the final totals. Do not rely on a hand-written total that can drift when an item changes.

Checkpoint question: if you add or remove one expense record, does every total update automatically?

## Milestone 3: ask for the budget

Replace the fixed budget with user input. Convert it to a number and keep asking until it is valid. Decide whether your program accepts decimals and whether zero is a valid planning budget.

Give the user enough information to correct an invalid value. "Enter a number greater than or equal to zero" is more useful than "Invalid."

Keep the fixed expense list for this milestone. Change only one source of data at a time.

## Milestone 4: add expenses one by one

Let the user enter an expense label and amount. Add the new record to the list, then show the updated remaining budget.

Begin with a fixed number of entries or ask whether the user wants to add another. Later, a menu can make this more flexible. Reject empty labels and negative amounts unless your version intentionally uses negative numbers for refunds.

Decide how the user finishes entering expenses. Whatever command you choose should not be accepted as an expense label by accident.

## Milestone 5: organize the work into functions

Separate the program into jobs that you can name clearly. Likely jobs include reading a valid amount, adding an expense, calculating totals, and displaying the summary.

Calculation functions should return numbers or other data so you can test them without typing input every time. User-facing functions can handle prompts and printed messages.

Checkpoint question: can you test the total calculation with a prepared list of expenses without running the full interactive program?

## Milestone 6: edit the plan

Add one way to correct a mistake. The user might remove an expense, change its amount, or clear the list and begin again. Start with one edit action before building a larger menu.

Numbered expenses make selection easier, but remember to validate the number and convert from the user's numbering to a Python index.

After editing, recalculate from the records. Do not try to repair the old total by hand.

## Decisions that belong to you

- Whether amounts display as whole numbers or with two decimal places.
- Whether expenses have categories such as venue, food, and materials.
- Whether overspending is allowed with a warning or blocked before an item is added.
- Whether the summary follows entry order, amount, or category.
- Whether a contingency amount is an expense, a reserved part of the budget, or an optional recommendation.

Pick rules that match the event you imagined. Explain them briefly in the README.

## Test the finished version

Try no expenses, one expense equal to the budget, several expenses below it, and a plan that goes over. Check decimal values such as `99.50`. Try an empty label, a negative amount, letters where a number is expected, and an edit number outside the list.

Calculate one test case by hand and compare it with the program. Formatting may round the display, but the stored numbers should still produce the correct total.

## If you want to take it further

You could add category totals, a recommended contingency, JSON saving, or a comparison between planned and actual costs. Another direction is to export a plain text report someone can attach to an event proposal.

The project is finished enough when another person can enter a plan, correct one mistake, and understand the summary without you explaining each line of output.
