"""
Identifies regions of color 3 (green) in the input grid and inserts color 6 (magenta)
to the immediate horizontal neighbors (left and right) if the neighbor is not already 3 or 6.
If color 3 is at the edge, add 6 only to available side.
The central magenta region remains unchanged.
"""

import numpy as np

def get_horizontal_neighbors(grid, r, c):
    """Gets the valid horizontal neighbors of a cell."""
    neighbors = []
    rows, cols = grid.shape
    if c > 0:
        neighbors.append((r, c - 1))  # Left neighbor
    if c < cols - 1:
        neighbors.append((r, c + 1))  # Right neighbor
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the grid to find green pixels (3)
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 3:
                neighbors = get_horizontal_neighbors(input_grid, r, c)
                for nr, nc in neighbors:
                    # Check if the neighbor is not green or magenta, then set to magenta
                    if input_grid[nr, nc] != 3 and input_grid[nr,nc] != 6:
                        output_grid[nr, nc] = 6

    return output_grid