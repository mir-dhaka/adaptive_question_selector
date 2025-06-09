import unittest
from adaptive_question_selector.selector import BayesianQuestionSelector
from adaptive_question_selector.question import Question

class TestBayesianQuestionSelector(unittest.TestCase):

    def setUp(self):
        self.questions = [
            Question("Q1", {'a': 'Option 1', 'b': 'Option 2', 'c': 'Option 3', 'd': 'Option 4'}, 'a'),
            Question("Q2", {'a': 'Option A', 'b': 'Option B', 'c': 'Option C', 'd': 'Option D'}, 'b'),
            Question("Q3", {'a': 'Yes', 'b': 'No', 'c': 'Maybe', 'd': 'Sometimes'}, 'c'),
        ]
        self.selector = BayesianQuestionSelector(self.questions, initial_alpha=1.5, initial_beta=1.5)

    def test_initial_alpha_beta(self):
        for q in self.questions:
            self.assertAlmostEqual(self.selector.alphas[q.text], 1.5)
            self.assertAlmostEqual(self.selector.betas[q.text], 1.5)

    def test_update_correct(self):
        self.selector.update("Q1", True)
        self.assertEqual(self.selector.alphas["Q1"], 2.5)
        self.assertEqual(self.selector.betas["Q1"], 1.5)

    def test_update_incorrect(self):
        self.selector.update("Q2", False)
        self.assertEqual(self.selector.alphas["Q2"], 1.5)
        self.assertEqual(self.selector.betas["Q2"], 2.5)

    def test_select_question(self):
        # Make 'Q1' closer to target success probability
        self.selector.alphas["Q1"] = 5
        self.selector.betas["Q1"] = 2
        selected = self.selector.select_question(target_prob=0.7)
        self.assertEqual(selected.text, "Q1")

    def test_invalid_question_update(self):
        with self.assertRaises(ValueError):
            self.selector.update("Q5", True)

if __name__ == "__main__":
    unittest.main()
