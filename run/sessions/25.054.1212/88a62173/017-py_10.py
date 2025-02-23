import numpy as np
from collections import Counter

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    rows, cols = input_grid.shape
    row_mid = (rows + 1) // 2
    col_mid = (cols + 1) // 2
    quadrants = [
        (0, row_mid, 0, col_mid),
        (0, row_mid, col_mid, cols),
        (row_mid, rows, 0, col_mid),
        (row_mid, rows, col_mid, cols),
    ]

    quadrant_data = []
    for i, (row_start, row_end, col_start, col_end) in enumerate(quadrants):
        quadrant = input_grid[row_start:row_end, col_start:col_end]
        counts = Counter(quadrant.flatten())
        most_common = counts.most_common()
        quadrant_data.append({
            "quadrant_index": i,
            "most_common_colors": most_common,
            "output_pixel": (i // 2, i % 2),
            "expected_color": expected_output[i // 2, i % 2],
            "transformed_color": transformed_output[i // 2, i % 2]
        })

    return quadrant_data

# Example data (as lists, for easier handling)
examples = [
    {
        "input": [
            [0, 2, 0, 0, 2],
            [2, 2, 0, 2, 2],
            [0, 0, 0, 0, 0],
            [0, 2, 0, 2, 2],
            [2, 2, 0, 2, 0]
        ],
        "expected": [
            [2, 2],
            [2, 0]
        ],
        "transformed": [
            [0, 0],
            [0, 0]
        ]
    },
    {
        "input": [
            [1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 1, 0, 0, 1]
        ],
        "expected": [
            [1, 0],
            [1, 1]
        ],
        "transformed": [
            [0, 0],
            [0, 0]
        ]
    },
    {
        "input": [
            [8, 8, 0, 0, 8],
            [8, 0, 0, 8, 0],
            [0, 0, 0, 0, 0],
            [8, 8, 0, 8, 8],
            [8, 0, 0, 8, 0]
        ],
        "expected": [
            [0, 8],
            [8, 0]
        ],
        "transformed": [
            [0, 0],
            [0, 0]
        ]
    }
]

# Analyze all examples
analysis_results = []
for example in examples:
    analysis_results.append(analyze_example(example["input"], example["expected"], example["transformed"]))

# Print the results (formatted for readability)
for i, example_analysis in enumerate(analysis_results):
    print(f"Example {i+1}:")
    for quadrant_info in example_analysis:
        print(f"  Quadrant {quadrant_info['quadrant_index']} (Output Pixel: {quadrant_info['output_pixel']}):")
        print(f"    Most Common Colors: {quadrant_info['most_common_colors']}")
        print(f"    Expected Color: {quadrant_info['expected_color']}")
        print(f"    Transformed Color: {quadrant_info['transformed_color']}")
    print("-" * 40)