"""
Transformation rule:
1. Preserve all instances of color 2 (red).
2. For each instance of 1 (blue) that contains an adjacent cell of color 0,
   change the adjacent color 0 to color 2.
3. For each instance of 1 (blue) that contains and adjacent cell of color 2,
    change the instance of 1 to 2.

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
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the grid
    for row in range(rows):
        for col in range(cols):
            if input_grid[row,col] == 1:
                for neighbor_row, neighbor_col in get_neighbors(input_grid, row, col):
                    if input_grid[neighbor_row,neighbor_col] == 0:
                         output_grid[neighbor_row,neighbor_col] = 2

    for row in range(rows):
        for col in range(cols):
            if input_grid[row,col] == 1:
                for neighbor_row, neighbor_col in get_neighbors(input_grid, row, col):
                    if output_grid[neighbor_row,neighbor_col] == 2:
                         output_grid[row,col] = 2

    return output_grid