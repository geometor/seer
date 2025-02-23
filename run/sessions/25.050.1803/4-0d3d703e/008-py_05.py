"""
The transformation rule is a color-to-color replacement applied to each cell in the input grid.  Specifically:
- Color 8 (azure) is transformed to color 1 (blue).
- Color 2 (red) is transformed to color 3 (green).
- Color 7 (orange) is transformed to color 4 (yellow).

Each instance of these input colors is substituted with its corresponding output colors to produce the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    8 (azure) -> 1 (blue)
    2 (red) -> 3 (green)
    7 (orange) -> 4 (yellow)
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Apply the color mapping by iterating through each cell.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 8:
                output_grid[i, j] = 1
            elif output_grid[i, j] == 2:
                output_grid[i, j] = 3
            elif output_grid[i, j] == 7:
                output_grid[i, j] = 4

    return output_grid