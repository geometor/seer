import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    input_maroon_positions = np.argwhere(input_grid == 9)
    expected_red_positions = np.argwhere(expected_output == 2)
    transformed_red_positions = np.argwhere(transformed_output == 2)

    print("Input Maroon Positions:", input_maroon_positions)
    print("Expected Red Positions:", expected_red_positions)
    print("Transformed Red Positions:", transformed_red_positions)
    print("---")

# Example Data
examples = [
    {
        "input": [
            [0, 9, 9],
            [0, 9, 9],
            [9, 9, 9],
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ],
        "expected": [
            [2, 0, 0],
            [2, 0, 0],
            [0, 0, 0]
        ],
        "transformed": [
            [0, 2, 2],
            [0, 2, 2],
            [2, 2, 2]
        ]
    },
    {
        "input": [
            [9, 0, 9],
            [0, 9, 9],
            [0, 0, 9],
            [1, 0, 1],
            [1, 0, 0],
            [1, 0, 0]
        ],
        "expected": [
            [0, 2, 0],
            [0, 0, 0],
            [0, 2, 0]
        ],
        "transformed": [
            [2, 0, 2],
            [0, 2, 2],
            [0, 0, 2]
        ]
    },
    {
        "input": [
            [0, 9, 0],
            [9, 0, 9],
            [9, 0, 0],
            [0, 0, 0],
            [0, 0, 1],
            [1, 0, 0]
        ],
        "expected": [
            [2, 0, 2],
            [0, 2, 0],
            [0, 2, 2]
        ],
        "transformed": [
            [0, 2, 0],
            [2, 0, 2],
            [2, 0, 0]
        ]
    },
    {
        "input": [
            [0, 0, 9],
            [9, 9, 9],
            [0, 9, 0],
            [1, 0, 0],
            [0, 1, 1],
            [0, 0, 1]
        ],
        "expected": [
            [0, 2, 0],
            [0, 0, 0],
            [2, 0, 0]
        ],
        "transformed": [
            [0, 0, 2],
            [2, 2, 2],
            [0, 2, 0]
        ]
    },
    {
        "input": [
            [0, 9, 0],
            [0, 9, 9],
            [0, 9, 9],
            [0, 0, 0],
            [1, 1, 1],
            [1, 0, 1]
        ],
        "expected": [
            [2, 0, 2],
            [0, 0, 0],
            [0, 0, 0]
        ],
        "transformed": [
            [0, 2, 0],
            [0, 2, 2],
            [0, 2, 2]
        ]
    }
]

for i, example in enumerate(examples):
    print(f"Example {i+1}:")
    analyze_example(example["input"], example["expected"], example["transformed"])
