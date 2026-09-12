---
title: Take control of loops
description: Use range, nested loops, break, and continue when repetition needs rules.
---

The quiz used `while` to retry invalid input and `for` to visit every question. As your programs grow, you will sometimes need to repeat a fixed number of times, stop early, or skip one item.

## Pick the loop that matches the job

Use `for` when you have a collection to visit or a known number of repetitions. Use `while` when repetition depends on a condition that may change while the program runs.

```python title="Try in scratch.py"
for attempt_number in range(1, 4):
    print("Attempt", attempt_number)
```

`range(1, 4)` supplies `1`, `2`, and `3`. The stop value is excluded. A third argument sets the step, so `range(0, 10, 2)` supplies the even numbers from `0` through `8`.

## Stop when the answer is found

`break` exits the nearest loop immediately.

```python
names = ["Ari", "Bea", "Carlo", "Dani"]
search_name = "Carlo"

for name in names:
    if name == search_name:
        print("Found", name)
        break
```

This is useful when the remaining items cannot change the result. In a nested loop, `break` exits only the inner loop where it appears.

## Skip one item

`continue` ends the current iteration and moves to the next one.

```python
scores = [4, 0, 3, 0, 2]

for score in scores:
    if score == 0:
        continue
    print(score)
```

Use it when one case should be ignored. A plain `if` block is often clearer when the loop body is already short.

## Put a loop inside a loop

A **nested loop** repeats one loop inside another. It fits data that has levels, such as teams and their members.

```python
teams = {
    "Blue": ["Ari", "Bea"],
    "Gold": ["Carlo", "Dani"],
}

for team_name in teams:
    print(team_name)
    for member_name in teams[team_name]:
        print("-", member_name)
```

Use different variable names for the outer and inner loops. Read it one outer item at a time: choose a team, then visit all members of that team.

## Watch for infinite loops

A `while` loop needs a path that can make its condition false. If your program repeats forever in a terminal, press Ctrl+C. Then check which value the condition depends on and whether the loop changes that value.

## Practice: search a weekly schedule

Create a dictionary whose keys are days and whose values are lists of tasks. Ask for a task name, then search each day. Stop the inner loop when you find a match. Decide whether to stop the whole search after the first match or report every matching day.

Test a task that exists, one that appears twice, and one that does not exist. The [Python control flow guide](https://docs.python.org/3/tutorial/controlflow.html) covers more loop tools when you need them.
