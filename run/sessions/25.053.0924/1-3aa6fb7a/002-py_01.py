"""
Identifies azure pixels (value 8) in the input grid and changes adjacent white pixels (value 0) to blue pixels (value 1).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing white pixels (0) adjacent to azure pixels (8) to blue (1).
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of input_grid
    rows, cols = input_grid.shape

    # Iterate through each cell of the input_grid
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8:  # Check if the current cell is azure (8)
                # Check to the immediate right
                if c + 1 < cols and input_grid[r, c + 1] == 0:
                    output_grid[r, c + 1] = 1  # Change adjacent white pixel to blue
                # Check to the immedate left
                if c - 1 >= 0 and input_grid[r, c-1] == 0:
                    output_grid[r, c-1] = 1

    return output_grid