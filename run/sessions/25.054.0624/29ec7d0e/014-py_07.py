"""
1.  **Identify the "removal zone":** This is initially defined as the subgrid bounded by rows 3-8 and columns 3-8, inclusive (using 1-based indexing, corresponding to rows 2-7 and cols 2-7 inclusive, using the zero-based indexing).
2.  **Identify the "seed" pixels**: These are the pixels of color white (0) in the input grid within the "removal zone".
3.  **Expand the removal zone**: Start from the identified "seed" pixels and expand, creating the "removal block" using any color within the removal block.
4.  **Perform Removal:** Any pixel connected to the seed pixel becomes part of the contiguous "removal block".
5.  **Construct Output:** Copy all pixels from the input grid to the output grid *except* those belonging to the removal block. The removal region is a connected component.
"""

import numpy as np

def find_connected_component(grid, start_row, start_col):
    """
    Finds the connected component starting from a given seed pixel using Depth-First Search (DFS).
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    component = []

    def dfs(row, col):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or visited[row, col]
        ):
            return

        visited[row, col] = True
        component.append((row, col))

        # Explore adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc)

    dfs(start_row, start_col)
    return component

def transform(input_grid):
    """
    Transforms the input grid by removing a connected component of pixels.
    """
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify the "removal zone" (rows 3-8, cols 3-8, 1-based indexing)
    removal_zone_start_row = 2  # 0-based indexing
    removal_zone_end_row = 7
    removal_zone_start_col = 2
    removal_zone_end_col = 7

    # 2. Find "seed" pixels (white/0) within the removal zone
    seed_pixels = []
    for r in range(removal_zone_start_row, removal_zone_end_row + 1):
        for c in range(removal_zone_start_col, removal_zone_end_col + 1):
            if input_grid[r, c] == 0:
                seed_pixels.append((r, c))

    # 3. & 4. Expand the removal zone and perform removal (connected component)
    removal_block = set()
    for seed_row, seed_col in seed_pixels:
      if (seed_row, seed_col) not in removal_block:  # important check for not re-expanding
        component = find_connected_component(input_grid, seed_row, seed_col)
        removal_block.update(component)

    # 5. Construct Output (by removing the removal_block)
    for row, col in removal_block:
        # we are just blanking out the output
        # output_grid[row, col] = input_grid[row,col] # default is just to copy
        pass # removal occurs by *not* copying

    return output_grid