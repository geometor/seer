"""
Replaces blue pixels with red pixels if they are in the first two columns of a 3x3 grid.
All other pixels become white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms a 3x3 input grid according to the specified rule.

    Args:
        input_grid: A 3x3 NumPy array representing the input grid.

    Returns:
        A 3x3 NumPy array representing the transformed output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    output_grid[:] = 0

    # Iterate through each cell of the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Check if the current cell is blue (1).
            if input_grid[i, j] == 1:
                # If the cell is blue and in the first or second column, change it to red (2).
                if j <= 1:
                    output_grid[i, j] = 2
                
            # else: # removed the else part
            #    output_grid[i,j] = 0 # since we initialize to 0, we do not need to explicitly set the output grid

    return output_grid