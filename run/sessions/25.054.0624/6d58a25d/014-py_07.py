"""
1.  **Identify** all pixels.
2.  **Identify** the contiguous yellow (4) shape.
3.  **Locate** the position the yellow shape.
4.  **Replace** the yellow (4) shape with green (3)
5.  **Fill** all of the empty (white, 0) cells with green (3) pixels.
6. Existing Green (3) pixels remain unchanged.
"""

import numpy as np

def find_contiguous_shape(grid, color):
    """Finds the coordinates of a contiguous shape of the given color."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    shape_coords = []

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        shape_coords.append((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        # Include diagonals:
        dfs(r + 1, c + 1)
        dfs(r + 1, c - 1)
        dfs(r - 1, c + 1)
        dfs(r - 1, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                dfs(r, c)
                return shape_coords  # Return after finding the *first* contiguous shape
    return [] # return empty if no shape found


def transform(input_grid):
    # Initialize the output grid as a copy of the input grid
    output_grid = input_grid.copy()
    rows, cols = input_grid.shape

    # Find the coordinates of the contiguous yellow shape
    yellow_shape_coords = find_contiguous_shape(input_grid, 4)

    # Replace the yellow shape with green
    for r, c in yellow_shape_coords:
        output_grid[r, c] = 3

    # Fill all empty cells (white, 0) with green (3), keeping existing greens
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 0:
                output_grid[r, c] = 3

    return output_grid