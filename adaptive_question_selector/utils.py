def print_selector_status(selector):
    """
    Utility function to print the current alpha and beta values for all questions.
    """
    print("Current Beta Distribution parameters:")
    for q in selector.questions:
        print(f"Question: {q}, alpha: {selector.alpha[q]:.2f}, beta: {selector.beta[q]:.2f}")
