"""
The transformation rule is to reduce both the width and the height of the input grid by half. The output grid is formed by retaining the top-left quadrant of the input grid, resulting in dimensions that are half the height and half the width of the original.
"""

import numpy as np

def transform(input_grid):
    # Get input grid dimensions
    height = len(input_grid)
    width = len(input_grid[0])

    # Calculate new dimensions (half of original)
    new_height = height // 2
    new_width = width // 2

    # Initialize output grid with correct dimensions, filled by zeros to begin
    output_grid = np.zeros((new_height, new_width), dtype=int)
    
    # Copy the relevant portion (top-left quadrant) of the input grid to the output grid
    for i in range(new_height):
        for j in range(new_width):
            output_grid[i][j] = input_grid[i][j]

    return output_grid