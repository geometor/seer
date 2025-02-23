"""
The transformation rule is to create an alternating pattern of green and maroon. The first cell is green. Adjacent cells (horizontal and vertical) can not have same color.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # change output pixels
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                output_grid[i, j] = 3  # Green
            else:
                output_grid[i, j] = 9  # Maroon

    return output_grid