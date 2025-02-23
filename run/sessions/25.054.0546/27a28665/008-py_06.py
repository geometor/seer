"""
Count the azure pixels at the corners of the input grid. This count is the output number, represented as a 1x1 red grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by counting azure pixels at the corners and returning the count as a 1x1 red grid.
    """
    # Initialize count
    count = 0

    # Get grid dimensions
    rows, cols = input_grid.shape

    # Check corners for azure (8)
    if input_grid[0, 0] == 8:
        count += 1
    if input_grid[0, cols - 1] == 8:
        count += 1
    if input_grid[rows - 1, 0] == 8:
        count += 1
    if input_grid[rows - 1, cols - 1] == 8:
        count += 1

    # Create output grid (1x1 with the count as a red pixel)
    output_grid = np.array([[count]])
    
    # convert to red
    output_grid[:] = 2


    return output_grid