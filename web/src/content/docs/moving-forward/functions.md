---
title: Make functions predictable
description: Understand return values, None, early returns, defaults, and scope.
---

The quiz used functions to give names to separate jobs. A good function has a clear input, does one understandable piece of work, and gives its caller a result when needed.

## Separate returning from printing

`return` sends a value back to the place where the function was called. `print()` only writes something to the screen.

```python title="Try in scratch.py"
def percentage(points, total):
    if total == 0:
        return 0
    return points / total * 100

result = percentage(3, 5)
print(result)
```

Because the function returns a number, the caller can print it, compare it, round it, or store it. A function that only prints is fine when printing is its whole job, but the printed text cannot be used as a number later.

## Understand None

If execution reaches the end of a function without a `return`, Python returns `None`. `None` means that no value is present.

```python
def show_status(task):
    print("Working on", task)

returned_value = show_status("reviewer")
print(returned_value)
```

The first line of output is the status. The second is `None`. This often explains why assigning the result of `print()`, `append()`, or another action function does not produce the value you expected.

## Return early when the job is finished

A `return` ends the current function call. Any statement after an unconditional return cannot run.

```python
def describe_score(score):
    if score < 0:
        return "Invalid score"

    if score >= 75:
        return "Passed"

    return "Try again"
```

Each return handles one finished case. This can be easier to read than wrapping the rest of the function in several levels of `else` blocks.

## Use parameters instead of hidden dependencies

Names created inside a function are normally **local** to that call. A function can read some names from an enclosing or global scope, but passing the needed value as a parameter usually makes the dependency clearer.

```python
tax_rate = 0.12

def total_with_tax(price, rate):
    return price + price * rate

print(total_with_tax(100, tax_rate))
```

The function does not secretly depend on `tax_rate`. You can test it with a different rate by passing another argument.

## Add a sensible default

A **default argument** makes a parameter optional.

```python
def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"

print(greet("Sam"))
print(greet("Sam", greeting="Good morning"))
```

The second call uses a **keyword argument**, which names the parameter being supplied. Avoid using a list or dictionary as a default while you are starting out. Mutable defaults can keep changes between calls.

## Practice: a reusable price calculator

Write a function that accepts a price, quantity, and optional discount rate. It should return the final number instead of printing it. Decide what should happen for a negative price, a quantity of zero, and a discount above 100 percent.

Call it with several sets of arguments. Print the results outside the function. Once the calculations work, add a separate function that formats one result for display.

The official tutorial explains more about [defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) and [Python scopes](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces).
