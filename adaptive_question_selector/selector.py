import numpy as np
from adaptive_question_selector.question import Question 

class BayesianQuestionSelector:
    def __init__(self, questions: list[Question], initial_alpha=1.0, initial_beta=1.0):
        """
        Initialize with a list of Question objects.
        Each question has a .text property used as the unique key.
        """
        self.questions = questions

        # Verify all are Question instances
        for q in questions:
            if not isinstance(q, Question):
                raise TypeError("All elements in 'questions' must be instances of Question")

        self.alphas = {q.text: initial_alpha for q in questions}
        self.betas = {q.text: initial_beta for q in questions}
        self.asked_questions = set()

    def update(self, question_text: str, is_correct: bool):
        """
        Update alpha and beta based on whether the student's answer was correct.
        """
        
        if question_text not in self.alphas or question_text not in self.betas:
            raise ValueError(f"Question '{question_text}' not found in selector.")
        if is_correct:
            self.alphas[question_text] += 1
        else:
            self.betas[question_text] += 1
        self.asked_questions.add(question_text)
    

    def select_question(self, target_prob=0.5) -> Question | None:
        """
        Select the Question whose success probability is closest to the target.
        """
        min_diff = float('inf')
        next_question = None

        for question in self.questions:
            if question.text in self.asked_questions:
                continue

            alpha = self.alphas[question.text]
            beta = self.betas[question.text]

            # Estimate the probability of success
            prob = alpha / (alpha + beta)
            diff = abs(prob - target_prob)

            if diff < min_diff:
                min_diff = diff
                next_question = question

        return next_question

    def get_probabilities(self) -> dict[str, float]:
        """
        Return a dictionary of current success probabilities for each question.
        """
        return {
            q.text: self.alphas[q.text] / (self.alphas[q.text] + self.betas[q.text])
            for q in self.questions
        }
