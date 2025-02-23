"""
The transformation reverses the order of columns, expands to left with repeats of the input row, and fills the remaining space with 0.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_grid = np.zeros((input_height * 2, input_width), dtype=int)

    # Reverse Column Order and Column-wise Transformation
    for i in range(input_width):
        # reversed column index
        rev_col_index = input_width - 1 - i
        
        # copy input column into the expanded output grid
        for row in range(input_height):
            output_grid[row, rev_col_index] = input_grid[row, i]
            for j in range(input_height*2):
                # find left-most non zero column
                left_most_non_zero = 0
                for col_to_fill in range(input_width):
                    if output_grid[row,col_to_fill] != 0:
                        left_most_non_zero = col_to_fill
                        break

                if j >= row and j < input_height*2 and rev_col_index < input_width:
                  output_grid[j,left_most_non_zero] = input_grid[row,i]


    return output_grid