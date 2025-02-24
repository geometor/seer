import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    metrics = {
        "input_shape": input_grid.shape,
        "expected_shape": expected_output.shape,
        "transformed_shape": transformed_output.shape,
        "match": np.array_equal(expected_output, transformed_output),
        "pixels_off": np.sum(expected_output != transformed_output) if not np.array_equal(expected_output, transformed_output) else 0
    }

    return metrics

# Example Data (from the prompt)
examples = [
    {
        "input": [
            [8, 9, 8],
            [9, 8, 8],
            [8, 8, 8],
            [2, 2, 1],
            [2, 2, 1],
            [1, 1, 2],
            [4, 4, 4],
            [4, 4, 3],
            [3, 3, 3]
        ],
        "expected": [
            [4, 4, 4],
            [4, 4, 3],
            [3, 3, 3]
        ],
        "transformed": [
            [4, 4, 4],
            [4, 4, 3],
            [3, 3, 3]
        ]
    },
     {
        "input": [
            [1, 5, 5],
            [5, 1, 1],
            [5, 1, 1],
            [3, 3, 3],
            [3, 6, 3],
            [3, 6, 6],
            [7, 7, 7],
            [7, 2, 2],
            [7, 2, 2]
        ],
        "expected": [
            [3, 3, 3],
            [3, 6, 3],
            [3, 6, 6]
        ],
        "transformed": [
           [7, 7, 7],
            [7, 2, 2],
            [7, 2, 2]
        ]
    },
    {
        "input": [
            [2, 2, 2],
            [2, 2, 3],
            [2, 3, 3],
            [5, 7, 7],
            [7, 5, 5],
            [7, 5, 5],
            [8, 8, 1],
            [1, 8, 1],
            [1, 8, 1]
        ],
        "expected": [
            [8, 8, 1],
            [1, 8, 1],
            [1, 8, 1]
        ],
        "transformed": [
            [8, 8, 1],
            [1, 8, 1],
            [1, 8, 1]
        ]
    },
    {
        "input": [
            [8, 8, 4],
            [4, 4, 4],
            [4, 4, 8],
            [1, 1, 3],
            [1, 3, 3],
            [3, 3, 1],
            [6, 2, 2],
            [2, 2, 2],
            [2, 2, 6]
        ],
        "expected": [
            [8, 8, 4],
            [4, 4, 4],
            [4, 4, 8]
        ],
        "transformed": [
            [6, 2, 2],
            [2, 2, 2],
            [2, 2, 6]
        ]
    }
]

# Analyze each example
for i, example in enumerate(examples):
    metrics = analyze_example(example["input"], example["expected"], example["transformed"])
    print(f"Example {i+1} Metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")