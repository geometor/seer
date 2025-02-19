"""
The transformation rule is as follows:
1.  Preserve all instances of color 2 (red) and 8 (azure).
2.  For each cell containing color 2, change any adjacent (up, down, left, right) 
    cells with color 0 (white) to color 8 (azure).
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Returns the valid neighbors (up, down, left, right) of a cell."""
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if row < rows - 1:
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col < cols - 1:
        neighbors.append((row, col + 1))  # Right
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)  # Start with a copy of the input
    rows, cols = input_grid.shape

    # Iterate through each cell of the input grid
    for row in range(rows):
        for col in range(cols):
            # If the cell is red (2)
            if input_grid[row, col] == 2:
                # Get the valid neighbors
                for neighbor_row, neighbor_col in get_neighbors(input_grid, row, col):
                    # If the neighbor is white (0), change it to azure (8) in the output grid
                    if input_grid[neighbor_row, neighbor_col] == 0:
                        output_grid[neighbor_row, neighbor_col] = 8

            # all original values are preserved. No need for else.

    return output_grid