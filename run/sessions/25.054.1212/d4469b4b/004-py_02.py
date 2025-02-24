"""
Superimpose a 3x3 grid over the 5x5 input grid, creating nine overlapping 3x3 regions.
For each region:
  - If any pixel within the region is not white (value is not 0), the corresponding output pixel is gray (value 5).
  - If all pixels within the region are white (value 0), the corresponding output pixel is white (value 0).
Output a 3x3 grid.
"""

import numpy as np

def get_region(input_grid, row_start, col_start):
    """Helper function to extract a 3x3 region from the input grid."""
    return input_grid[row_start:row_start+3, col_start:col_start+3]

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    input_grid = np.array(input_grid)  # Ensure numpy array for easy slicing
    output_grid = np.zeros((3, 3), dtype=int)  # Initialize output grid with zeros (white)

    # Iterate through the nine overlapping 3x3 regions
    for i in range(3):
        for j in range(3):
            region = get_region(input_grid, i, j)
            if np.any(region != 0):  # Check for any non-white pixels
                output_grid[i, j] = 5  # Set to gray
            else:
                output_grid[i,j] = 0 # Set to white

    return output_grid.tolist()