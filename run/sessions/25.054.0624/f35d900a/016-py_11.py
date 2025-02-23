"""
1.  **Initial Placement and Mirroring**: Copy each non-white pixel from the input grid to four corresponding positions in the output grid: the original position, its horizontal mirror, its vertical mirror, and its mirror across both axes. If any mirroring causes an overlap, place the colored pixel value once.
2.  **Color Expansion**: After *all* initial non-white pixels have been placed and mirrored:
    *   Expand red (2) pixels to all directly adjacent (up, down, left, right) white (0) pixels.
    *   Expand yellow (4) pixels to all directly adjacent (up, down, left, right) white (0) pixels.
    *   Expand green(3) pixels to all directly adjacent (up, down, left, right) white(0) pixels.
    *    Expand azure(8) pixels to all directly adjacent (up, down, left, right) white(0) pixels.
3.  **Gray Filling**: After color expansion, for each remaining white (0) pixel in the output grid:
    *   Check if it is directly adjacent (up, down, left, right) to at least two pixels of *different* non-white colors.
    *   If so, replace the white pixel with gray (5).
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """Gets the values of adjacent pixels (up, down, left, right)."""
    rows, cols = grid.shape
    adjacent = []
    if row > 0:
        adjacent.append((row - 1, col))  # Up
    if row < rows - 1:
        adjacent.append((row + 1, col))  # Down
    if col > 0:
        adjacent.append((row, col - 1))  # Left
    if col < cols - 1:
        adjacent.append((row, col + 1))  # Right
    return adjacent

def transform(input_grid):
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # 1. Initial Placement and Mirroring
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] != 0:
                # Place in all four mirrored positions, handling overlaps
                positions = [(i, j), (i, cols - 1 - j), (rows - 1 - i, j), (rows - 1 - i, cols - 1 - j)]
                for r, c in positions:
                    if 0 <= r < rows and 0 <= c < cols:  # boundary check added
                        output_grid[r, c] = input_grid[i, j]

    # 2. Color Expansion
    temp_grid = np.copy(output_grid)  # work on a copy to avoid influencing the expansion
    for i in range(rows):
        for j in range(cols):
            if output_grid[i,j] != 0: # skip expansion is this cell is not colored yet
                continue

            adjacent_coords = get_adjacent_pixels(output_grid, i, j)
            for r, c in adjacent_coords:
                if 0 <= r < rows and 0 <= c < cols: # boundary check
                    adj_val = output_grid[r,c]
                    if adj_val == 2:  # Red
                        temp_grid[i, j] = 2
                    elif adj_val == 4:  # Yellow
                        temp_grid[i, j] = 4
                    elif adj_val == 3: # Green
                        temp_grid[i,j] = 3
                    elif adj_val == 8: # Azure
                        temp_grid[i,j] = 8

    output_grid = np.copy(temp_grid) # update output

    # 3. Gray Filling
    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] == 0:
                adjacent_coords = get_adjacent_pixels(output_grid, i, j)
                adjacent_colors = set()
                for r, c in adjacent_coords:
                     if 0 <= r < rows and 0 <= c < cols: # boundary check
                        adjacent_colors.add(output_grid[r, c])

                adjacent_colors.discard(0)  # Remove white
                if len(adjacent_colors) >= 2:
                    output_grid[i, j] = 5

    return output_grid