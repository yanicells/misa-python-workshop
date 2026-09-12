---
title: Build your first class
description: Keep related state and behavior together with objects, classes, and methods.
---

Lists and dictionaries are enough for many small programs. A class becomes useful when your program has several things of the same kind and each one carries its own data and behavior.

## Think in objects

An **object** has four useful parts:

- A **type**, which says what kind of thing it is.
- An **identity**, which makes it a distinct instance.
- **State**, stored in attributes.
- **Behavior**, written as methods.

For a study planner, one task could have a title and completion status as its state. Completing or describing the task would be behavior.

## Define a class and make instances

A **class** describes what its instances know and can do.

```python title="Try in scratch.py"
class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True

    def describe(self):
        if self.done:
            return "[x] " + self.title
        return "[ ] " + self.title


reading = Task("Read chapter 3")
practice = Task("Answer practice quiz")

reading.complete()
print(reading.describe())
print(practice.describe())
```

`Task("Read chapter 3")` creates, or **instantiates**, an object. `__init__` initializes its attributes. `self` refers to the instance receiving the method call. Each task has its own `title` and `done` values, even though every task uses the same method definitions.

## Connect methods to familiar syntax

You have already called methods on objects:

```python
name.strip()
tasks.append("Review")
reading.complete()
```

The value before the dot receives the method call. Inside a method you define, `self` refers to that value.

## Keep changes behind useful methods

**Encapsulation** means keeping related state and behavior together and controlling how other code changes that state. The `complete()` method gives the task one clear way to mark itself done.

Python relies heavily on convention. A leading underscore, such as `self._done`, tells other programmers that an attribute is an internal detail. Two leading underscores trigger name mangling, but they do not create a security boundary. Validation in your methods still matters.

Do not write a getter and setter for every attribute automatically. Add a method when it protects a rule or gives an operation a useful name.

## Decide whether a class helps

Use a class when several objects share a clear kind, carry their own state, and have behavior that belongs with that state. Keep dictionaries and functions when they already make the program easy to understand. The workshop quiz does not need classes just because Python has them.

## Practice: model an event expense

Create an `Expense` class with a label, amount, and paid status. Give it a method that marks the expense paid and another that returns a readable description. Make two instances, change one, and confirm that the other keeps its own state.

Then decide on one rule worth protecting. You might reject negative amounts or prevent an expense from being paid twice. Put that rule in the method that performs the change.

The [Python classes tutorial](https://docs.python.org/3/tutorial/classes.html) goes deeper into class and instance variables, methods, and naming conventions.
