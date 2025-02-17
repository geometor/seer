"""
The transformation rule is a color mapping where each color in the input grid is
incremented or decremented by a specific value:
- Gray (5) becomes Blue (1) - decrement by 4.
- Azure (8) becomes Maroon (9) - increment by 1.
- Magenta (6) becomes Red (2) - decrement by 4.
The positions, sizes, and shapes of the colored regions remain the same.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Apply color transformation based on the rules
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 5:  # Gray
                output_grid[i, j] = 1  # Blue
            elif output_grid[i, j] == 8:  # Azure
                output_grid[i, j] = 9  # Maroon
            elif output_grid[i, j] == 6:  # Magenta
                output_grid[i, j] = 2  # Red

    return output_grid