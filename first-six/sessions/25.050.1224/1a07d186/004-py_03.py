"""
The transformation rule is as follows:
1. Two vertical lines, one green (color 3) in column 4 and one yellow (color 4) in column 13, remain unchanged.
2. Every other color, different from 3 and 4 will:
    *   Be deleted if they exist.
    *   If they are green or yellow, two copies of them must be made next to the green and yellow columns respectively, to the right of the green column and to the left of the yellow one.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)

    # Find the green and yellow lines
    green_line_col = 4
    yellow_line_col = 13
   
    # Iterate the input
    for r in range(input_grid.shape[0]):
      for c in range(input_grid.shape[1]):
        # Keep green and yellow columns
        if c == green_line_col and input_grid[r,c] == 3:
           output_grid[r,c] = 3          
        elif c == yellow_line_col and input_grid[r,c] == 4:
           output_grid[r,c] = 4   
        # Move other single cells       
        elif input_grid[r,c] == 3 and c != green_line_col:
          output_grid[r,c] = 0
          output_grid[r, green_line_col + 1] = 3
        elif input_grid[r,c] == 4 and c!= yellow_line_col:
          output_grid[r,c] = 0
          output_grid[r, yellow_line_col - 1] = 4
        elif input_grid[r,c] != 3 and input_grid[r,c] != 4:
          output_grid[r,c] = 0

    return output_grid