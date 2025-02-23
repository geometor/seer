"""
The transformation rule is a color mapping applied to each cell individually:

1. Identify the color of each cell in the input grid.
2. Apply a color mapping to each cell individually:
    - If the cell's color is 5 (gray), change it to 1 (blue).
    - If the cell's color is 8 (azure), change it to 9 (maroon).
    - If the cell's color is 6 (magenta), change it to 2 (red).
    - If the cell's color is 3 (green), change it to 4 (yellow).
    - If the cell's color is 1 (blue), change it to 5 (gray).
    - If the cell's color is 2 (red), change it to 6 (magenta).
    - If the cell's color is 9 (maroon), change it to 8 (azure).
    - If the cell's color is 4 (yellow), change it to 3 (green).
3. All other colors remain unchanged. The output grid has the exact
   same dimensions and structure as the input grid; only the specified
   colors are substituted.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping rule.
    """
    # Create a copy of the input grid to modify.
    output_grid = np.copy(input_grid)

    # Apply the color mapping to each cell.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 5:
                output_grid[i, j] = 1
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9
            elif output_grid[i, j] == 6:
                output_grid[i, j] = 2
            elif output_grid[i, j] == 3:
                output_grid[i,j] = 4
            elif output_grid[i, j] == 1:
                output_grid[i, j] = 5
            elif output_grid[i, j] == 2:
                output_grid[i, j] = 6
            elif output_grid[i, j] == 9:
                output_grid[i, j] = 8
            elif output_grid[i, j] == 4:
                output_grid[i, j] = 3

    return output_grid