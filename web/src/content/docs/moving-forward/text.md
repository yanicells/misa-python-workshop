---
title: Work with text
description: Slice, clean, split, replace, and format Python strings.
---

A string is a sequence of characters. That is why `len()`, `in`, indexing, and slicing work on strings much like they work on lists.

## Read part of a string

```python title="Try in scratch.py"
course = "Python Workshop"
print(course[0])
print(course[-1])
print(course[:6])
print("Workshop" in course)
```

These lines read one character, the last character, the first six characters, and whether a smaller string appears inside the larger one.

Strings are **immutable**. You cannot replace `course[0]` directly. Build a new string instead, then assign it back to the variable if you want to keep the change.

## Clean input before comparing it

People add spaces and capitalization without thinking about it. Normalize input before you compare it.

```python
answer = input("Continue? ")
clean_answer = answer.strip().lower()

if clean_answer == "yes":
    print("Continuing")
```

`strip()` removes whitespace from both ends. `lower()` returns a lowercase string. Neither method changes the original string.

Other useful methods include:

| Method | Result |
| --- | --- |
| `split()` | A list of words separated by whitespace |
| `split(",")` | A list split wherever a comma appears |
| `replace(old, new)` | A new string with matching text replaced |
| `find(text)` | The first matching index, or `-1` if absent |
| `upper()` | An uppercase string |

## Put line breaks inside text

The backslash begins an **escape sequence** inside a string. `\n` starts a new line.

```python
message = "Tasks for today:\n1. Read\n2. Practice"
print(message)
```

If your text contains an apostrophe, you can use double quotes around the string instead of escaping it. Choose the version that is easiest to read.

## Format useful output

The quiz used an **f-string** to place a value inside text and show one decimal place.

```python
subject = "CSCI"
finished = 3
total = 5
percentage = finished / total

print(f"{subject}: {finished}/{total}")
print(f"Finished: {percentage:.1%}")
```

`:.1%` multiplies the number by 100, adds the percent sign, and keeps one decimal place. `:,` adds comma separators to large numbers. Formatting changes how a value is displayed, not the value stored in the variable.

The older `.format()` method is still common in existing programs:

```python
message = "{} has {} tasks left".format(subject, total - finished)
print(message)
```

You should be able to read both styles. For new beginner projects, f-strings are usually shorter and easier to adjust.

## Practice: clean a list of names

Ask the user for names separated by commas. Split the text into a list. Loop through the names and print each one after removing outside spaces and changing it to title case with `title()`.

Decide what your program should do with an empty name between two commas. That decision is part of designing the program.

The official tutorial has more detail on [text](https://docs.python.org/3/tutorial/introduction.html#text) and [formatted output](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting).
