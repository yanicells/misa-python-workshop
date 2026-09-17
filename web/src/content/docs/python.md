---
title: What is Python?
description: See what Python can make, why beginners learn it, and how a program runs.
---

Python is a programming language. You write instructions in a text file, then the Python interpreter reads and runs them. A file ending in `.py` is a Python file.

The language is used for web applications, automation, data analysis, scientific computing, and machine learning. Python.org lists tools for all of these areas, from Django and Flask for websites to pandas and SciPy for working with data. [Browse Python's application guide](https://www.python.org/about/apps/) when you want to see the wider ecosystem.

## Python shows up in familiar products

Instagram has described using Python and Django for its frontend server. Spotify has written about using Python for backend services and data analysis. Those products use many languages and systems, but Python is one part of how their teams build them.

- [How Instagram uses Python](https://engineering.fb.com/2023/08/15/developer-tools/immortal-objects-for-python-instagram-meta/)
- [How Spotify has used Python](https://engineering.atspotify.com/2013/3/how-we-use-python-at-spotify/)

In the 2024 Python Developers Survey, respondents reported using Python for web development, data analysis, machine learning, automation, research, and education. The same survey found that 48% used VS Code as their main editor. It surveyed more than 30,000 Python developers and learners from almost 200 countries and regions. [See the survey results](https://lp.jetbrains.com/python-developers-survey-2024/).

## What we will make

Our Python program is a MISA cluster quiz. It will:

1. welcome the player by name;
2. ask 15 questions and read each answer;
3. add weighted points to matching clusters; and
4. show the player's top score levels.

Python handles the input, processing, and output. The terminal is where we type answers and see results. VS Code is where we edit the instructions.

## Your first mental model

Python runs a file from top to bottom. It skips a block only when a condition says to skip it, and it repeats a block only when a loop says to repeat it. Later, functions will give groups of instructions a name.

You do not need to memorize syntax before starting. Keep a `scratch.py` file for small experiments, predict what each example will do, then run it. After an idea makes sense on its own, we will use it in `quiz.py`.

[Next: Git and GitHub →](../git-github/)
