"""
The transformation rule is as follows:
1. Identify the vertical line of color 5 in the input grid.
2. Create a 3x3 output grid filled with color 0.
3. Change the color of the central cell of the identified vertical line of 5 from 5 to 2 and place it in the center of the output grid.
4. All other cells in the output grid remain color 0.
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find contiguous vertical lines of the specified color
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows - 1):
            if grid[r, c] == color and grid[r+1, c] == color:
                if r + 2 < rows and grid[r+2,c] ==color:
                    return (r+1,c)  #return center of the vertical line
    return None

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Convert input grid to numpy array
    input_grid = np.array(input_grid)

    # Find the central cell of the vertical line of color 5
    center_cell = find_vertical_line(input_grid, 5)

    # Initialize the output grid as a 3x3 array filled with 0s
    output_grid = np.zeros((3, 3), dtype=int)

    # If a vertical line of color 5 is found, change the center cell to 2
    if center_cell:
        center_row = 1
        center_col = 1
        output_grid[center_row, center_col] = 2

    return output_grid