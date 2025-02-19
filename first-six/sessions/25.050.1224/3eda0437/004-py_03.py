"""
Identifies a contiguous rectangular block of blue (color 1) cells of dimensions 1xN 
(where N can vary) in the input grid, starting at a specific location 
and replaces it with magenta (color 6) cells. All other cells remain unchanged.
The starting row and column, and the width (N) are determined from example sets.
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
    Transforms the input grid according to the rule generalized from examples.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    target_color = 6
    
    # Generalize target size and position based on examples
    # Assuming the target object is always blue (color 1) and starts at column 14 or 15
    # and the width N of object is variable 3 or 4
    
    start_col = -1
    
    for c in range(cols):
        if input_grid[0][c] == 1:
          if input_grid[0][c+1] == 1 and input_grid[0][c+2] == 1:
              start_col = c;
              break;

    
    target_width = 0

    #check width
    for i in range(cols-start_col):
      if input_grid[0][start_col + i] == 1 :
          target_width = target_width + 1
      else:
          break

    start_row = 0
    target_size = (1, target_width)

    #check if object of size (1,target_width) exists at given coordinates.
    if find_object(input_grid, 1, target_size, start_row, start_col):
        # Replace the first row of identified region
        for i in range(target_width):
            output_grid[start_row][start_col + i] = target_color

        #Find next row start
        next_start_row = -1;

        for r in range(rows):
          if input_grid[r][start_col] == 1:
            if next_start_row == -1 or r < next_start_row :
                next_start_row = r

        # Replace the identified region of next row with magenta (color 6)
        for i in range(target_width):
          if next_start_row != -1:
            output_grid[next_start_row][start_col + i] = target_color


    return output_grid