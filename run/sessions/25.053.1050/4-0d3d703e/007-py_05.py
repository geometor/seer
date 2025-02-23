"""
The task involves a color substitution. Each color in the input grid is consistently replaced with a corresponding color in the output grid. The spatial arrangement of the pixels remains unchanged; only the color values are altered. The substitution is specific to each example, and must be derived by comparing the input and output grids.
"""

import numpy as np

def get_substitution_map(input_grid, output_grid):
    """Determines the example-specific substitution mapping."""
    substitution_map = {}
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            substitution_map[input_grid[i, j]] = output_grid[i, j]
    return substitution_map

def transform(input_grid: np.ndarray, output_grid: np.ndarray) -> np.ndarray:
    # Determine the example-specific mapping.
    substitution_map = get_substitution_map(input_grid, output_grid)

    # Apply the Mapping
    transformed_grid = np.copy(input_grid) # make a copy of the input to modify
    for row_index, row in enumerate(input_grid):
        for col_index, value in enumerate(row):
            if value in substitution_map:
                transformed_grid[row_index, col_index] = substitution_map[value]

    return transformed_grid