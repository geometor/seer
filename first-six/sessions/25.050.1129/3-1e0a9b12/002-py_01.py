"""
Moves all non-zero colored cells to the bottom row of the grid,
preserving their original column and color.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero cells to the bottom row.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the transformed output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Get the dimensions of the grid.
    rows, cols = output_grid.shape

    # Clear the last row to prepare to move the non-zero cells.
    # The last row will be filled with the input cells with non-zero values.
    output_grid[-1, :] = 0
    
    # Iterate through each column.
    for j in range(cols):
        # Find the non-zero elements in the current column.
        non_zero_elements = []
        for i in range(rows):
           if input_grid[i,j] != 0:
              non_zero_elements.append(input_grid[i,j])
        
        # Move last non-zero values to the last row.
        for i, value in enumerate(non_zero_elements):
           output_grid[rows-len(non_zero_elements)+i, j] = value
           
        #Clear all rows but the last one
        for i in range(rows-len(non_zero_elements)):
           output_grid[i, j] = 0

    return output_grid