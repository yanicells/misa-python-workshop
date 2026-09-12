---
title: For facilitators
description: A pacing guide, demo instructions, and checks to run before teaching.
---

Use the website as the teaching surface, including introductions and closing. Help students finish a personalized project, and let them copy full files when typing would make them miss the explanation. Any separate presentation materials are managed outside this repository.

## Pacing target

| Segment | Minutes | Teaching check |
| --- | ---: | --- |
| Introductions and destination | 5 | Show a finished quiz run |
| Setup and starting branch | 6 | Everyone sees the starter message |
| Greeting, values, first commit | 8 | Name prompt works and is committed |
| One question and validation | 10 | Invalid answer retries |
| Data, loops, and scoring | 13 | Seven numbered questions work |
| Functions | 8 | Refactor preserves the score dictionary |
| Percentages and tied ranks | 10 | All-a answers show seven tied results |
| Improve the quiz | 8 | Fifteen weighted questions award 45 points |
| Test and personalize | 7 | A neighbor tries the finished quiz |
| Closing | 3 | Point to the follow-up guide |

Total target: 78 minutes. Reserve up to 12 more minutes for setup, recovery, and personalization. This schedule needs a timed human rehearsal; automated runs do not measure how long beginners need.

## Introductions with Python

In a separate presenter scratch file, use participant numbers rather than collecting personal information. Replace `participant_count` with the actual number present:

```python
import random

participant_count = 5
numbers = list(range(1, participant_count + 1))
intro_count = min(5, participant_count)
selected = random.sample(numbers, intro_count)
for number in selected:
    print(number)
```

`import` loads Python's random module. `sample` chooses without replacement. Briefly show the output, then invite the selected participants to introduce themselves; let anyone pass. The count must be a nonnegative integer. Don't teach all the helper syntax at this point.

## Before people arrive

Verify a fresh clone, all checkpoint commands, the final Colab link, and a saved personal notebook copy. Check Windows and macOS on actual laptops. Run the production site and test search, copy buttons, both themes, mobile navigation, and the steppers. Browser testing and Python checks in the repository help, but they do not replace a projector check or a timed rehearsal.

`main` must hold the guide, not the completed learner project. Publish all seven checkpoint branches before sharing setup commands. If the site is connected to Vercel, use `main` for production; Yani handles that setup and deployment separately. Before sharing the repository, manually confirm that temporary teaching inputs are absent from every public branch and from the build output.

## During the build

Pause after a run succeeds. Explain the next piece immediately before students use it. After copying the bank, ask one student to trace a chosen answer's cluster list; that matters more than typing the data.

Use the all-a run at checkpoint 05 to explain why seven results can share rank 1. On the final checkpoint, trace one answer that gives 2 primary points and 1 related point. Use the fixture on the test page to show a tie at rank 3. If time slips, cut repeated demonstrations and optional edits first. Keep the essential values, operators, conditions, loops, and completed results path.

## Sources and writing

MISA's supplied website provides the logo and mascot. Cluster associations and original result descriptions draw on the supplied MISA project-management context. The quiz uses only broad cluster roles; it contains no internal process documents, private links, or personal records.

The learner copy follows [Humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md): plain wording, specific claims, and no invented cluster facts. The website uses [Starlight](https://starlight.astro.build/), with the documentation layout requested in the build plan.
