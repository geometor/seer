"""
Examine each row in the input grid.
If all pixels in the row are the same non-zero color, change all pixels in that row to gray (5) in the output grid.
Otherwise, change all the pixels in the row to white (0).
Return the changed grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # iterate over each row of the grid
    for row_index, row in enumerate(input_grid):
        # check if all pixels in the row are the same and not zero
        first_pixel = row[0]
        all_same = True
        for pixel in row:
            if pixel != first_pixel or first_pixel == 0:
                all_same = False
                break
        
        # If all pixels are the same non-zero color, change the row to gray (5)
        if all_same:
            output_grid[row_index, :] = 5
        # Otherwise, change the row to white (0).
        else:
            output_grid[row_index, :] = 0
    return output_grid