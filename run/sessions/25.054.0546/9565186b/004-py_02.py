"""
Iterate through each pixel of the input grid. Azure, Red, Green, and Blue pixels are changed to gray. Yellow pixels remain Yellow.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each pixel in the grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the color transformation rules.
            if output_grid[i, j] == 8:  # Azure becomes gray.
                output_grid[i, j] = 5
            elif output_grid[i, j] == 2: # Red becomes gray
                output_grid[i,j] = 5
            elif output_grid[i, j] == 3: # Green becomes gray
                output_grid[i, j] = 5
            elif output_grid[i, j] == 1: # Blue becomes gray.
                output_grid[i, j] = 5
            elif output_grid[i, j] == 4:  # Yellow remains yellow.
                continue

    return output_grid