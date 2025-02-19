"""
Locates a 1x3 contiguous block of blue (color 1) cells starting at row 0, column 14 in the input grid,
and replaces it with magenta (color 6) cells. All other cells remain unchanged.
"""

import numpy as np

def find_object(grid, color, size, start_row, start_col):
    """
    Finds an object of specified color and size starting at given coordinates.

    Args:
        grid: The input grid.
        color: The color of the object to find.
        size: The size (rows, cols) of the object.
        start_row: starting row
        start_col: starting column
    Returns:
        bool: True if object is found at start coordinates. False Otherwise.
    """
    rows, cols = size
    for r in range(rows):
        for c in range(cols):
            if grid[start_row + r][start_col + c] != color:
                return False
    return True

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)  # Create a copy to avoid modifying the original
    rows, cols = output_grid.shape
    target_color = 6
    target_size = (1, 3)
    start_row = 0
    start_col = 14

    #check if object of size (1,3) exists at given coordinates
    if find_object(input_grid, 1, target_size, start_row, start_col):        
        # Replace the identified region with magenta (color 6)
        for i in range(target_size[1]):
            output_grid[start_row][start_col + i] = target_color
            output_grid[start_row + 1][start_col + i] = target_color # extends the replacement to next row
            

    return output_grid