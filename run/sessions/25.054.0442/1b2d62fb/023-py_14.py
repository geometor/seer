import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    rows, cols = input_grid.shape
    expected_rows, expected_cols = expected_output.shape
    transformed_rows, transformed_cols = transformed_output.shape

    metrics = {
        "input_shape": (rows, cols),
        "expected_output_shape": (expected_rows, expected_cols),
        "transformed_output_shape": (transformed_rows, transformed_cols),
        "pixels_off": np.sum(expected_output != transformed_output),
        "size_correct": (expected_rows, expected_cols) == (transformed_rows, transformed_cols),
    }
    return metrics

# Example Data (replace with your actual data)
examples = [
    {
        "input": [
            [0, 9, 9, 1, 9, 9, 9],
            [0, 0, 9, 1, 9, 9, 0],
            [9, 0, 9, 1, 9, 9, 0],
            [0, 0, 0, 1, 9, 0, 0],
            [0, 9, 9, 1, 9, 9, 9]
        ],
        "expected": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 8, 8],
            [0, 0, 0]
        ],
        "transformed": [
            [0, 0, 8],
            [0, 0, 0],
            [8, 0, 0],
            [0, 0, 0],
            [0, 0, 8]
        ]
    },
     {
        "input": [
            [0, 0, 0, 1, 9, 0, 0],
            [9, 0, 9, 1, 9, 9, 9],
            [0, 9, 9, 1, 9, 9, 9],
            [0, 0, 0, 1, 9, 9, 9],
            [0, 9, 9, 1, 9, 9, 9]
        ],
        "expected": [
            [0, 8, 8],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        "transformed": [
            [0, 0, 0],
            [8, 0, 8],
            [0, 0, 8],
            [0, 0, 8],
            [0, 0, 8]
        ]
    },
    {
        "input": [
           [9, 0, 0, 1, 9, 0, 9],
            [9, 0, 0, 1, 0, 9, 0],
            [9, 0, 0, 1, 9, 0, 0],
            [0, 9, 9, 1, 0, 9, 9],
            [0, 0, 9, 1, 0, 9, 0]
        ],
        "expected": [
            [0, 8, 0],
            [0, 0, 8],
            [0, 8, 8],
            [8, 0, 0],
            [8, 0, 0]
        ],
        "transformed": [
            [8, 0, 8],
            [8, 0, 0],
            [8, 0, 0],
            [0, 0, 8],
            [0, 0, 0]
        ]
    },
     {
        "input": [
            [0, 9, 9, 1, 9, 0, 9],
            [9, 0, 0, 1, 9, 0, 0],
            [9, 9, 9, 1, 9, 9, 9],
            [0, 9, 0, 1, 0, 0, 0],
            [9, 0, 0, 1, 9, 0, 0]
        ],
        "expected": [
            [0, 0, 0],
            [0, 8, 8],
            [0, 0, 0],
            [8, 0, 8],
            [0, 8, 8]
        ],
        "transformed": [
            [0, 0, 8],
            [8, 0, 0],
            [8, 0, 8],
            [0, 0, 0],
            [8, 0, 0]
        ]
    },
     {
        "input": [
          [0, 9, 9, 1, 9, 0, 9],
            [9, 0, 9, 1, 9, 9, 9],
            [9, 9, 9, 1, 0, 0, 9],
            [9, 0, 0, 1, 9, 0, 0],
            [9, 9, 9, 1, 0, 0, 9]
        ],
        "expected": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 8, 8],
            [0, 0, 0]
        ],
        "transformed": [
            [0, 0, 8],
            [8, 0, 8],
            [8, 0, 8],
            [8, 0, 0],
            [8, 0, 8]
        ]
    }

]

for i, example in enumerate(examples):
    metrics = analyze_example(example["input"], example["expected"], example["transformed"])
    print(f"Example {i+1}:")
    print(f"  Input Shape: {metrics['input_shape']}")
    print(f"  Pixels Off: {metrics['pixels_off']}")
    print(f"  Size Correct: {metrics['size_correct']}")
    print("-" * 20)
