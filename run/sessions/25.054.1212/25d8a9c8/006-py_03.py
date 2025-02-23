"""
The transformation rule performs a color replacement based on the following mapping:

1.  Yellow (4) in the input becomes gray (5) in the output.
2.  Red (2) in the input becomes white (0) in the output.
3.  Green (3) in the input becomes white (0) in the output.
4.  Orange (7) in the input becomes white(0) in the output.
5.  Gray (6) becomes Gray (5).
6.  Maroon (9) becomes Gray(5).
7.  Blue(1) remains Blue(1).
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply the color transformation rules.
            if input_grid[i, j] == 4:   # Yellow becomes gray
                output_grid[i, j] = 5
            elif input_grid[i, j] == 2: # Red becomes white
                output_grid[i, j] = 0
            elif input_grid[i, j] == 3: # Green becomes white
                output_grid[i, j] = 0
            elif input_grid[i, j] == 7: # Orange becomes white
                output_grid[i, j] = 0
            elif input_grid[i, j] == 6: # Gray becomes gray
                output_grid[i, j] = 5
            elif input_grid[i, j] == 9: # Maroon becomes gray
                output_grid[i, j] = 5
            elif input_grid[i, j] == 1: # Blue remains blue
                output_grid[i,j] = 1

    return output_grid