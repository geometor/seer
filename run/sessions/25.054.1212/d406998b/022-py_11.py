"""
Transforms an input grid by replacing the first gray (5) pixel with a green (3) pixel in every other group of three consecutive gray pixels within each row. Non-gray pixels act as separators between groups.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input
    rows, cols = input_grid.shape

    for r in range(rows):
        gray_count = 0  # Counter for gray pixels in the current row
        replace_group = False  # Flag to indicate whether to replace in the current group
        group_start_col = -1

        for c in range(cols):
            if output_grid[r, c] == 5:  # Check if the pixel is gray
                if group_start_col == -1:
                    group_start_col = c
                gray_count += 1
                if gray_count == 3:
                    if replace_group:
                        output_grid[r,group_start_col] = 3 # replace first in group
                    #reset for next group
                    replace_group = not replace_group
                    gray_count = 0
                    group_start_col = -1
            else: #reset if we hit a non-gray
                gray_count = 0
                replace_group = False
                group_start_col = -1
        #Handle remaining at end of row
        if gray_count >0 and gray_count < 3 and replace_group:
          output_grid[r,group_start_col] = 3
    return output_grid