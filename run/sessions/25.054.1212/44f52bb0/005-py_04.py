"""
Transforms an input grid of colored pixels into a 1x1 output grid. The output color is either blue (1) or orange (7).

The output is blue (1) if the red pixels form a continuous vertical or horizontal line across the entire grid (even if interrupted by other colors). 
Otherwise, if red pixels are present but do NOT form a continuous line across the grid, the output is orange (7).
"""

import numpy as np

def check_for_line(grid, color):
    """Checks if a continuous line of a given color exists horizontally or vertically."""
    rows, cols = grid.shape

    # Check for horizontal lines
    for row in range(rows):
        red_in_row = 0
        for col in range(cols):
            if grid[row, col] == color:
                red_in_row += 1
        if red_in_row > 0 and red_in_row == np.count_nonzero(grid[row,:] != 0):
            return True


    # Check for vertical lines
    for col in range(cols):
        red_in_col = 0
        for row in range(rows):
            if grid[row, col] == color:
                red_in_col +=1
        if red_in_col > 0 and red_in_col == np.count_nonzero(grid[:,col] != 0):
            return True

    return False
            

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Check if a continuous red line exists.
    if check_for_line(input_grid, 2):
        output_grid = np.array([[1]])  # Blue
    else:
        output_grid = np.array([[7]])  # Orange
    return output_grid