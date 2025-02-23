"""
1.  **Copy Existing Pixels:** All pixels that are not black (color 0) in the input grid are copied to the same position in the output grid.
2.  **Add Yellow Pixels:** For every non-black pixel in the input grid, add two yellow pixels in the output grid. The yellow pixels' positions depend on the position of original color pixels. One of these is placed two rows above, in the same column. The second is two rows above, and two columns to the right. If those spaces don't exist(out of grid bounds, or occupied), skip adding those yellow pixels.
3. **Add Orange Pixels around Blue:** Add orange pixels around any blue pixel that existed in the *input* grid, but only in the direct adjacent positions(up, down, left and right). If any of these positions are occupied or out of grid bound, skip addition.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Returns the valid neighbor coordinates (up, down, left, right) of a cell.
    """
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
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    rows, cols = input_grid.shape

    # change output pixels
    # 1. Copy Existing Pixels
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                output_grid[r, c] = input_grid[r, c]

    # 2. Add Yellow Pixels
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                # Position 1: Two rows above, same column
                new_r1 = r - 2
                new_c1 = c
                if 0 <= new_r1 < rows and output_grid[new_r1, new_c1] == 0:
                    output_grid[new_r1, new_c1] = 4  # Yellow

                # Position 2: Two rows above, two columns right
                new_r2 = r - 2
                new_c2 = c + 2
                if 0 <= new_r2 < rows and 0 <= new_c2 < cols and output_grid[new_r2, new_c2] == 0:
                    output_grid[new_r2, new_c2] = 4  # Yellow

    # 3. Add Orange Pixels around Blue
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 1:  # Blue
                for nr, nc in get_neighbors(input_grid, r, c):
                    if output_grid[nr, nc] == 0:
                        output_grid[nr, nc] = 7  # Orange

    return output_grid