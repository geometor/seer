"""
The transformation rule is to reduce the width of the input grid by half, while keeping the height same. Take the original left most four columns and discard the right four columns. The output grid is formed by retaining the top-left quadrant (4x4) of the original input.
"""

import numpy as np

def transform(input_grid):
    """
    Reduces the width of the input grid by half, preserving the height.
    """
    # Get input grid dimensions
    height = len(input_grid)
    width = len(input_grid[0])

    # Calculate new width (half of original)
    new_width = width // 2

    # Initialize output grid with correct dimensions, filled by zeros to begin
    output_grid = np.zeros((height, new_width), dtype=int)
    
    # Copy the relevant portion of the input grid to the output grid
    for i in range(height):
        for j in range(new_width):
            output_grid[i][j] = input_grid[i][j]

    return output_grid