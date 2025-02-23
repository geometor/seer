"""
The transformation rule is as follows:
1. Identify the object in the center of the grid.
2. Change the color of the object in the center of the grid from 1(blue) to 2(red).
3. All other cells in the grid remain the same.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape
    
    #Change the color of the object in the center.
    output_grid[rows//2,cols//2] = 2
    
    return output_grid