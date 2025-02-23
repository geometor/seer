"""
The transformation identifies and preserves azure (8) pixels that form the boundary of azure shapes in the input grid. Other pixels are set to white (0).
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the valid neighbors of a cell in a grid."""
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
    """
    Transforms the input grid, keeping azure pixels that represent borders and setting others to white.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the input grid
    for row in range(rows):
        for col in range(cols):
            # Check for azure pixels
            if input_grid[row, col] == 8:
                is_border = False
                neighbors = get_neighbors(input_grid, row, col)
                for r, c in neighbors:
                    if input_grid[r,c] != 8:
                      is_border = True
                      break

                if is_border:
                  output_grid[row,col] = 8

    return output_grid.tolist()