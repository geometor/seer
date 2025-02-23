"""
For each row in the input grid, identify the rightmost non-black pixel.
If a non-black pixel is found, change all pixels below that pixel, in the same column, to the color of that rightmost non-black pixel.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()
    
    # iterate through each row
    for row_index, row in enumerate(input_grid):
        # find non-black pixels in the current row
        non_black_pixels = [x for x in row if x != 0]
        
        # check if there are non-black pixels
        if len(non_black_pixels) > 0:
            # get the rightmost non-black pixel's color
            rightmost_color = non_black_pixels[-1]
            
            # find the column index of the rightmost non-black pixel
            for col_index in range(len(row) -1, -1, -1):
                if input_grid[row_index, col_index] == rightmost_color:
                    # change pixels below in the same column
                    output_grid[row_index + 1:, col_index] = rightmost_color
                    break  # Move to the next row after processing

    return output_grid