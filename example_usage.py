from adaptive_question_selector.question import Question
from adaptive_question_selector.selector import BayesianQuestionSelector

def main():
    question_bank = [
        Question(
            "What is the capital of France?",
            {'a': 'Berlin', 'b': 'Madrid', 'c': 'Paris', 'd': 'Rome'},
            'c'
        ),
        Question(
            "What is 2 + 2?",
            {'a': '3', 'b': '4', 'c': '5', 'd': '22'},
            'b'
        ),
        Question(
            "Which language is primarily used for Android development?",
            {'a': 'Kotlin', 'b': 'Swift', 'c': 'Ruby', 'd': 'C#'},
            'a'
        ),
        Question(
            "What planet is known as the Red Planet?",
            {'a': 'Venus', 'b': 'Saturn', 'c': 'Mars', 'd': 'Jupiter'},
            'c'
        )
    ]

    selector = BayesianQuestionSelector(question_bank)

    for _ in range(5):
        next_q = selector.select_question()
        if not next_q:
            print("No more questions available.")
            break

        print("\nNext Question:")
        is_correct = next_q.ask()
        selector.update(next_q.text, is_correct)

        print("Correct!" if is_correct else "Incorrect.")

    print("\n=== Current Question Stats ===")
    for q in question_bank:
        alpha = selector.alphas[q.text]
        beta = selector.betas[q.text]
        prob = alpha / (alpha + beta)
        print(f"{q.text} -> α: {alpha:.2f}, β: {beta:.2f}, P(correct): {prob:.2%}")

if __name__ == "__main__":
    main()
