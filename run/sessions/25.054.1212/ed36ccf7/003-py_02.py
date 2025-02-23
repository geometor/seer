def compare_grids(input_grid, expected_output_grid, transformed_output_grid):
    """Compares input, expected output, and transformed output grids pixel by pixel.

    Args:
        input_grid: The input grid.
        expected_output_grid: The expected output grid.
        transformed_output_grid: The transformed output grid.

    Returns:
        A dictionary containing pixel mappings and analysis.
    """

    analysis = {}
    height = len(input_grid)
    width = len(input_grid[0]) if height > 0 else 0

    for i in range(height):
        for j in range(width):
            input_pixel = input_grid[i][j]
            expected_pixel = expected_output_grid[i][j]
            transformed_pixel = transformed_output_grid[i][j]

            key = f"({i},{j})"
            analysis[key] = {
                "input": input_pixel,
                "expected": expected_pixel,
                "transformed": transformed_pixel,
            }

    return analysis
examples = [
    {
        "input": [
            [9, 0, 0],
            [9, 9, 9],
            [9, 9, 9]
        ],
        "expected": [
            [0, 9, 9],
            [0, 9, 9],
            [9, 9, 9]
        ],
        "transformed": [
            [9, 9, 9],
            [9, 9, 0],
            [9, 9, 0]
        ]
    },
    {
        "input": [
            [6, 6, 6],
            [0, 0, 0],
            [6, 6, 0]
        ],
        "expected": [
            [6, 0, 0],
            [6, 0, 6],
            [6, 0, 6]
        ],
        "transformed": [
            [6, 0, 6],
            [6, 0, 6],
            [0, 0, 6]
        ]
    },
    {
      "input": [
            [0, 0, 9],
            [0, 0, 9],
            [9, 9, 9]
      ],
      "expected": [
            [9, 9, 9],
            [0, 0, 9],
            [0, 0, 9]
        ],
        "transformed": [
            [9, 0, 0],
            [9, 0, 0],
            [9, 9, 9]
        ]
    },
    {
        "input": [
            [2, 0, 2],
            [0, 0, 2],
            [0, 2, 2]
        ],
        "expected": [
            [2, 2, 2],
            [0, 0, 2],
            [2, 0, 0]
        ],
        "transformed": [
            [0, 0, 2],
            [2, 0, 0],
            [2, 2, 2]
        ]
    }
]

report = {}
example_num = 1
for example in examples:
  report[f"example_{example_num}"] = compare_grids(example["input"], example["expected"], example["transformed"])
  example_num += 1

import yaml
print(yaml.dump(report))