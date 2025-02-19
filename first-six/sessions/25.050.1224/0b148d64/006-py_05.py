"""
The output grid is a 9x6 section extracted from the input grid,
specifically containing the contiguous block of color 4 and rows of 0s below.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a 9x6 subgrid from the input.
    """
    input_array = np.array(input_grid)
    rows, cols = input_array.shape
    
    # Find the first row containing color 4.
    first_row_with_4 = -1
    for i in range(rows):
        if 4 in input_array[i]:
            first_row_with_4 = i
            break

    output_rows = 9
    output_cols = 6

    output_grid = input_array[first_row_with_4:first_row_with_4 + output_rows, :output_cols]
    
    return output_grid.tolist()
