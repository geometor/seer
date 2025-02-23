"""
Iterate through each pixel of the input grid. For every azure pixel, check its immediate horizontal neighbors (left and right) *in the original input grid*. If a neighbor is white, change that *original* white pixel to blue in the output grid. Do not change white pixels that became blue during the *current* transformation process. Only apply changes on the same row as the azure pixel.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing white pixels (0) horizontally adjacent to azure pixels (8) to blue (1),
    considering only the original input state.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of input_grid
    rows, cols = input_grid.shape

    # Iterate through each cell of the input_grid
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8:  # Check if the current cell is azure (8)
                # Check to the immediate right, using original input_grid for the check
                if c + 1 < cols and input_grid[r, c + 1] == 0:
                    output_grid[r, c + 1] = 1  # Change adjacent white pixel to blue
                # Check to the immediate left, using original input_grid for the check
                if c - 1 >= 0 and input_grid[r, c - 1] == 0:
                    output_grid[r, c - 1] = 1  # Change adjacent white pixel to blue

    return output_grid