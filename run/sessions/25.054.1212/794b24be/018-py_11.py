"""
1.  Initialization: Create an output grid identical in size to the input grid.
2.  Row Iteration: Process each row of the input grid independently.
3.  Pixel Examination: Within each row, iterate through the pixels from left to right.
4.  Blue Pixel Rule: If a pixel is blue (1), change the corresponding pixel in the output grid to red (2).
5. White Pixel Rule Check: If a pixel is white, look to see if this a blue pixel that has occurred previously in the same row, and if a non-white/non-blue color has not occurred
6. White Pixel Change: If the conditions are met, change to red (2).
7.  Other Pixels: All other pixels remain unchanged in the output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of input grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # iterate through each row
    for r in range(rows):
        blue_found = False  # Flag to indicate if blue has been encountered in the current row
        # iterate though each pixel in row
        for c in range(cols):
            if input_grid[r, c] == 1:  # Blue pixel
                output_grid[r, c] = 2  # change to red
                blue_found = True  # Set flag
            elif input_grid[r,c] == 0 and blue_found:
                output_grid[r,c] = 2
            elif input_grid[r,c] != 0 and input_grid[r,c] != 1:
                blue_found = False

    return output_grid