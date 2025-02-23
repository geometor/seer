"""
1.  **Identify Initial Shape:** Locate all pixels with the color green (value 3) in the input grid. These pixels define the initial shape.

2.  **Identify Inside Pixels:** Define "inside pixels" as any non-green pixels that are completely surrounded by the initial green shape. *Completely Surrounded* means that any path from this pixel to the outside edge of the grid must cross a green pixel.

3.  **Fill Inside Pixels:** Change the color of all identified "inside pixels" to yellow (value 4).

4.  **Output:** Return the modified grid. The output grid should have the same dimensions as the input grid. Only the "inside pixels" should have changed from their original color to yellow. All other pixels, including the initial green shape and any pixels outside the shape, should remain their original colors.
"""

import numpy as np
from collections import deque

def get_neighbors(grid, row, col):
    """Gets the valid neighbors of a cell in the grid."""
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # North
    if row < rows - 1:
        neighbors.append((row + 1, col))  # South
    if col > 0:
        neighbors.append((row, col - 1))  # West
    if col < cols - 1:
        neighbors.append((row, col + 1))  # East
    return neighbors

def is_inside(grid, r, c, green_pixels):
    """
    Checks if a pixel is inside the shape defined by green_pixels using a flood-fill approach.
    """
    rows, cols = grid.shape
    if (r, c) in green_pixels:
        return False  # Green pixels are not inside

    visited = set()
    queue = deque([(r, c)])
    visited.add((r,c))

    while queue:
        curr_r, curr_c = queue.popleft()

        # Check if we've reached the edge of the grid
        if curr_r == 0 or curr_r == rows - 1 or curr_c == 0 or curr_c == cols - 1:
            return False  # Reached the edge, so it's not inside

        neighbors = get_neighbors(grid, curr_r, curr_c)
        for nr, nc in neighbors:
            if (nr, nc) not in visited:
                if (nr, nc) not in green_pixels:
                  visited.add((nr,nc))
                  queue.append((nr, nc))
    return True # if the while loop completes, it means the pixel is inside

def transform(input_grid):
    # initialize output_grid as a copy of the input
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify the initial shape (green pixels)
    green_pixels = set()
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 3:
                green_pixels.add((r, c))

    # Identify and fill inside pixels
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in green_pixels:
                if is_inside(input_grid, r, c, green_pixels):
                    output_grid[r, c] = 4

    return output_grid