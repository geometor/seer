"""
Extracts a 3x3 subgrid from the center of the input grid. Replaces grey pixels within the subgrid with white (0). For each row in the subgrid, if the row contains any blue pixels, the pixel at [row_index, 2 - row_index] in the output grid becomes red (2).
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
    
    # Color Transformation within subgrid
    for i in range(3):
       for j in range(3):
         if subgrid[i,j] == 5:
            output_grid[i,j] = 0 #replace gray with white
          
    
    # Apply Red color rule based on blue pixel presence and diagonal flip
    for i in range(3):
        if 1 in subgrid[i, :]:  # Check the row for blue
            output_grid[i, 2 - i] = 2  # set [i, 2-i] red

    return output_grid