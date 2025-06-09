# Adaptive Question Selector

This project implements a simple Bayesian approach to adaptively select the next best question for a learner based on their previous answers. It uses Beta distributions to update the probability of success and selects the next question closest to a target probability.

## Project Structure

- `selector.py`: Main class implementing the Bayesian update and selection logic.
- `utils.py`: Helper functions for reporting and debugging.
- `example_usage.py`: Demonstrates usage of the selector with simulated responses.
- `tests/test_selector.py`: Unit tests for the selector logic.

## Dependencies

- Python 3.8+
- numpy
- pytest>=7.0.0

## How to Install Dependencies

It's recommended to use a virtual environment to keep dependencies isolated. You can create and activate one as follows:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate
pip install -r requirements.txt
```

## How to Run

```bash
python3 example_usage.py
.\venv\Scripts\python.exe .\example_usage.py # to ensure venv python interpreter
```

## How to Test

```bash
python3 -m unittest tests/test_selector.py
```


## Question Selection Strategy

Question selector uses Bayesian statistics — specifically, the Beta distribution — to estimate how likely a student is to answer each question correctly. This helps guide the next question choice toward one that best matches a target difficulty level, typically set to 50% (i.e. medium difficulty).

## Step-by-Step Selection Logic

1. Track performance per question
Each question starts with:

alpha = 1 (number of correct answers + 1)

beta = 1 (number of incorrect answers + 1)

As the student answers:

If correct → alpha += 1

If incorrect → beta += 1

2. Estimate probability of success
For each unanswered question, we calculate:

```
P(success) = alpha / (alpha + beta)
```
This gives an estimate of how likely the student is to get the question correct, based on past performance.

3. Compare with target probability
You define a target_prob, usually 0.5 (50% correct), meaning:
“Ask the question the student is most uncertain about — not too easy, not too hard.”

The selector finds the question with a success probability closest to 0.5:

```
diff = abs(prob - target_prob)
```

It selects the question with the smallest difference from this target.


