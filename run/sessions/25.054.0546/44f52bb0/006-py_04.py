"""
Counts the number of red pixels in the input grid. If the count is even, the output is a 1x1 blue grid; if odd, the output is a 1x1 orange grid.
"""

import numpy as np

def transform(input_grid):
    # Count the number of red pixels (value 2)
    red_count = np.sum(input_grid == 2)

    # Create a 1x1 output grid
    output_grid = np.zeros((1, 1), dtype=int)

    # If the count is even, set output to blue (1); otherwise, set to orange (7)
    if red_count % 2 == 0:
        output_grid[0, 0] = 1
    else:
        output_grid[0, 0] = 7

    return output_grid