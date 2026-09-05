"""Run with QUIZ_DIR pointing to an exported final checkpoint."""
import contextlib
import importlib.util
import io
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

project = Path(os.environ.get('QUIZ_DIR', 'workshop')).resolve()
sys.path.insert(0, str(project))

class QuizChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not (project / 'quiz.py').exists():
            cls.quiz = None
            return
        spec = importlib.util.spec_from_file_location('quiz', project / 'quiz.py')
        cls.quiz = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.quiz)

    def setUp(self):
        self.assertIsNotNone(self.quiz, 'Final checkpoint must supply quiz.py')

    def results(self, scores):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.quiz.show_results(scores)
        return output.getvalue()

    def test_single_and_double_awards(self):
        scores = {'HR': 0, 'Events': 0}
        self.quiz.award_points(scores, ['HR'])
        self.quiz.award_points(scores, ['HR', 'Events'])
        self.assertEqual(scores, {'HR': 2, 'Events': 1})

    def test_invalid_answers_retry_without_awarding(self):
        question = {'prompt': 'Pick one', 'choices': {'a': {'text': 'Help', 'clusters': ['HR']}}}
        with patch('builtins.input', side_effect=['', '9', ' A ']), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(self.quiz.ask_question(question), 'a')

    def test_dense_ranks_keep_every_third_rank_tie(self):
        scores = {'COMMS': 5, 'OSG': 4, 'MKT': 3, 'OET': 3, 'Events': 3, 'eServs': 2, 'HR': 0}
        output = self.results(scores)
        self.assertIn('1. COMMS | 25.0% of quiz points', output)
        self.assertIn('2. OSG | 20.0% of quiz points', output)
        for name in ['MKT', 'OET', 'Events']:
            self.assertIn(f'3. {name} (tied) | 15.0% of quiz points', output)
        self.assertNotIn('eServs |', output)
        self.assertNotIn('HR |', output)

    def test_fewer_positive_ranks(self):
        output = self.results({'COMMS': 1, 'HR': 1, 'OSG': 0})
        self.assertIn('1. HR (tied) | 50.0%', output)
        self.assertNotIn('2.', output)

    def test_zero_and_empty_scores(self):
        self.assertIn('No points yet', self.results({}))
        self.assertIn('No points yet', self.results({'HR': 0}))

    def test_rank_by_raw_points(self):
        output = self.results({'COMMS': 10001, 'HR': 10000, 'OSG': 9999})
        self.assertIn('1. COMMS | 33.3%', output)
        self.assertIn('2. HR | 33.3%', output)
        self.assertIn('3. OSG | 33.3%', output)
        self.assertNotIn('(tied)', output)

    def test_question_bank_balanced_and_valid(self):
        from questions import QUESTIONS, CLUSTERS
        self.assertEqual(len(QUESTIONS), 7)
        self.assertEqual(set(CLUSTERS), {'COMMS', 'OSG', 'MKT', 'OET', 'Events', 'eServs', 'HR'})
        opportunities = dict.fromkeys(CLUSTERS, 0)
        for question in QUESTIONS:
            self.assertEqual(list(question['choices']), ['a','b','c','d'])
            for choice in question['choices'].values():
                awards = choice['clusters']
                self.assertIn(len(awards), [1,2])
                self.assertEqual(len(awards), len(set(awards)))
                for cluster in awards:
                    self.assertIn(cluster, CLUSTERS)
                    opportunities[cluster] += 1
        self.assertEqual(set(opportunities.values()), {7})

if __name__ == '__main__':
    unittest.main()
