import numpy as np
from collections import Counter

def grid_metrics(grid):
    grid_array = np.array(grid)
    height, width = grid_array.shape
    color_counts = Counter(grid_array.flatten())
    return height, width, color_counts

examples = [
    {
        "input": [[4, 5, 1, 1, 5, 4, 4, 5, 1], [5, 5, 5, 5, 5, 5, 5, 5, 5], [1, 5, 4, 4, 5, 1, 1, 5, 4]],
        "expected": [[4, 5, 1], [5, 5, 5], [1, 5, 4]],
        "transformed": [[4, 1, 5, 4, 1], [5, 5, 5, 5, 5], [1, 4, 5, 1, 4]]
    },
    {
        "input": [[2, 0, 0, 1, 2, 0, 0, 1, 2, 0, 0, 1], [4, 2, 1, 4, 4, 2, 1, 4, 4, 2, 1, 4], [4, 1, 2, 4, 4, 1, 2, 4, 4, 1, 2, 4], [1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 0, 2]],
        "expected": [[2, 0, 0, 1], [4, 2, 1, 4], [4, 1, 2, 4], [1, 0, 0, 2]],
        "transformed": [[2, 0, 2, 0, 2, 0], [4, 1, 4, 1, 4, 1], [4, 2, 4, 2, 4, 2], [1, 0, 1, 0, 1, 0]]
    },
    {
        "input": [[2, 1, 2, 1, 2, 1], [2, 3, 2, 3, 2, 3]],
        "expected": [[2, 1], [2, 3]],
        "transformed": [[2, 2, 2], [2, 2, 2]]
    }
]

for i, example in enumerate(examples):
    input_h, input_w, input_colors = grid_metrics(example["input"])
    expected_h, expected_w, expected_colors = grid_metrics(example["expected"])
    transformed_h, transformed_w, transformed_colors = grid_metrics(example["transformed"])

    print(f"Example {i+1}:")
    print(f"  Input:      Height={input_h}, Width={input_w}, Colors={input_colors}")
    print(f"  Expected:   Height={expected_h}, Width={expected_w}, Colors={expected_colors}")
    print(f"  Transformed: Height={transformed_h}, Width={transformed_w}, Colors={transformed_colors}")