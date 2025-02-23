"""
Extracts a 3x3 subgrid from the center of the input grid. Replaces gray pixels within the subgrid with white. If any blue pixels exist within the extracted 3x3 subgrid, the center pixel of the output grid becomes red; otherwise, it remains white.
"""

import numpy as np

def transform(input_grid):
    # Get input grid dimensions
    rows, cols = input_grid.shape

    # Calculate the starting row and column for the 3x3 subgrid
    start_row = 0
    start_col = (cols // 2) - 1

    # Extract the 3x3 subgrid
    subgrid = input_grid[start_row:start_row + 3, start_col:start_col + 3]
    
    # Create output grid initialized with white (0)
    output_grid = np.zeros((3, 3), dtype=int)
    
    # Copy and modify subgrid values
    for i in range(3):
      for j in range(3):
        if subgrid[i,j] == 5:
          output_grid[i,j] = 0 #replace gray with white
        else:
          output_grid[i,j] = subgrid[i,j]

    # Check for blue pixels in original subgrid and apply red if found
    if 1 in subgrid:
      output_grid[1,1] = 2 # replace with red
   
    return output_grid