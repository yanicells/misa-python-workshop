---
title: More with collections
description: Change, copy, search, and organize lists, tuples, and dictionaries.
---

The quiz used lists to keep items in order and dictionaries to find values by name. Those two structures can already handle many small programs. This lesson adds the operations you will need when the data changes while the program runs.

## Change a list

A list is **mutable**, which means its contents can change. You can replace one item by assigning through its index.

```python title="Try in scratch.py"
tasks = ["Read chapter", "Review notes"]
tasks[0] = "Read pages 10 to 20"
tasks.append("Answer practice quiz")
print(tasks)
```

`append()` adds one item to the end. Other common list methods include:

| Method | What it changes |
| --- | --- |
| `insert(index, item)` | Adds an item at a chosen position |
| `remove(item)` | Removes the first matching item |
| `extend(other_list)` | Adds every item from another collection |
| `sort()` | Rearranges items from lowest to highest |
| `reverse()` | Reverses the current order |
| `clear()` | Removes every item |

Methods such as `append()` change the list itself. They do not return the changed list. If `result = tasks.append("Rest")`, `result` becomes `None`.

## Take part of a sequence

A **slice** selects a range. The start is included and the stop is excluded.

```python
topics = ["values", "lists", "loops", "functions", "classes"]
print(topics[1:4])
print(topics[:2])
print(topics[-2:])
```

The outputs are `['lists', 'loops', 'functions']`, the first two topics, and the last two topics. Negative indexes count from the right, starting with `-1` for the final item.

## Copy before experimenting

Assignment does not copy a list. It gives the same list another name.

```python
original = ["COMMS", "HR"]
same_list = original
separate_list = original[:]

original.append("MKT")
print(same_list)
print(separate_list)
```

`same_list` sees the added item because both names refer to one list. `separate_list` does not. A full slice makes a **shallow copy**. If the list contains other mutable lists or dictionaries, those inner values are still shared.

## Use a tuple for a fixed record

A **tuple** is an ordered sequence written with parentheses. You cannot replace, add, or remove its positions after creation.

```python
result = ("Events", 4)
cluster, points = result
print(cluster)
print(points)
```

The second line **unpacks** the two positions into two variables. A tuple is useful when the number and meaning of the positions should stay fixed. It does not make objects stored inside it immutable.

## Add and remove dictionary entries

Assigning a new key creates an entry. `del` removes one.

```python
scores = {"COMMS": 2, "HR": 1}
scores["MKT"] = 3
print("HR" in scores)
del scores["HR"]
print(len(scores))
```

`in` checks dictionary keys, not their values. If a key might be missing, check first before using `scores[key]`.

## Practice: a small reading list

Make a list of at least four titles. Then:

1. Add a new title.
2. Replace one title.
3. Print the first two and last two titles using slices.
4. Copy the list, sort the copy, and prove that the original order stayed the same.
5. Store one title and its status in a tuple, then unpack it.

Use the [Python data structures guide](https://docs.python.org/3/tutorial/datastructures.html) when you need a list method that is not shown here.
