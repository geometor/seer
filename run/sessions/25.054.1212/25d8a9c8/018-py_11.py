"""
The transformation rule is a color mapping applied to each pixel of the input grid. The mapping is as follows:

1.  Orange (7) pixels become White (0).
2.  Green (3) pixels become White (0).
3.  Gray (6) pixels become Gray (5).
4.  Red (2) pixels become White (0).
5.  Maroon (9) pixels become Gray (5).
6.  Yellow (4) pixels become Gray (5).
7.  Blue (1) pixels become Gray (5).
8.  All other colors remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping.
    """
    output_grid = np.copy(input_grid)  # Start with a copy to handle unchanged colors

    # Iterate through each pixel of the input grid
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply the color mapping
            if input_grid[i, j] == 7:
                output_grid[i, j] = 0
            elif input_grid[i, j] == 3:
                output_grid[i, j] = 0
            elif input_grid[i, j] == 6:
                output_grid[i, j] = 5
            elif input_grid[i, j] == 2:
                output_grid[i, j] = 0
            elif input_grid[i, j] == 9:
                output_grid[i, j] = 5  # Corrected mapping
            elif input_grid[i, j] == 4:
                output_grid[i, j] = 5  # Corrected mapping
            elif input_grid[i, j] == 1:
                output_grid[i, j] = 5

    return output_grid