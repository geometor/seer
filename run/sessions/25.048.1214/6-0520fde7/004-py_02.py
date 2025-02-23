"""
The transformation extracts a 3x3 subgrid centered on the middle gray object of the original grid. Those cells that were blue (1) in the original grid will be colored red (2), other than that all the cells are colored white (0).
"""

import numpy as np

def find_gray_column(grid):
    # Find the column index where all elements are gray (5)
    for j in range(grid.shape[1]):
        if np.all(grid[:, j] == 5):
            return j
    return -1  # Return -1 if no such column is found

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    input_grid = np.array(input_grid)
    
    # Find the column index with all gray objects
    gray_column_index = find_gray_column(input_grid)
    
    # Initialize the output grid as all white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    #If there is not a gray column, return all zeros
    if gray_column_index == -1:
        return output_grid

    # Define center of the 3x3 subgrid
    center_row = 1
    center_col = gray_column_index

    # Extract the 3x3 subgrid from the input grid
    subgrid = input_grid[0:3, gray_column_index - 1:gray_column_index + 2]

    # Iterate over the subgrid and update output_grid
    for i in range(3):
        for j in range(3):
            if subgrid[i, j] == 1:  # If the cell in the subgrid is blue
                output_grid[i, j] = 2  # Set corresponding cell in output to red
            
    return output_grid