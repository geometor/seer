import numpy as np
from collections import Counter

def analyze(grid):
    return Counter(grid.flatten())

examples = [
    {
        "input": np.array([[2, 2, 1], [2, 3, 1], [1, 1, 1]]),
        "expected": np.array([[1, 2, 3], [1, 2, 0], [1, 2, 0], [1, 0, 0], [1, 0, 0]]),
    },
    {
        "input": np.array([[3, 1, 1, 4], [2, 2, 2, 4], [4, 4, 4, 4]]),
        "expected": np.array([[4, 2, 1, 3], [4, 2, 1, 0], [4, 2, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0]]),
    },
    {
        "input": np.array([[8, 8, 2], [3, 8, 8], [3, 3, 4], [3, 3, 4]]),
        "expected": np.array([[3, 8, 4, 2], [3, 8, 4, 0], [3, 8, 0, 0], [3, 8, 0, 0], [3, 0, 0, 0]]),
    },
    {
        "input": np.array([[1, 1, 1], [2, 2, 1], [2, 8, 1], [2, 8, 1]]),
        "expected": np.array([[1, 2, 8], [1, 2, 8], [1, 2, 0], [1, 2, 0], [1, 0, 0], [1, 0, 0]]),
    },
]

for i, example in enumerate(examples):
    print(f"Example {i+1}:")
    print("Input Counts:", analyze(example["input"]))
    print("Expected Counts:", analyze(example["expected"]))
    print()
