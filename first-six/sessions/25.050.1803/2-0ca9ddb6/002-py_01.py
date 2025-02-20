"""
Transforms an input grid into an output grid based on the colors of non-zero cells. 
Red (2) cells cause their diagonal neighbors to become yellow (4).
Blue (1) cells cause their orthogonal neighbors to become orange (7).
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell of the input grid
    for i in range(rows):
        for j in range(cols):
            # Check if the cell's value is non-zero
            if input_grid[i, j] > 0:
                # If the cell is red (2)
                if input_grid[i, j] == 2:
                    # Set diagonal neighbors to yellow (4)
                    for x, y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        if 0 <= i + x < rows and 0 <= j + y < cols:
                            output_grid[i + x, j + y] = 4
                # If the cell is blue (1)
                elif input_grid[i, j] == 1:
                    # Set orthogonal neighbors to orange (7)
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if 0 <= i + x < rows and 0 <= j + y < cols:
                            output_grid[i + x, j + y] = 7

    return output_grid