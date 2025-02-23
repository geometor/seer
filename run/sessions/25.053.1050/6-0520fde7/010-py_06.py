"""
The transformation rule is as follows:

1. Ignore the Central Column: Disregard the central column of the input grid, which is filled with gray (5) pixels.
2. Identify Blue Regions: Focus on the blue (1) pixels in the remaining parts of the input grid.
3. Translate and Replace: Create a new 3x3 grid. Map the blue pixels from the relevant part of the input grid to the new grid, changing their color to red (2). All other pixels in the output grid should be white (0).
"""

import numpy as np

def get_non_central_columns(input_grid):
    """
    Extracts columns of the input_grid that are to the left and right of the central grey column.
    """
    height, width = input_grid.shape
    center_col_index = width // 2

    left_cols = []
    right_cols = []
    
    for x in range(width):
        if x == center_col_index:
            continue
        
        if input_grid[0, x] != 5 and input_grid[1, x] !=5 and input_grid[2, x] != 5:

            column = []
            for y in range(height):
                column.append(input_grid[y,x])

            if x < center_col_index:
              left_cols.append((x,column))
            else:
              right_cols.append((x-center_col_index-1,column)) # correct index after removing central column

    return left_cols, right_cols

def transform(input_grid):
    """
    Transforms an input grid into an output grid according to the specified rules.
    """

    # Initialize output_grid as 3x3, filled with white (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Get non-central columns
    left_cols, right_cols = get_non_central_columns(input_grid)

    # all columns
    all_cols = left_cols + right_cols
    
    # Fill in the output
    for x, col in all_cols:
      for y, pixel in enumerate(col):
        if pixel == 1: # if blue pixel
          output_grid[y,x] = 2 # place a red
        
    return output_grid