"""
1.  **Duplicate:** Duplicate the entire input grid vertically to create a 6x4 grid.
2.  **Mirror Top Left:**
    The first row of the duplicated grid is unchanged.
    The values of first column is copied to the last column of the duplicated grid.
3.  **Mirror Bottom Right**
The last row of the duplicated grid is unchanged.
The values of the last column are copied to the first column.

In short, the transformation copies values from the left edge of the input to the right edge of the output, and copies values from the right edge to the left edge.
"""

import numpy as np

def transform(input_grid):
    # Duplicate the input grid vertically
    output_grid = np.concatenate((input_grid, input_grid), axis=0)

    # Get dimensions of the output grid
    rows, cols = output_grid.shape

    # Mirror Top Left to bottom Right: Copy first column to last column
    output_grid[:, cols - 1] = output_grid[:, 0]

     # Mirror Bottom Right to Top Left: Copy last column of input to the first column of output
    output_grid[:,0] = np.concatenate((input_grid[:, -1], input_grid[:, -1]), axis=0)
    
    return output_grid