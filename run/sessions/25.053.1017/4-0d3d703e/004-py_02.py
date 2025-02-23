"""
The transformation rule is to add a constant value to each element of the input grid. 
Specifically, the value 4 is added to elements that map to colors red(2), green(3) and azure(8).
If we add '4' directly, values can be over '9'.
So we are performing modular addition of 4 such that any result greater than 9 is rolled over, starting back at 0.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each element of the grid
    for i in range(rows):
        for j in range(cols):
           # Apply transformation for each element: Modular addition of 4
            output_grid[i, j] = (output_grid[i,j] + 4) % 10

    return output_grid