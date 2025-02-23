"""
Counts the number of red pixels (value '2') in the input grid. If the count is even, the output is a 1x1 grid with a blue pixel (value '1'). If the count is odd, the output is a 1x1 grid with an orange pixel (value '7').
"""

import numpy as np

def transform(input_grid):
    # Count the number of red pixels (value 2).
    red_count = np.count_nonzero(input_grid == 2)

    # Create a 1x1 output grid.
    output_grid = np.zeros((1, 1), dtype=int)

    # Determine the output color based on the parity of the red count.
    if red_count % 2 == 0:
        output_grid[0, 0] = 1  # Blue
    else:
        output_grid[0, 0] = 7  # Orange

    return output_grid