import numpy as np

def analyze_changes(input_grid, expected_grid, transformed_grid):
    """Analyzes changes between input, expected, and transformed grids."""

    input_grid = np.array(input_grid)
    expected_grid = np.array(expected_grid)
    transformed_grid = np.array(transformed_grid)

    print("Input Grid:")
    print(input_grid)
    print("Expected Grid:")
    print(expected_grid)
    print("Transformed Grid (from current code):")
    print(transformed_grid)


    # Find mismatched coordinates
    mismatched_coords_expected = np.where(input_grid != expected_grid)
    mismatched_coords_transformed = np.where(input_grid != transformed_grid)

    print("\nCoordinates Changed in Expected Output:")
    for y, x in zip(*mismatched_coords_expected):
        print(f"  ({y}, {x}): Input={input_grid[y, x]}, Expected={expected_grid[y, x]}")

    print("\nCoordinates Changed in Transformed Output (Current Code):")
    for y, x in zip(*mismatched_coords_transformed):
        print(f"  ({y}, {x}): Input={input_grid[y, x]}, Transformed={transformed_grid[y, x]}")
    print("-" * 20)

# Example Data
examples = [
    {
        "input": [[2, 2, 1], [2, 1, 2], [2, 8, 1]],
        "expected": [[1, 8, 2], [2, 1, 2], [1, 2, 2]],
        "transformed": [[2, 2, 1], [2, 1, 2], [8, 2, 1]],
    },
    {
        "input": [[9, 2, 4], [2, 4, 4], [2, 9, 2]],
        "expected": [[2, 9, 2], [4, 4, 2], [4, 2, 9]],
        "transformed": [[9, 2, 4], [2, 4, 4], [9, 2, 2]],
    },
    {
        "input": [[8, 8, 8], [5, 5, 8], [8, 5, 5]],
        "expected": [[5, 5, 8], [8, 5, 5], [8, 8, 8]],
        "transformed": [[8, 8, 8], [5, 5, 8], [5, 8, 5]],
    },
    {
        "input": [[3, 2, 9], [9, 9, 9], [2, 3, 3]],
        "expected": [[3, 3, 2], [9, 9, 9], [9, 2, 3]],
        "transformed": [[3, 2, 9], [9, 9, 9], [3, 2, 3]],
    },
]

for i, example in enumerate(examples):
    print(f"Example {i + 1}:")
    analyze_changes(example["input"], example["expected"], example["transformed"])
