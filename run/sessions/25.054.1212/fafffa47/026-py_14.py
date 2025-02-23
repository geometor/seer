"""
The transformation extracts the top half of the input grid (first three rows). 
Then, it translates the cells: if a cell in the top half is maroon (9), 
it becomes red (2) in the output grid. 
All other cells in the output grid are white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a 3x3 array filled with white (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through the top half of the input grid.
    for i in range(3):
        for j in range(3):
            # Check if the current cell in the input grid is maroon (9).
            if input_grid[i][j] == 9:
                # If it's maroon, set the corresponding cell in the output grid to red (2).
                output_grid[i][j] = 2
            # Otherwise it will remain the initialized value of 0
    return output_grid