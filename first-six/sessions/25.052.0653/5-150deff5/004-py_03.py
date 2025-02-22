"""
1. **Identify and Replace Gray:** Find all gray (5) pixels in the input grid. Replace them with azure (8) pixels.

2. **Identify Interior Red Pixels:** Within the newly created azure (8) regions, identify pixels that should be red (2) based on the following condition: A pixel should be colored red if all the cells from its 4-neighbors have color 8 or 2.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """ Return 4 neighbors of the cell in grid"""

    rows, cols = grid.shape
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if r < rows - 1:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""

    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # 1. Replace gray (5) with azure (8)
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 5:
                output_grid[r, c] = 8

    # 2. Identify and color interior red pixels
    output_grid_before = np.copy(output_grid) # Create copy before changing to red.
    for r in range(rows):
        for c in range(cols):
            if output_grid_before[r, c] == 8:
                neighbors = get_neighbors(output_grid_before, r, c)
                neighbor_colors = [output_grid_before[nr, nc] for nr, nc in neighbors]
                # Check neighbors. Color this to 2 if all valid neighbors are 8 or 2.
                if all(color == 8 or color == 2 for color in neighbor_colors) and len(neighbors) == 4:
                    output_grid[r,c] = 2

    return output_grid