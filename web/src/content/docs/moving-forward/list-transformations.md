---
title: Transform a list
description: Compare ordinary loops, mapping, filtering, and list comprehensions.
---

Many programs take a collection and produce a new one. There are two common operations:

- **Mapping** applies the same operation to every item.
- **Filtering** keeps only the items that pass a condition.

Start with an ordinary loop. It makes every step visible.

## Build the result one item at a time

```python title="Try in scratch.py"
scores = [0, 2, 5, 1]
doubled_scores = []

for score in scores:
    if score > 0:
        doubled_score = score * 2
        doubled_scores.append(doubled_score)

print(doubled_scores)
```

The condition filters out zero. Multiplication maps each remaining score to a new value. `append()` collects those values in a new list. The original list stays unchanged.

## Write the same transformation as a comprehension

A **list comprehension** puts the new value, loop, and optional condition inside brackets.

```python
scores = [0, 2, 5, 1]
doubled_scores = [score * 2 for score in scores if score > 0]
print(doubled_scores)
```

Read it in this order:

1. Take each `score` from `scores`.
2. Keep it if `score > 0`.
3. Put `score * 2` in the new list.

The result is `[4, 10, 2]` in both versions.

## Know when to keep the loop

A comprehension works well when you are building one new collection from another. Use an ordinary loop when you need several statements, multiple side effects, `break`, detailed error handling, or comments inside the process.

Avoid using a comprehension only to call `print()`. Its purpose is to create a collection. A normal loop says that job more clearly.

## Recognize map and filter

Python also has `map()` and `filter()`. They work best when the operation or condition already has a clear named function.

```python
def double(number):
    return number * 2

scores = [2, 5, 1]
doubled_scores = list(map(double, scores))
print(doubled_scores)
```

`map()` returns an iterable, so `list()` collects its results into a list. For a short beginner program, a loop or a clear comprehension is often easier to follow. Learn `map()` and `filter()` so you can read code that uses them, not because every loop needs replacing.

## Practice: prepare a grade report

Start with a list of numeric grades. Make a new list containing only passing grades, then make another list that adds five bonus points to each passing grade without going over 100.

Write the ordinary loop first. Test it. Then write a comprehension that produces the same result. Keep the version you find easier to explain.

The [list comprehension section](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) in the official tutorial has more examples.
