"""
Transformation Rule:

1. **Identify Objects:** For each column (vertical line) in the input grid, identify its color.
2. **Color Substitution**: Replace the color of each column based on the following mapping:
    *   If the color is Red (2), change the column to Magenta (6).
    *   If the color is Green (3), change the column to Yellow (4).
    *   If the color is Azure (8), change the column to Maroon (9).
3. **Preserve Structure:** The shape and position of the objects (columns) are maintained.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping rule.
    """
    output_grid = np.copy(input_grid)  # Create a copy to preserve structure.

    # Iterate through each cell in the grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the color substitution rules.
            if output_grid[i, j] == 2:  # Red to Magenta
                output_grid[i, j] = 6
            elif output_grid[i, j] == 3:  # Green to Yellow
                output_grid[i, j] = 4
            elif output_grid[i, j] == 8:  # Azure to Maroon
                output_grid[i, j] = 9

    return output_grid