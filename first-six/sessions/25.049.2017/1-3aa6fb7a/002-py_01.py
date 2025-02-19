"""
Locate all of `8` colored pixels that forms a group (at least 2). For each group, find the pixel that have another pixel in the group adjacent to it. For all this cases, change color `8` by color `1`. Keep the rest of the grid equal.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """
    Returns a list of valid neighbor coordinates for a given cell.
    """
    rows, cols = grid.shape
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Change the color of '8' cells to '1' if they are part of an '8' cluster and next to others '8'.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid to find the position of '8'
    for r in range(rows):
        for c in range(cols):
           if output_grid[r,c]== 8:
                neighbors = get_neighbors(output_grid,r,c)
                for nr,nc in neighbors:
                    if output_grid[nr,nc]==8:
                        output_grid[r,c] = 1
                        break

    return output_grid