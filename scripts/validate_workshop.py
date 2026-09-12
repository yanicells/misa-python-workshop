"""Run focused checks against the learner checkpoint examples."""

from collections import Counter
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "web" / "src" / "examples"


def read_example(checkpoint, filename):
    return (EXAMPLES / checkpoint / filename).read_text(encoding="utf-8")


def load_question_data(checkpoint):
    namespace = {}
    exec(read_example(checkpoint, "questions.txt"), namespace)
    return namespace["CLUSTERS"], namespace["QUESTIONS"]


def run_checkpoint(checkpoint, answers):
    with tempfile.TemporaryDirectory() as directory:
        temporary = Path(directory)
        for source in (EXAMPLES / checkpoint).glob("*.txt"):
            (temporary / source.with_suffix(".py").name).write_text(
                source.read_text(encoding="utf-8"), encoding="utf-8"
            )
        completed = subprocess.run(
            [sys.executable, "quiz.py"],
            input=answers,
            text=True,
            capture_output=True,
            cwd=temporary,
            check=True,
        )
        return completed.stdout


def validate_python_syntax():
    for path in EXAMPLES.glob("*/*.txt"):
        compile(path.read_text(encoding="utf-8"), str(path), "exec")


def validate_early_question_bank():
    first = read_example("03-loops", "questions.txt")
    assert first == read_example("04-functions", "questions.txt")
    assert first == read_example("05-results", "questions.txt")

    clusters, questions = load_question_data("03-loops")
    assert len(questions) == 7
    for question in questions:
        assert set(question["choices"]) == {"a", "b", "c", "d"}
        for choice in question["choices"].values():
            assert 1 <= len(choice["clusters"]) <= 2
            assert set(choice["clusters"]) <= set(clusters)


def validate_weighted_question_bank():
    clusters, questions = load_question_data("06-improve")
    assert len(questions) == 15
    opportunities = Counter()

    for question in questions:
        assert question["prompt"].strip()
        assert set(question["choices"]) == {"a", "b", "c", "d"}
        for choice in question["choices"].values():
            points = choice["points"]
            assert choice["text"].strip()
            assert len(points) == 2
            assert set(points) <= set(clusters)
            assert sorted(points.values()) == [1, 2]
            assert sum(points.values()) == 3
            opportunities.update(points)

    assert max(opportunities.values()) - min(opportunities.values()) <= 1
    assert sorted(opportunities.values()) == [25, 25, 26, 26, 26, 26, 26]


def validate_runs():
    assert "Your MISA quiz starts here." in run_checkpoint("00-start", "")
    assert "Hi, Alex!" in run_checkpoint("01-welcome", "Alex\n")

    question_output = run_checkpoint("02-question", "Alex\nz\n A \n")
    assert "Please type a, b, or c." in question_output
    assert "eServices is the closest match" in question_output

    seven_answers = "Alex\n" + "a\n" * 7
    for checkpoint in ("03-loops", "04-functions", "05-results"):
        output = run_checkpoint(checkpoint, seven_answers)
        assert "Question 1 of 7" in output
        assert "Question 7 of 7" in output

    final_answers = "\nAlex\nz\n" + "a\n" * 15
    final_output = run_checkpoint("06-improve", final_answers)
    assert "Please enter a name or nickname." in final_output
    assert "Please type one of the letters shown." in final_output
    assert "Question 1 of 15" in final_output
    assert "Question 15 of 15" in final_output
    assert "Alex, here are your top MISA cluster matches:" in final_output


def main():
    validate_python_syntax()
    validate_early_question_bank()
    validate_weighted_question_bank()
    validate_runs()
    print("Workshop examples passed syntax, data, balance, and interaction checks.")


if __name__ == "__main__":
    main()
