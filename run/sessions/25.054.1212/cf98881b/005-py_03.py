import numpy as np
from collections import Counter

def analyze_results(input_grid, expected_grid, transformed_grid):
    input_grid = np.array(input_grid)
    expected_grid = np.array(expected_grid)
    transformed_grid = np.array(transformed_grid)

    input_colors = Counter(input_grid.flatten())
    expected_colors = Counter(expected_grid.flatten())
    transformed_colors = Counter(transformed_grid.flatten())

    print("Input Colors:", input_colors)
    print("Expected Colors:", expected_colors)
    print("Transformed Colors:", transformed_colors)
    print("Shape - Input:", input_grid.shape, "Expected:", expected_grid.shape, "Transformed:", transformed_grid.shape)

    # check for target color columns.
    target_columns = []
    target_colors = [9,4,1]
    for j in range(input_grid.shape[1]):
        for i in range(input_grid.shape[0]):
            if input_grid[i,j] in target_colors:
                target_columns.append(j)
                break # next col

    print("Target Columns:", target_columns)

    # Check for color preservation.
    color_preservation_counts = {}
    for color in target_colors:
        color_preservation_counts[color] = {
            'input' : 0,
            'expected': 0,
            'transformed': 0
        }
      
    # count total target color pixels in input.
    for i in range(input_grid.shape[0]):
      for j in range(input_grid.shape[1]):
        color = input_grid[i,j]
        if color in target_colors:
            color_preservation_counts[color]['input'] += 1

    # count expected pixels.
    for i in range(expected_grid.shape[0]):
        for j in range(expected_grid.shape[1]):
            color = expected_grid[i,j]
            if color in target_colors:
                color_preservation_counts[color]['expected'] += 1
            
    # count transformed pixels.
    for i in range(transformed_grid.shape[0]):
      for j in range(transformed_grid.shape[1]):
        color = transformed_grid[i,j]
        if color in target_colors:
            color_preservation_counts[color]['transformed'] += 1
    print("Color counts (9,4,1):", color_preservation_counts)
# Example Data (replace with your actual data)
examples = [
    {
        "input": [
            [0, 4, 0, 4, 2, 9, 9, 0, 0, 2, 0, 0, 0, 0],
            [0, 4, 0, 0, 2, 0, 0, 9, 9, 2, 0, 1, 0, 0],
            [4, 0, 0, 0, 2, 0, 0, 0, 0, 2, 1, 1, 1, 0],
            [4, 4, 4, 4, 2, 9, 0, 9, 0, 2, 1, 1, 0, 1]
        ],
        "expected": [
            [9, 4, 0, 4],
            [0, 4, 9, 9],
            [4, 1, 1, 0],
            [4, 4, 4, 4]
        ],
        "transformed": [
            [4, 4, 9, 9],
            [4, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 4, 9, 0]
        ]
    },
   {
        "input": [
            [4, 4, 4, 4, 2, 9, 0, 9, 0, 2, 0, 0, 0, 1],
            [4, 4, 0, 0, 2, 9, 9, 0, 0, 2, 1, 0, 0, 0],
            [4, 0, 4, 4, 2, 0, 0, 0, 9, 2, 0, 1, 0, 1],
            [0, 0, 0, 0, 2, 0, 0, 9, 0, 2, 1, 0, 1, 0]
        ],
        "expected": [
            [4, 4, 4, 4],
            [4, 4, 0, 0],
            [4, 1, 4, 4],
            [1, 0, 9, 0]
        ],
        "transformed": [
            [4, 4, 4, 4],
            [4, 4, 0, 0],
            [4, 0, 4, 4],
            [0, 0, 0, 0]
        ]
    },
    {
        "input": [
            [4, 4, 4, 0, 2, 9, 9, 0, 9, 2, 0, 1, 0, 1],
            [0, 4, 0, 4, 2, 0, 0, 9, 0, 2, 0, 1, 0, 0],
            [0, 4, 0, 4, 2, 0, 0, 9, 9, 2, 1, 0, 0, 1],
            [4, 0, 4, 4, 2, 9, 9, 9, 0, 2, 0, 0, 0, 1]
        ],
        "expected": [
            [4, 4, 4, 9],
            [0, 4, 9, 4],
            [1, 4, 9, 4],
            [4, 9, 4, 4]
        ],
        "transformed": [
            [4, 4, 4, 9],
            [0, 4, 0, 0],
            [0, 4, 0, 0],
            [4, 0, 4, 9]
        ]
    },
    {
        "input": [
            [0, 0, 0, 4, 2, 0, 0, 0, 9, 2, 0, 0, 0, 0],
            [4, 4, 0, 4, 2, 9, 0, 9, 0, 2, 0, 0, 0, 0],
            [4, 0, 4, 4, 2, 0, 9, 9, 0, 2, 1, 1, 0, 1],
            [0, 4, 4, 4, 2, 0, 9, 0, 0, 2, 1, 1, 1, 1]
        ],
        "expected": [
            [0, 0, 0, 4],
            [4, 4, 9, 4],
            [4, 9, 4, 4],
            [1, 4, 4, 4]
        ],
        "transformed": [
            [4, 9, 0, 0],
            [4, 0, 4, 4],
            [4, 0, 4, 0],
            [4, 0, 0, 4]
        ]
    },
    {
        "input": [
            [4, 0, 4, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 1],
            [4, 4, 4, 4, 2, 0, 0, 0, 9, 2, 1, 1, 0, 0],
            [0, 4, 4, 4, 2, 0, 9, 9, 0, 2, 1, 1, 0, 1],
            [0, 4, 4, 0, 2, 0, 0, 9, 0, 2, 0, 1, 0, 1]
        ],
        "expected": [
            [4, 0, 4, 1],
            [4, 4, 4, 4],
            [1, 4, 4, 4],
            [0, 4, 4, 1]
        ],
        "transformed": [
            [4, 4, 1, 0],
            [4, 4, 0, 4],
            [0, 4, 1, 4],
            [0, 4, 1, 4]
        ]
    }
]

for i, example in enumerate(examples):
    print(f"--- Example {i+1} ---")
    analyze_results(example["input"], example["expected"], example["transformed"])
