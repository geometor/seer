import numpy as np

# Provided input and expected output grids for all examples
examples = [
    {
        "input": np.array([[0, 0, 5], [0, 5, 0], [5, 0, 0]]),
        "expected": np.array([[3, 3, 3], [4, 4, 4], [2, 2, 2]]),
    },
    {
        "input": np.array([[0, 0, 5], [0, 0, 5], [0, 0, 5]]),
        "expected": np.array([[3, 3, 3], [3, 3, 3], [3, 3, 3]]),
    },
    {
        "input": np.array([[5, 0, 0], [0, 5, 0], [5, 0, 0]]),
        "expected": np.array([[2, 2, 2], [4, 4, 4], [2, 2, 2]]),
    },
    {
        "input": np.array([[0, 5, 0], [0, 0, 5], [0, 5, 0]]),
        "expected": np.array([[4, 4, 4], [3, 3, 3], [4, 4, 4]]),
    },
]

# Analyze each example
for i, example in enumerate(examples):
    input_grid = example["input"]
    expected_output = example["expected"]
    print(f"Example {i+1}:")
    print(f"Expected Output unique values and counts: {np.unique(expected_output, return_counts=True)}")
    print(f"Input unique values and counts: {np.unique(input_grid, return_counts=True)}")

