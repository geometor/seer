"""
1. Count the number of blue pixels (cells with value 1) in the input grid.
2. Create a new grid with a height of 1 and a width equal to the count of blue pixels from the input grid.
3. Fill all cells of the output grid with the value 1 (blue).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by counting the blue pixels (1s) and creating a 
    new grid representing that count.
    """
    # Count the number of blue pixels (1s) in the input grid.
    count_of_ones = np.count_nonzero(input_grid == 1)

    # Create a new grid with a height of 1 and a width equal to the count.
    output_grid = np.ones((1, count_of_ones), dtype=int)

    return output_grid