"""
Counts the number of blue (1) cells in the input grid and creates an output grid of size 1xN, where N is the count, filled entirely with blue (1) cells.
"""

import numpy as np

def transform(input_grid):
    # Count the number of cells with value 1 (blue) in the input grid.
    count_of_ones = np.sum(input_grid == 1)

    # Create a new grid with dimensions 1xN, where N is the count of 1s.
    output_grid = np.ones((1, count_of_ones), dtype=int)

    return output_grid