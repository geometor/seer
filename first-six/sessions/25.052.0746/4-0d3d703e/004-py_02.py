"""
The transformation rule involves a one-to-one color mapping. The program examines each cell
in the input grid. If a cell's color is present in a predefined color mapping,
that color is replaced with the corresponding color from the mapping. Colors not in the
mapping remain unchanged. The spatial structure of the grid remains identical; only the
colors of certain cells are altered according to the mapping.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a complete color mapping while preserving
    the spatial structure.
    """
    # Initialize the output grid with the same dimensions as the input
    output_grid = np.copy(input_grid)

    # Define the complete color mapping, derived from all input/output examples
    color_map = {
        3: 4,
        1: 5,
        2: 6,
        8: 9,
        5: 1,
        9: 8,
        4: 3,
        6: 2
    }

    # Iterate through the input grid and apply the color mapping
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] in color_map:
                output_grid[i, j] = color_map[input_grid[i, j]]

    return output_grid