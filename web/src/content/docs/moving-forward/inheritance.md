---
title: Reuse with inheritance
description: Create a specialized class by extending and overriding an existing one.
---

Inheritance connects two classes when one is a more specific kind of the other. A timed task is a task with extra information. That is a reasonable **is-a relationship**. A task list contains tasks, but it is not itself a task, so inheritance would be the wrong relationship there.

## Start with a working base class

The more general class is the **base class**, also called a parent class or superclass. The specialized class is the **derived class**, also called a child class or subclass.

```python title="Try after the Task class from the previous lesson"
class TimedTask(Task):
    def __init__(self, title, minutes):
        super().__init__(title)
        self.minutes = minutes

    def describe(self):
        original_description = super().describe()
        return original_description + f" ({self.minutes} minutes)"
```

`TimedTask(Task)` declares the relationship. `super().__init__(title)` runs the base class initialization before the subclass stores its extra attribute.

An inherited method remains available unless the subclass replaces it. A `TimedTask` can call `complete()` even though that method is written only in `Task`.

## Override behavior carefully

Defining `describe()` again in `TimedTask` is **method overriding**. When you call it on a timed task, the subclass version takes precedence.

The method still uses `super().describe()` instead of repeating the base class logic. It keeps the existing description and adds the duration. If the base behavior changes later, the subclass receives that change too.

## Check the relationship before inheriting

Inheritance can remove repeated code, but that alone is not enough reason to use it. Ask:

1. Is every instance of the subclass genuinely a kind of the base class?
2. Should it keep most of the base behavior?
3. Can someone understand the relationship without reading every method?

If the answer is no, store one object inside another or use separate functions instead. A budget has expenses. A budget is not an expense.

## Practice: add a deadline task

Create a `DeadlineTask` subclass of `Task`. Add a due date or due label. Override `describe()` so it keeps the original task description and adds the deadline.

Then make one ordinary task and one deadline task. Put both in the same list and call `describe()` on each. The loop should not need to know which class each item uses.

Once that works, decide how overdue status should behave. You may store a simple boolean first or explore Python's `datetime` module later. Keep the first version small enough to test by reading its output.

The official [inheritance tutorial](https://docs.python.org/3/tutorial/classes.html#inheritance) explains multiple inheritance and other details. Begin with one base class and one subclass until method lookup feels predictable.
