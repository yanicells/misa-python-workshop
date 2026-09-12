"""Build the checkpoint notebook from the website's tested example files."""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "web" / "src" / "examples"
CHECKPOINTS = [
    ("00-start", "setup.mdx"),
    ("01-welcome", "build/welcome.mdx"),
    ("02-question", "build/question.mdx"),
    ("03-loops", "build/loops.mdx"),
    ("04-functions", "build/functions.mdx"),
    ("05-results", "build/results.mdx"),
    ("06-improve", "build/improve.mdx"),
]


def source_lines(text):
    return text.splitlines(keepends=True)


def markdown_cell(text):
    return {"cell_type": "markdown", "metadata": {}, "source": source_lines(text)}


def code_cell(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source_lines(text),
    }


def milestone_source(checkpoint):
    directory = EXAMPLES / checkpoint
    parts = []
    questions = directory / "questions.txt"
    if questions.exists():
        parts.append(questions.read_text(encoding="utf-8").rstrip())
    parts.append((directory / "quiz.txt").read_text(encoding="utf-8").rstrip())
    return "\n\n".join(parts) + "\n"


def build_notebook(through):
    cells = [
        markdown_cell(
            "# My MISA cluster quiz\n\n"
            "Save a copy in Drive before editing. Follow the workshop guide and run "
            "one milestone at a time. Each code cell is a complete version.\n\n"
            "Choose a letter when prompted. Rerunning a milestone resets its scores. "
            "This notebook needs no extra packages or local Git.\n"
        )
    ]

    for checkpoint, lesson in CHECKPOINTS:
        cells.append(
            markdown_cell(
                f"## {checkpoint}\n\n"
                "Read the [matching lesson]"
                f"(https://github.com/yanicells/misa-python-workshop/blob/main/web/src/content/docs/{lesson}). "
                "This cell is the complete checkpoint version.\n"
            )
        )
        cells.append(code_cell(milestone_source(checkpoint)))
        if checkpoint == through:
            break

    return {
        "cells": cells,
        "metadata": {
            "colab": {"name": "misa-quiz.ipynb", "provenance": []},
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.10"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--through", choices=[item[0] for item in CHECKPOINTS], required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    args.output.write_text(
        json.dumps(build_notebook(args.through), indent=1) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
