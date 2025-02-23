"""
The program detects blue pixels in the input grid, then creates new blue grid with the width equal to number of the blue pixels detected.
"""

import numpy as np

def transform(input_grid):
    # Count the number of blue pixels (value 1) in the input grid.
    blue_count = np.sum(input_grid == 1)

    # Create an output grid with dimensions 1 x blue_count, filled with blue pixels (value 1).
    output_grid = np.ones((1, blue_count), dtype=int)

    return output_grid