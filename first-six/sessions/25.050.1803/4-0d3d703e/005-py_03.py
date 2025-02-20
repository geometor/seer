"""
The transformation rule is a color-to-color replacement applied to each cell in the input grid.
Specifically, color 5 (gray) is replaced with color 1 (blue), color 8 (azure) is replaced with color 9 (maroon), and color 6 (magenta) is replaced with color 2 (red).
Each instance of these input colors is substituted with their corresponding output colors to generate the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    5 (gray) -> 1 (blue)
    8 (azure) -> 9 (maroon)
    6 (magenta) -> 2 (red)
    """
    output_grid = np.copy(input_grid)

    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 5:
                output_grid[i, j] = 1
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9
            elif output_grid[i, j] == 6:
                output_grid[i, j] = 2

    return output_grid