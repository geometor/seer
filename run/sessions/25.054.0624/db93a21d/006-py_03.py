"""
1.  **Preserve Maroon:** Copy all maroon (9) pixels from the input grid to the output grid.

2.  **Green Outline:**
    *   Create a green (3) outline around any maroon (9) pixels, changing all adjacent (up, down, left, right) white (0) pixels to green.
    *   Create a green (3) outline on all edges of the grid, by changing any white (0) pixels that are on the border of the grid to green.

3.  **Fill Enclosed Regions:**
    *   Identify regions of contiguous white (0) pixels.
    *   For each region, determine if any pixel in the region touches the edge of the grid.
    *   If a region *does not* touch the edge, fill the entire region with blue (1) pixels.
    *   If it does touch the edge, leave as white (0).
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the valid neighbors of a cell (up, down, left, right)."""
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

def flood_fill(grid, row, col, target_color, replacement_color):
    """Performs a flood fill, but only if the region is not connected to the edge."""
    rows, cols = grid.shape
    if grid[row, col] != target_color:
        return
    
    stack = [(row, col)]
    seen = set()
    edge_connected = False

    while stack:
        r, c = stack.pop()

        if (r,c) in seen:
            continue
        seen.add((r,c))

        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            edge_connected = True

        for nr, nc in get_neighbors(grid, r, c):
            if grid[nr,nc] == target_color:
                stack.append((nr,nc))

    if not edge_connected:
        for r,c in seen:
            grid[r,c] = replacement_color
        

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Preserve Maroon - copy
    # Green Outline (including edge)
    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 9:  #Maroon
                for r, c in get_neighbors(input_grid, row, col):
                    if input_grid[r,c] == 0:
                        output_grid[r,c] = 3
            elif input_grid[row,col] == 0:
                is_edge = row == 0 or row == rows -1 or col == 0 or col == cols - 1
                if is_edge:
                    output_grid[row,col] = 3

    # Flood fill for blue objects - constrained to non-edge-connected regions
    for row in range(rows):
        for col in range(cols):
            if output_grid[row,col] == 0:
                flood_fill(output_grid, row, col, 0, 1)


    return output_grid