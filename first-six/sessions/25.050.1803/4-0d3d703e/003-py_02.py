"""
The transformation rule is a color-to-color replacement applied to each cell in the input grid.
Specifically:
- Color 2 (red) is transformed into color 6 (magenta).
- Color 3 (green) is transformed into color 4 (yellow).
- Color 8 (azure) is transformed into color 9 (maroon).
All instances of these input colors are replaced by their corresponding output colors to produce the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    2 (red) -> 6 (magenta)
    3 (green) -> 4 (yellow)
    8 (azure) -> 9 (maroon)
    """
    output_grid = np.copy(input_grid)

    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 2:
                output_grid[i, j] = 6
            elif output_grid[i, j] == 3:
                output_grid[i, j] = 4
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9

    return output_grid