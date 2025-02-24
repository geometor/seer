"""
Identify the center pixel of a 3x3 grid. Keep its value as 0. Change the value of all other pixels to 8.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms a 3x3 grid by keeping the center pixel value as 0 and changing all other pixels to 8.
    
    Args:
        input_grid: A 3x3 numpy array representing the input grid.
        
    Returns:
        A 3x3 numpy array representing the transformed grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Get the dimensions of the grid
    rows, cols = output_grid.shape

    # Iterate through each cell of the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is the center pixel
            if i == rows // 2 and j == cols // 2:
                # Keep the center pixel as 0
                continue  # Skip to the next iteration
            else:
                # Change all other pixels to 8
                output_grid[i, j] = 8

    return output_grid