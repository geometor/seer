import numpy as np
from typing import List, Tuple, Dict, Any

# COLOR_MAP and other helper functions (if any) would be defined here.

def get_substitution_map(input_grid, output_grid):
    """Determines the example-specific substitution mapping."""
    substitution_map = {}
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            substitution_map[input_grid[i, j]] = output_grid[i, j]
    return substitution_map

def transform(input_grid, output_grid):
    # Determine the example-specific mapping.
    substitution_map = get_substitution_map(input_grid, output_grid)

    # Apply the Mapping
    transformed_grid = np.copy(input_grid) # make a copy of the input to modify
    for row_index, row in enumerate(input_grid):
        for col_index, value in enumerate(row):
            if value in substitution_map:
                transformed_grid[row_index, col_index] = substitution_map[value]

    return transformed_grid
                
def compare_grids(grid1: np.ndarray, grid2: np.ndarray) -> Tuple[bool, int, bool, bool, bool]:
    """Compares two grids and returns a tuple of results."""
    if grid1.shape != grid2.shape:
        return False, -1, False, False, False

    pixels_off = np.sum(grid1 != grid2)
    size_correct = True
    color_palette_correct = set(np.unique(grid1)) == set(np.unique(grid2))

    # Check if counts of each unique color are the same
    correct_pixel_counts = True
    unique_colors = np.unique(grid1)
    for color in unique_colors:
        if np.sum(grid1 == color) != np.sum(grid2 == color):
            correct_pixel_counts = False
            break

    return (pixels_off == 0), pixels_off, size_correct, color_palette_correct, correct_pixel_counts

def run_test(train_examples):
    report = ""
    for i, (input_grid, output_grid) in enumerate(train_examples):

        input_np = np.array(input_grid)
        output_np = np.array(output_grid)
        
        transformed_grid = transform(input_np, output_np)
        match, pixels_off, size_correct, color_palette_correct, correct_pixel_counts = compare_grids(transformed_grid, output_np)

        report += f"## Example {i+1}:\n"
        report += f"Input:\n```\n{input_np}\n```\n"
        report += f"Expected Output:\n```\n{output_np}\n```\n"
        report += f"Transformed Output:\n```\n{transformed_grid}\n```\n"
        report += f"match: {match}\n"
        report += f"pixels_off: {pixels_off}\n"
        report += f"size_correct: {size_correct}\n"
        report += f"color_palette_correct: {color_palette_correct}\n" #this metric is not relevant here
        report += f"correct_pixel_counts: {correct_pixel_counts}\n" #this metric is not relevant here
        report += "\n"
    return report

# Example Usage (replace with actual data)
train_examples = [
    ([[3, 1, 2], [3, 1, 2], [3, 1, 2]], [[4, 5, 6], [4, 5, 6], [4, 5, 6]]),
    ([[2, 3, 8], [2, 3, 8], [2, 3, 8]], [[6, 4, 9], [6, 4, 9], [6, 4, 9]]),
    ([[5, 8, 6], [5, 8, 6], [5, 8, 6]], [[1, 9, 2], [1, 9, 2], [1, 9, 2]]),
    ([[9, 4, 2], [9, 4, 2], [9, 4, 2]], [[8, 3, 6], [8, 3, 6], [8, 3, 6]]),
]
report = run_test(train_examples)
print(report)
