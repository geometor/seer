"""
The input grid is a 3x3 grid of pixels. The output grid is also a 3x3 grid.
The transformation rule is:
- If an input pixel is yellow (4), change it to gray (5) in the output grid.
- If an input pixel is red (2), change it to white (0).
- If an input pixel is maroon (9), change it to gray (5) in the output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Iterate through each pixel of the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply the color transformation rules.
            if input_grid[i, j] == 4:  # Yellow
                output_grid[i, j] = 5  # Gray
            elif input_grid[i, j] == 2:  # Red
                output_grid[i, j] = 0  # White
            elif input_grid[i, j] == 9:  # Maroon
                output_grid[i, j] = 5  # Gray
            else:
                output_grid[i,j] = input_grid[i,j]

    return output_grid