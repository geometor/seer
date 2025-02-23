"""
Extracts a 3x3 subgrid from the center of the input grid. Replaces grey pixels within the subgrid with white (0). For each row in the subgrid, if the row contains any blue pixels, the corresponding pixel in the center column of the output grid becomes red (2); otherwise, it remains white(0).
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
   
    # Color Transformation within Subgrid:
    for i in range(3):
       for j in range(3):
         if subgrid[i,j] == 5:
           output_grid[i,j] = 0 # Replace gray

    # Apply the Red color rule based on Blue pixel presence in each row
    for i in range(3):
        if 1 in subgrid[i,:]:  # Check for blue in the current row
            output_grid[i, 1] = 2  # Set the center column pixel to red

    return output_grid