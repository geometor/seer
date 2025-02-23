"""
The transformation rule is a color replacement:
1. Yellow (4) pixels in the input become gray (5) in the output.
2. Red (2) or green (3) pixels in the input become white (0) in the output.
3. Pixel positions remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Iterate through each cell of the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply the color transformation rules.
            if input_grid[i, j] == 4:
                output_grid[i, j] = 5
            elif input_grid[i, j] == 2 or input_grid[i, j] == 3:
                output_grid[i, j] = 0
            else:
                output_grid[i,j] = input_grid[i,j] # added to handle other cases in future examples

    return output_grid