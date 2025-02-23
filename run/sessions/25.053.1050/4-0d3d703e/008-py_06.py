"""
The program performs a direct substitution of each pixel's value based on a mapping specific to each input/output pair.

1.  **Determine the Example-Specific Mapping:** For each example, a unique mapping is created. This mapping associates each pixel value present in the input grid with its corresponding pixel value in the output grid. The mapping is derived by comparing the values at identical positions (row, column) in the input and output grids.

2.  **Apply the Mapping:** Iterate through each pixel of the input grid. For every pixel, use its value as a key to look up the corresponding replacement value in the example-specific mapping. Replace the original pixel's value in the input grid with this new value from the mapping.  This is done in place on a copy of the input grid.

3.  The final output is the modified grid, which now contains the substituted values according to the determined mapping.
"""

import numpy as np
from typing import List, Dict

def get_substitution_map(input_grid: np.ndarray, output_grid: np.ndarray) -> Dict[int, int]:
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