"""
The transformation rule involves subtracting 1 from the color code of the objects in the first and second columns (maroon to azure, and yellow to green) and adding 4 to the color code of the object in the third column (red to magenta).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by subtracting 1 from the color code of the first and second columns
    and adding 4 to the color code of the third column.
    
    Args:
        input_grid (numpy.ndarray): The input grid.
    
    Returns:
        numpy.ndarray: The transformed output grid.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)
    
    # Iterate through each cell in the grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Subtract 1 from the color code of the first and second columns.
            if j == 0 or j == 1:
                output_grid[i, j] = (output_grid[i, j] - 1)
            # Add 4 to the color code of the third column.
            elif j == 2:
                output_grid[i, j] = (output_grid[i, j] + 4)
    
    return output_grid