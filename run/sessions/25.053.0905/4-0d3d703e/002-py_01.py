"""
For each number in the input grid, add a value that is specific to the original value of that number. Specifically, add 1 to all cells of value 3; add 4 to all cells with the original value 1; add 4 to all cells with the original value 2.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Define the transformation rules based on the original values
    # Add 1 to cells with the original value of 3
    output_grid[input_grid == 3] = input_grid[input_grid == 3] + 1
    # Add 4 to cells with original value of 1
    output_grid[input_grid == 1] = input_grid[input_grid == 1] + 4
    # Add 4 to cells with original value of 2
    output_grid[input_grid == 2] = input_grid[input_grid == 2] + 4
    
    return output_grid