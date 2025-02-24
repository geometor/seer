"""
The program takes the input, replaces blue pixels (1) with red pixels (2), and outputs the modified grid. White pixels (0) remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each pixel of the input grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Change output pixels: If the pixel is blue (1), change it to red (2).
            if output_grid[i, j] == 1:
                output_grid[i, j] = 2

    return output_grid