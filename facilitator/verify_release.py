"""Verify an assembled release from local refs, using temporary fresh clones."""
import ast
import contextlib
import io
import json
from pathlib import Path
import os
import subprocess
import sys
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
MAPPING = json.loads((ROOT / 'checkpoints.json').read_text())


def run(*args, cwd=ROOT, input=None, env=None):
    return subprocess.check_output(args, cwd=cwd, text=True, input=input, env=env, stderr=subprocess.STDOUT)


branches = run('git', 'branch', '--format=%(refname:short)').split()
assert set(branches) == {'main', *(item['id'] for item in MAPPING)}, branches
# Codex may keep private turn-diff refs in the local repository. They are not
# part of the public release, so audit only local and remote branch refs.
paths = run('git', 'rev-list', '--objects', '--branches', '--remotes')
assert not any(' notes/' in line or 'session-02-python' in line for line in paths.splitlines())
main_files = run('git', 'ls-tree', '-r', '--name-only', 'main').splitlines()
assert not any(name in main_files for name in ['workshop/quiz.py','workshop/questions.py','workshop/misa-quiz.ipynb'])
base_web = run('git', 'rev-parse', 'main:web').strip()
with tempfile.TemporaryDirectory(prefix='misa-check-') as temporary:
    clone = Path(temporary) / 'learner'
    run('git', 'clone', '--no-local', str(ROOT), str(clone))
    run('git', 'config', 'user.name', 'Workshop Test', cwd=clone)
    run('git', 'config', 'user.email', 'test@example.invalid', cwd=clone)
    for item in MAPPING:
        run('git', 'checkout', item['id'], cwd=clone)
        assert run('git', 'rev-parse', f"{item['id']}:web", cwd=clone).strip() == base_web
        output = run(sys.executable, 'quiz.py', cwd=clone/'workshop', input='a\n'*7)
        assert item['expected'] in output, (item['id'],output)
        for name in item['files']:
            code = (clone/'workshop'/name).read_text()
            tree = ast.parse(code)
            forbidden = (ast.Lambda, ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp, ast.ClassDef)
            assert not any(isinstance(node, forbidden) for node in ast.walk(tree))
            example = ROOT/'web/src/examples'/item['id']/name.replace('.py','.txt')
            assert example.read_text() == code
        nb = json.loads((clone/'workshop/misa-quiz.ipynb').read_text())
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                result = io.StringIO()
                with contextlib.redirect_stdout(result), patch('builtins.input', side_effect=['a']*7):
                    exec(''.join(cell['source']), {'__name__':'__main__'})
                expected = next(row['expected'] for row in MAPPING if row['id']==cell['metadata']['milestone'])
                assert expected in result.getvalue()
        print('PASS checkpoint and notebook:',item['id'])
    env = dict(os.environ, QUIZ_DIR=str(clone/'workshop'))
    print(run(sys.executable,'-m','unittest','discover','-s',str(ROOT/'facilitator'),'-p','test_quiz.py',env=env))
    run('git','checkout','00-start',cwd=clone)
    run('git','checkout','-b','my-quiz',cwd=clone)
    custom = 'print("My personal greeting")\n'
    (clone/'workshop/quiz.py').write_text(custom)
    run('git','add','quiz.py',cwd=clone/'workshop')
    run('git','commit','-m','Save personal greeting',cwd=clone)
    run('git','fetch','origin',cwd=clone)
    run('git','checkout','-b','recovery-loops','origin/03-loops',cwd=clone)
    assert 'My personal greeting' not in (clone/'workshop/quiz.py').read_text()
    run('git','checkout','my-quiz',cwd=clone)
    assert (clone/'workshop/quiz.py').read_text()==custom
    print('PASS fresh clone and save/recover/return workflow')
print('PASS public-ref history and shared website baseline audit')
