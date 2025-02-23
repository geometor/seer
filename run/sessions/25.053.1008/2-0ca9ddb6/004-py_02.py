"""
1.  **Identify** the locations of all blue (1) and red (2) pixels in the input grid.
2.  **Create** orange (7) pixels adjacent to the identified blue and red pixels. Adjacency includes diagonals. If an orange pixel can be placed adjacent to both a blue and red pixel, perform this fill.
3.  **Extend** yellow (4) cross shapes (one pixel wide extending vertically and horizontally by one unit) from orange(7). For each orange pixel created on step 2, a yellow cross is extended from it, unless:
 * It overlaps with an already existing pixel.
 * It goes beyond the border of the grid.
4.  **Preserve** the azure (8) pixel from the input grid; copy it to the output grid in the same location.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the coordinates of all neighbors of a cell, including diagonals."""
    rows, cols = grid.shape
    neighbors = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):
                neighbors.append((i, j))
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)

    # Find locations of blue (1) and red (2) pixels.
    blue_pixels = np.argwhere(input_grid == 1)
    red_pixels = np.argwhere(input_grid == 2)

    # Create orange (7) pixels adjacent to blue and red pixels.
    orange_candidates = set()
    for r, c in blue_pixels:
        for nr, nc in get_neighbors(input_grid, r, c):
            orange_candidates.add((nr, nc))
    for r, c in red_pixels:
        for nr, nc in get_neighbors(input_grid, r, c):
            orange_candidates.add((nr, nc))

    for r, c in orange_candidates:
      if output_grid[r,c] == 0:
        output_grid[r, c] = 7

    # Create yellow (4) crosses around the orange pixels.
    for r, c in np.argwhere(output_grid == 7):
        for nr, nc in [(r-1,c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < output_grid.shape[0] and 0 <= nc < output_grid.shape[1] and output_grid[nr,nc] == 0:
                output_grid[nr, nc] = 4

    return output_grid