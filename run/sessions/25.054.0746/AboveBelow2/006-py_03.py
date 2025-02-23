"""
1.  **Identify Objects:** Find all contiguous regions (objects) of the same color (excluding white/0). An object is any grouping of adjacent pixels, not just rectangles.
2.  **Selective Retention:** Keep only the green (color 3) objects.
3.  **Removal:** Remove all other colored objects, replacing their pixels with the background color (white/0).
4.  **Output:** Create a new grid where only the green objects are present, and everything else is white.
"""

import numpy as np

def find_objects(grid):
    """
    Finds all contiguous objects in the grid.
    Returns a list of (color, [(r, c), ...]) tuples.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, color, object_pixels):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return

        visited[r, c] = True
        object_pixels.append((r, c))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, color, object_pixels)


    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if not visited[r, c] and grid[r, c] != 0:
                color = grid[r, c]
                object_pixels = []
                dfs(r, c, color, object_pixels)
                objects.append((color, object_pixels))
    return objects

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Find all objects
    objects = find_objects(input_grid)

    # Iterate over identified objects and selectively retain/remove
    for color, pixels in objects:
        if color == 3:  # Green
            for r, c in pixels:
                output_grid[r, c] = color

    return output_grid.tolist()