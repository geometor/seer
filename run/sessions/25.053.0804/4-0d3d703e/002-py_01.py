"""
The transformation rule involves adding to each cell a number. The number to be added depends on the original number on the cell. Add 1 to cells with 3, 4 to cells with 1 and cells with 2. The spatial arrangement of pixels remains constant; only their values are modified based on the described mapping.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Apply the transformation: Add 1 to cells that are 3(green).
    output_grid[input_grid == 3] += 1
    # Apply the transformation: Add 4 to cells that are 1(blue).
    output_grid[input_grid == 1] += 4
    # Apply the transformation: Add 4 to cells that are 2(red).
    output_grid[input_grid == 2] += 4

    return output_grid