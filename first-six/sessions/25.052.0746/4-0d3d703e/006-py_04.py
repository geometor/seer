"""
The transformation rule involves a one-to-one color mapping applied to an
input grid. The input and output grids have the same dimensions. Objects,
defined as vertical lines of uniform color, maintain their spatial properties
(position, size, shape) during the transformation. Only the color of each cell
changes according to a predefined color mapping.
"""

import numpy as np

def transform(input_grid, color_map=None):
    """
    Transforms the input grid by applying a color mapping while preserving
    the spatial structure.  A color_map must be provided.
    """
    # Initialize the output grid with the same dimensions as the input
    output_grid = np.copy(input_grid)

    # If no color map is given try to infer one.
    if color_map is None:
        print("Warning: No color_map provided. Cannot perform transformation.")
        return output_grid

    # Iterate through the input grid and apply the color mapping
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] in color_map:
                output_grid[i, j] = color_map[input_grid[i, j]]

    return output_grid