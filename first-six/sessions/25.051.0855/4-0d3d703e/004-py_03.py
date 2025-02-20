"""
The transformation rule is a simple color substitution cipher applied to each cell of the input grid. The mapping is as follows:

1. **Color Substitution:**
   - If a cell's color is 3 (green), change it to 4 (yellow).
   - If a cell's color is 1 (blue), change it to 5 (gray).
   - If a cell's color is 2 (red), change it to 6 (magenta).
   - If a cell's color is 5 (gray), change it to 1(blue)
   - If a cell's color is 8 (azure), change it to 9 (maroon).
   - If a cell's color is 6 (magenta), change it to 2 (red)
    - If a cell's color is 9 (maroon), change it to 8 (azure).
    - If a cell's color is 4(yellow), change it to 3(green)
2. **Preservation of Structure:** The positions and arrangements of all cells remain unchanged. Only the color values within the cells are updated according to the mapping above.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the complete color mapping rule.
    """
    # Create a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Iterate over each cell in the grid
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply color substitution based on the defined mapping
            if output_grid[i, j] == 3:
                output_grid[i, j] = 4
            elif output_grid[i, j] == 1:
                output_grid[i, j] = 5
            elif output_grid[i, j] == 2:
                output_grid[i, j] = 6
            elif output_grid[i, j] == 5:
                output_grid[i, j] = 1
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9
            elif output_grid[i, j] == 6:
                output_grid[i,j] = 2
            elif output_grid[i,j] == 9:
                output_grid[i,j] = 8
            elif output_grid[i,j] == 4:
                output_grid[i,j] = 3
    return output_grid