"""
1.  **Initialization:** Create an output grid that is twice the dimensions of the input grid (2x width, 2x height).
2.  **Replication:** For each pixel in the input grid:
    *   Copy the pixel's value.
    *   Create a 2x2 block in the output grid, starting at the position (2 \* row, 2 \* column) where row and column are the coordinates of the current input pixel.
    *  Fill all four cells of this 2x2 block with the copied pixel value.
3. **Padding**: Fill the remaining cells (those not part of any 2x2 replication) of output grid with 0.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height, output_width = 2 * input_height, 2* input_width
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels
    for row in range(input_height):
        for col in range(input_width):
            # replication
            pixel_value = input_grid[row, col]
            output_grid[2*row:2*row+2, 2*col:2*col+2] = pixel_value

    return output_grid