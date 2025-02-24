"""
The output grid is always 1x1. If the number of azure pixels in the input grid
is greater than or equal to 7, the output grid's value is 8 (azure). Otherwise,
the output grid's value is 0 (white).
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as 1x1 with a default value of 0 (white).
    output_grid = np.zeros((1, 1), dtype=int)

    # Count the number of azure (8) pixels in the input grid.
    azure_count = np.count_nonzero(input_grid == 8)

    # Check if the count of azure pixels is greater than or equal to 7.
    if azure_count >= 7:
        # If the condition is met, set the output grid's value to 8 (azure).
        output_grid[0, 0] = 8

    return output_grid