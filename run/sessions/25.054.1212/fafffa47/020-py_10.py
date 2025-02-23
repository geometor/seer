"""
The program transforms a 6x3 input grid into a 3x3 output grid.
It identifies maroon (9) pixels in the input, halves the height, 
and maps these to red (2) pixels in the output. If a 9 is found
in the first of a pair of input rows, a 2 is placed in the
corresponding column of the output. 9s in the second of the pair
are ignored.  All other cells are white (0).
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height = len(input_grid)
    input_width = len(input_grid[0])
    output_height = input_height // 2
    output_width = input_width
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels
    for row_index in range(0, input_height, 2):
        for col_index in range(input_width):
           if input_grid[row_index][col_index] == 9:
              output_grid[row_index//2][col_index] = 2


    return output_grid