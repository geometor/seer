"""
Transforms a 3x3 input grid of gray (5) and white (0) pixels to an output grid of red (2) and yellow (4) pixels. 
The transformation depends on the row and column position of the pixels, as well as their initial color.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid
    output_grid = np.zeros_like(input_grid)

    # Iterate through each pixel in the input grid
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Gray pixel (5) - Row Dependent
            if input_grid[i, j] == 5:
                if i == 1:  # Middle row
                    output_grid[i, j] = 4  # Yellow
                elif i == 0:  # Top row
                    output_grid[i,j] = 2 # red
                elif i == 2: # Bottom row
                    output_grid[i,j] = 2 # red

            # White pixel (0) - position dependent
            elif input_grid[i,j] == 0:
                if i == 1 and j == 1:
                    output_grid[i,j] = 4
                elif i == 0:
                    output_grid[i,j] = 2
                elif i == 1 and (j == 0 or j == 2):
                    output_grid[i,j] = 2
                elif i == 2:
                   output_grid[i,j] = 2
    return output_grid