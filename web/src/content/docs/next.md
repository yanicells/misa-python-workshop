---
title: Keep building
description: Small exercises for Python topics beyond the live workshop, plus ways to share your quiz.
---

Pick something you want the program to do, then learn the next concept it needs. The [Python tutorial](https://docs.python.org/3/tutorial/) is a useful reference after this workshop; it assumes some programming background, so take it a section at a time.

## Collections and text

| Topic | Why use it? | A small exercise |
| --- | --- | --- |
| Tuples and unpacking | Keep an ordered record whose slots won't be reassigned | Store `(cluster, points)` and unpack it into two names |
| Slicing and negative indexes | Select part of a sequence | Print the last two items of a list using `items[-2:]` |
| List mutation and methods | Add, insert, remove, or reorder items | Make a task list with `append`, `insert`, `remove`, `extend`, `sort`, and `reverse`; use `index` to find a task and `clear` to empty a copy |
| Copying and aliasing | Understand when two names refer to one object | Compare `copy = original` with `copy = original[:]`, then change the first item |
| Sequence operators | Combine or inspect ordered values | Compare `len(names)`, `"Alex" in names`, `names + ["Sam"]`, and `names * 2` |
| Strings and escapes | Work with characters and line breaks | Print one letter with an index, a substring with a slice, and two lines using `\n` |
| String methods | Clean text before comparing it | Compare a name before and after `strip`, `lower`, and `replace` |
| Dictionaries | Look up values by meaningful keys | Add a cluster to a small practice dictionary and loop through its keys and values |
| Formatting | Control how numbers and text appear | Print a percentage with two decimal places, then try `.format()` and field alignment |

Read [data structures](https://docs.python.org/3/tutorial/datastructures.html), [strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), and [formatted output](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting).

A slice makes a shallow copy: nested mutable values still refer to the same objects. A tuple's slots cannot be reassigned, but an object inside a tuple can itself be mutable. Strings are immutable; methods such as `lower()` return a new string.

## Loops and transformations

Use `break` when a search should stop at the first match. Use `continue` when one item should be skipped. Try finding the first positive score, then printing every score except zero.

For a stepping range, try `range(0, 10, 2)`. For nested iteration, loop through a list of teams and print each member under their team. Keep the outer and inner variable names distinct.

Mapping transforms each item; filtering keeps only some items. First build a list of doubled positive scores with an ordinary loop and `append()`. Then compare it with:

```python
scores = [0, 2, 5]
doubled = [score * 2 for score in scores if score > 0]
print(doubled)
```

This prints `[4, 10]`. A comprehension is useful when the goal is a new collection. Keep printing and more complicated steps in ordinary loops. Python also has `map()` and `filter()`; try them with named functions after you understand the loop version.

Read [control flow](https://docs.python.org/3/tutorial/controlflow.html) and [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).

## Functions and scope

Give a function a parameter instead of relying on an unrelated global variable. Try writing `percentage(points, total)` that returns a number, then call it twice with different arguments. Decide how it should handle a zero total.

A return ends that function call; a statement after an unconditional return won't run. A function that reaches its end without a return value returns `None`. Compare `print(percentage(2, 4))` with a function that only prints inside its body.

Explore default arguments, keyword arguments, nested calls, and local versus enclosing scope in [defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) and [Python scopes](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces). Try a default greeting and override it in one call. Keep shared mutable defaults out of your first experiments.

## Objects, encapsulation, and inheritance

A class describes a kind of object. Instances have their own identity and can hold state in attributes. Methods act on an instance; `self` refers to it. `__init__` initializes an instance's attributes.

Try a `Task` class with `title` and `done` attributes and a `complete()` method. Create two tasks, complete one, and confirm the other stays unfinished. Compare instance attributes with a class attribute shared through the class.

Encapsulation groups state with the methods that manage it. A single leading underscore signals an internal detail by convention. Double leading underscores trigger name mangling; they are not a security boundary.

Then try a `TimedTask(Task)` subclass with a duration. Call `super().__init__(title)` to reuse initialization, and override a `describe()` method to include the duration. Inheritance resolves behavior through base classes; it doesn't paste copies of every method into your source file.

Read [classes](https://docs.python.org/3/tutorial/classes.html), especially inheritance and private variables. Use a subclass when the new object really is a specialized kind of the original. The quiz is small enough to stay as functions and dictionaries.

## Numbers and modules

Try `abs`, `round`, `min`, and `max` with a few practice scores. `sum([2, 3, 4])` adds a collection of numbers. In the workshop we used an explicit loop so you could see the accumulation.

A module groups code you can import. Explore [math](https://docs.python.org/3/library/math.html) with `floor`, `sqrt`, and `pi`, or [random](https://docs.python.org/3/library/random.html) with `choice` and `sample`. Write a random practice-question picker. Keep all values in your code while learning; don't use `eval(input())` to parse answers, because that runs the supplied text as Python code.

VS Code is an editor with debugging tools. [Jupyter](https://jupyter.org/try) offers notebooks that mix code and prose, much like Colab. Compare rerunning a saved `.py` file with rerunning one notebook cell: notebook variables can survive between cell runs.

## A few projects to try

### A study planner

Ask for a subject and tasks, then show unfinished work. Start with a list of dictionaries. Add a menu with a validation loop. When that works, learn [JSON files](https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json) so tasks survive after the program closes. Done means you can add, finish, save, and reload a task.

### An event budget checker

Store a budget and a list of labeled costs. Print the total, remaining amount, and a message when the costs exceed the budget. Use functions and numeric conversion. Test zero costs and an overspend. Use fictional amounts for practice.

### A question-bank editor

Add a menu that lets you create a question, show it, and preview each answer's cluster associations. Validate cluster names and reject empty awards. Add an opportunity count so the editor can compare the balance before and after a change. Keep the original bank as a separate backup.

## Publish your own quiz

GitHub doesn't automatically receive your commits. First create your own empty GitHub repository through the website. Leave its README and other initialization options unchecked so the remote starts empty. From the local workshop repository, inspect your remotes:

```bash
git remote -v
```

Add your own repository as a new remote named `mine`. Copy its exact HTTPS URL from GitHub, and use that URL in place of the example below:

```bash
git remote add mine https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u mine my-quiz
```

This publishes `my-quiz` to your repository. Keep `origin` pointing to the workshop so recovery references stay available. If you continued on a recovery branch, use that branch's name in the push command. GitHub will guide you through authentication; an account password is not an HTTPS Git credential.

Before sharing, check your files for private information. Add a short README explaining how to run `workshop/quiz.py`. To bring later changes down from your own remote, commit your local edits first, then use `git pull --ff-only mine my-quiz` while on the matching branch. If Git refuses because histories differ, ask a helper to explain the difference before merging.

Read [GitHub's push guide](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository) and the free [Pro Git book and videos](https://git-scm.com/book/en/v2). For video lessons, [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) has a longer course with practice problems.

Share your quiz with a friend, your organization, Yani, or Gabe. If you want to build with other students, ask the MISA team about joining and the work each cluster is doing. Your quiz result is a place to start that conversation.
