"""
The output grid is a 7x9 section extracted from the bottom-right part of the input grid,
specifically containing the contiguous block of color 3.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a 7x9 subgrid from the bottom-right corner of the input, where the green color is.
    """
    input_array = np.array(input_grid)
    rows, cols = input_array.shape

    output_rows = 7
    output_cols = 9

    output_grid = input_array[rows-output_rows:, cols-output_cols:]

    return output_grid.tolist()