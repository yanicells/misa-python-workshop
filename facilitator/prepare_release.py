"""Create a new, clean local Git repository. Never push or rewrite the source repo."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MAPPING = json.loads((ROOT / 'checkpoints.json').read_text())


def git(destination, *args):
    return subprocess.check_output(['git', '-C', str(destination), *args], text=True).strip()


def notebook(last_index):
    cells = [{"cell_type": "markdown", "metadata": {}, "source": [
        '# My MISA quiz\n',
        'Save a copy in Drive before editing. Follow the workshop guide and run one milestone at a time. Each code cell is a complete version.\n',
        'Choose a letter when prompted. Rerunning a milestone resets its scores. This notebook needs no extra packages or local Git.\n'
    ]}]
    for item in MAPPING[:last_index + 1]:
        stage = ROOT / 'web/src/examples' / item['id']
        description = f"## {item['id']}\n\nRead the [matching lesson](https://yanicells.github.io/misa-python-workshop/{item['lesson']}/). Edit this cell as the guide explains.\n"
        cells.append({'cell_type': 'markdown', 'metadata': {'milestone': item['id']}, 'source': description.splitlines(True)})
        code = ''
        if 'questions.py' in item['files']:
            code += (stage / 'questions.txt').read_text() + '\n'
        code += (stage / 'quiz.txt').read_text().replace('from questions import CLUSTERS, QUESTIONS\n', '')
        cells.append({'cell_type': 'code', 'execution_count': None, 'metadata': {'milestone': item['id']}, 'outputs': [], 'source': code.splitlines(True)})
    return {'cells': cells, 'metadata': {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}, 'language_info': {'name': 'python', 'version': '3.10'}, 'colab': {'name': 'misa-quiz.ipynb', 'provenance': []}}, 'nbformat': 4, 'nbformat_minor': 4}


def update_readmes():
    rows = ['| Checkpoint | Lesson |', '| --- | --- |']
    for item in MAPPING:
        rows.append(f"| [{item['id']}](https://github.com/yanicells/misa-python-workshop/tree/{item['id']}/workshop) | [Guide](https://yanicells.github.io/misa-python-workshop/{item['lesson']}/) |")
    for relative in ['README.md', 'workshop/README.md']:
        file = ROOT / relative
        source = file.read_text()
        before, rest = source.split('<!-- CHECKPOINTS:START -->')
        _, after = rest.split('<!-- CHECKPOINTS:END -->')
        file.write_text(before + '<!-- CHECKPOINTS:START -->\n' + '\n'.join(rows) + '\n<!-- CHECKPOINTS:END -->' + after)


def prepare(destination):
    if destination.exists():
        raise SystemExit('Destination already exists. Choose a new empty path; this script never overwrites a release.')
    update_readmes()
    shutil.copytree(ROOT, destination, ignore=shutil.ignore_patterns('.git', 'notes', 'node_modules', 'dist', '.astro', '__pycache__', '*.pyc', '.DS_Store', '.env', '.env.*'))
    git(destination, 'init', '-b', 'main')
    # Repository-local authorship for generated workshop release commits.
    git(destination, 'config', 'user.name', 'MISA Workshop Release')
    git(destination, 'config', 'user.email', 'workshop-release@users.noreply.github.com')
    git(destination, 'add', '.')
    git(destination, 'commit', '-m', 'Build MISA Python workshop guide and release tools')
    baseline = git(destination, 'rev-parse', 'HEAD')
    for index, item in enumerate(MAPPING):
        git(destination, 'checkout', '-b', item['id'], baseline)
        for file in item['files']:
            source = ROOT / 'web/src/examples' / item['id'] / file.replace('.py', '.txt')
            (destination / 'workshop' / file).write_text(source.read_text())
        (destination / 'workshop/misa-quiz.ipynb').write_text(json.dumps(notebook(index), indent=2) + '\n')
        git(destination, 'add', 'workshop')
        git(destination, 'commit', '-m', f"Add runnable checkpoint {item['id']}")
    git(destination, 'checkout', 'main')
    print(f'Clean release prepared: {destination}')
    print('Remote publication is a separate maintainer action. No push was performed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    prepare(args.destination.resolve())
