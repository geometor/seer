"""
The transformation identifies the locations of the blue (1) and green (3) pixels in the input grid. It then replicates the pattern '1 0 0 3' (blue, white, white, green) horizontally across the entire row starting from the blue pixel's location, and vertically down the entire column starting from the green pixel's location, in the output grid.
"""

import numpy as np

def find_pixel(grid, color):
    """Finds the coordinates of the first occurrence of a specified color."""
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == color:
                return (i, j)
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the blue and green pixels
    blue_pos = find_pixel(input_grid, 1)
    green_pos = find_pixel(input_grid, 3)

    # Define the pattern
    pattern = [1, 0, 0, 3]

    # Horizontal replication (Blue)
    if blue_pos:
        row = blue_pos[0]
        for j in range(output_grid.shape[1]):
            output_grid[row, j] = pattern[j % len(pattern)]

    # Vertical replication (Green)
    if green_pos:
        col = green_pos[1]
        for i in range(output_grid.shape[0]):
            output_grid[i, col] = pattern[i % len(pattern)]
            
    return output_grid