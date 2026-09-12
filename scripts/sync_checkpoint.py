"""Copy tested website examples into the matching checkpoint branch."""

import argparse
import json
from pathlib import Path
import shutil
import subprocess

from build_notebook import build_notebook


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "web" / "src" / "examples"
WORKSHOP = ROOT / "workshop"


def current_branch():
    return subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("checkpoint")
    args = parser.parse_args()

    mapping = json.loads(
        (ROOT / "web" / "src" / "data" / "checkpoints.json").read_text(encoding="utf-8")
    )
    checkpoint = next((item for item in mapping if item["id"] == args.checkpoint), None)
    if checkpoint is None:
        raise SystemExit(f"Unknown checkpoint: {args.checkpoint}")
    if current_branch() != args.checkpoint:
        raise SystemExit(
            f"Refusing to update {args.checkpoint} while on branch {current_branch()}"
        )

    for filename in checkpoint["files"]:
        source = EXAMPLES / args.checkpoint / filename.replace(".py", ".txt")
        shutil.copyfile(source, WORKSHOP / filename)

    notebook = build_notebook(args.checkpoint)
    (WORKSHOP / "misa-quiz.ipynb").write_text(
        json.dumps(notebook, indent=1) + "\n", encoding="utf-8"
    )
    print(f"Synced learner files and notebook for {args.checkpoint}.")


if __name__ == "__main__":
    main()
