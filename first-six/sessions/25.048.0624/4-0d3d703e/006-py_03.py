"""
The transformation rule involves subtracting 4 from the color code of the objects in the first and third columns (gray to blue, and magenta to red) and adding 1 to the color code of the object in the middle column (azure to maroon).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by subtracting 4 from the color code of the first and third columns
    and adding 1 to the color code of the second column.
    
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
            # Subtract 4 from the color code of the first and third columns.
            if j == 0 or j == 2:
                output_grid[i, j] = (output_grid[i, j] - 4)
            # Add 1 to the color code of the second column.
            elif j == 1:
                output_grid[i, j] = (output_grid[i, j] + 1)
    
    return output_grid