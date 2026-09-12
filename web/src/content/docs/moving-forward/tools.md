---
title: Use Python's tools
description: Work with built-in functions, modules, editors, scripts, and notebooks.
---

You do not have to write every operation yourself. Python includes small functions for common jobs and modules that group related tools.

## Start with built-in functions

**Built-in functions** are available without an import. You have already used `print()`, `input()`, `len()`, `type()`, and `sorted()`.

```python title="Try in scratch.py"
scores = [7, -2, 4]

print(abs(scores[1]))
print(min(scores))
print(max(scores))
print(sum(scores))
print(round(10 / 3, 2))
```

`abs()` returns a number's distance from zero. `min()` and `max()` find the lowest and highest items. `sum()` adds the numbers in a collection. `round(number, digits)` rounds to the requested number of decimal places.

Use a built-in when its name matches the job. Write the operation yourself when seeing the steps is part of what you are learning, as we did with the quiz score total.

## Import a module

A **module** is a Python file that groups related names. The standard library comes with Python, so you can import its modules without installing another package.

```python
import math
import random

print(math.sqrt(81))
print(math.floor(4.9))
print(math.pi)

topics = ["lists", "loops", "functions"]
print(random.choice(topics))
```

The module name before the dot shows where a function or value came from. This becomes useful when a program uses several libraries with similar names.

Read the documentation for the [math module](https://docs.python.org/3/library/math.html) and [random module](https://docs.python.org/3/library/random.html) as a catalog. Pick one function that fits your project and try it with a small input before adding it to the main file.

## Know what runs your code

An **integrated development environment**, or IDE, combines a code editor with tools for running and debugging programs. VS Code can do this after Python support is installed. It can also edit plain text without running it.

A `.py` file is a saved script. Each time you run it, Python starts the program again from the top. Variables from the previous run do not remain.

Jupyter and Colab use **notebooks**, which split code into cells. A notebook keeps variables while its runtime is active. Running cells out of order can leave old values in memory, so restart the runtime and run from the first cell when the result becomes confusing.

Neither an editor nor a notebook changes Python's basic rules. They give you different ways to write, run, and inspect the same language.

## Practice: a random review picker

Create a list of topics you want to review. Use `random.choice()` to select one. Then use `input()` to ask whether the topic was easy, okay, or hard. Keep a count for each answer.

Once that works, choose whether repeated topics are allowed. Solving that version may lead you to `random.sample()`, list removal, or a copy of the original list. Read each function's documentation before deciding which one fits.
