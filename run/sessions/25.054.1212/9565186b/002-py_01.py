"""
The transformation rule is:  If a pixel's color is blue (1) or azure (8), change it to gray (5). Otherwise, keep the original color.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rule: blue (1) or azure (8) pixels become gray (5).
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Get the dimensions of the grid
    rows, cols = output_grid.shape

    # Iterate through each pixel of the output grid.
    for i in range(rows):
        for j in range(cols):
            # Check if the pixel's color is blue (1) or azure (8).
            if output_grid[i, j] == 1 or output_grid[i, j] == 8:
                # Change the pixel's color to gray (5).
                output_grid[i, j] = 5

    # Return the modified grid.
    return output_grid