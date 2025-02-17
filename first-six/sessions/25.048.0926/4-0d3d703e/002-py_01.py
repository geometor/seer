"""
The transformation rule is a color mapping where each color in the input grid is
incremented by a specific value:
- Green (3) becomes Yellow (4) - increment by 1.
- Blue (1) becomes Gray (5) - increment by 4.
- Red (2) becomes Magenta (6) - increment by 4.
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
            if output_grid[i, j] == 3:  # Green
                output_grid[i, j] = 4  # Yellow
            elif output_grid[i, j] == 1:  # Blue
                output_grid[i, j] = 5  # Gray
            elif output_grid[i, j] == 2:  # Red
                output_grid[i, j] = 6  # Magenta

    return output_grid