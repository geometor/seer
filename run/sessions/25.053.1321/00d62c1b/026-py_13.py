"""
Identifies contiguous green area. In that area, the most "interior" green pixels (i.e. surrounded by green pixels up, down, left, right) is recolored to yellow.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # change output pixels
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if input_grid[r, c] == 3:  # Check if it's green
                # Check neighbors (up, down, left, right)
                if (input_grid[r-1, c] == 3 and
                    input_grid[r+1, c] == 3 and
                    input_grid[r, c-1] == 3 and
                    input_grid[r, c+1] == 3):
                    output_grid[r, c] = 4  # Change to yellow

    return output_grid