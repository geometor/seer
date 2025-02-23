"""
The input grid consists of three vertical lines of colors 2, 3, and 8.
The output grid has the same structure but substitutes each input color
with a distinct color according to the following mapping: 2 -> 6, 3 -> 4, 8 -> 9.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping while preserving
    the spatial structure.
    """
    # Initialize the output grid with the same dimensions as the input
    output_grid = np.copy(input_grid)

    # Define the color mapping
    color_map = {
        2: 6,
        3: 4,
        8: 9
    }

    # Iterate through the input grid and apply the color mapping
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] in color_map:
                output_grid[i, j] = color_map[input_grid[i, j]]

    return output_grid