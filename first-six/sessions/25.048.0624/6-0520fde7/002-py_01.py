"""
The transformation rule can be summarized as follows:

1. Identify the central pixel of the input grid and the vertical line object (color 5).
2. Check and Count the number of blue pixels (color 1) that surround the vertical line.
3. Create a 3x3 output grid filled with color 0.
4. If the count of surrounding blue pixels equals 2, set the central pixel of the output grid to color 2; otherwise, the output grid remains all zeros.
"""

import numpy as np

def find_central_pixel(grid):
    """Find and return the coordinates of the central pixel."""
    rows, cols = grid.shape
    center_row = rows // 2
    center_col = cols // 2
    return (center_row, center_col)

def count_surrounding_blue_pixels(grid, center_col):
    """Count the number of blue pixels (color 1) around the central column."""
    count = 0
    rows, cols = grid.shape
    
    for r in range(rows):
      if grid[r,center_col] == 5:
        if center_col > 0 and grid[r,center_col-1] == 1:
           count +=1
        if center_col < cols-1 and grid[r,center_col+1] == 1:
           count +=1
    return count

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Initialize output grid as 3x3 with all zeros
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the central pixel of the input grid
    center_row, center_col = find_central_pixel(input_grid)

    # Count surrounding blue pixels
    blue_count = count_surrounding_blue_pixels(input_grid, center_col)

    # Check if the central pixel should be 2
    if blue_count == 2:
        output_grid[1, 1] = 2

    return output_grid