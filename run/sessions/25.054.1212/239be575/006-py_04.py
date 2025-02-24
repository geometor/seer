"""
The output grid is always 1x1. Count the number of azure pixels in the input grid. If the number of azure pixels is less than 8, the output grid's value is 0 (white). If the number of azure pixels is greater than or equal to 8, the output grid's value is 8 (azure).
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as 1x1 with a default value of 0 (white).
    output_grid = np.zeros((1, 1), dtype=int)

    # Count the number of azure (8) pixels in the input grid.
    azure_count = np.count_nonzero(input_grid == 8)

    # Check if the count of azure pixels is less than 8.
    if azure_count < 8:
        # If the condition is met, set the output grid's value to 0 (white).
        output_grid[0, 0] = 0
    else:
        # Otherwise, set the output grid's value to 8 (azure).
        output_grid[0, 0] = 8

    return output_grid