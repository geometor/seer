"""
1.  **Identify the Main Shape:** Find the largest contiguous block of pixels of a single color (`shape_1` and its color `color_1`).

2.  **Identify Neighboring Colors:** Find all colors directly adjacent (up, down, left, right, or diagonal) to `shape_1`. These are the `shape_2` colors.

3.  **Conditional Fill:** Iterate through the white (0) pixels *within* `shape_1`'s bounding box (or the whole grid). If a white pixel is adjacent to *both* a pixel of `color_1` and *any* of the `shape_2` colors, change the white pixel's color to `color_1`.
"""

import numpy as np
from collections import Counter

def find_largest_object(grid):
    """Finds the largest contiguous block of pixels and its color."""
    visited = set()
    max_size = 0
    shape_color = -1

    def dfs(r, c, color, count):
        if (r, c) in visited or not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != color:
            return count
        visited.add((r, c))
        count += 1
        count = dfs(r + 1, c, color, count)
        count = dfs(r - 1, c, color, count)
        count = dfs(r, c + 1, color, count)
        count = dfs(r, c - 1, color, count)
        count = dfs(r + 1, c + 1, color, count)
        count = dfs(r - 1, c - 1, color, count)
        count = dfs(r + 1, c - 1, color, count)
        count = dfs(r - 1, c + 1, color, count)
        return count

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited:
                color = grid[r][c]
                size = dfs(r, c, color, 0)
                if size > max_size:
                    max_size = size
                    shape_color = color
    return shape_color

def get_adjacent_pixels(grid, coord):
    """Returns adjacent pixels, including diagonals."""
    r, c = coord
    adjacent = []
    for i in range(max(0, r - 1), min(len(grid), r + 2)):
        for j in range(max(0, c - 1), min(len(grid[0]), c + 2)):
            if (i, j) != (r, c):
                adjacent.append((i, j))
    return adjacent

def find_object_coords(grid, color):
    """Find coordinates of objects with the given color."""
    coords = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == color:
                coords.append((r, c))
    return coords


def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    color_1 = find_largest_object(input_grid)
    shape_1_coords = find_object_coords(input_grid, color_1)

    # Find shape_2 colors (adjacent to shape_1)
    shape_2_colors = set()
    for r, c in shape_1_coords:
        for ar, ac in get_adjacent_pixels(input_grid, (r, c)):
            if input_grid[ar, ac] != color_1 and input_grid[ar,ac] != 0:
                shape_2_colors.add(input_grid[ar, ac])
    
    if not shape_2_colors:
        return output_grid

    # Iterate through white pixels and apply the fill rule
    white_coords = find_object_coords(input_grid, 0)
    for wr, wc in white_coords:
        adjacent_to_shape_1 = False
        adjacent_to_shape_2 = False

        for ar, ac in get_adjacent_pixels(input_grid, (wr, wc)):
            if input_grid[ar, ac] == color_1:
                adjacent_to_shape_1 = True
            if input_grid[ar, ac] in shape_2_colors:
                adjacent_to_shape_2 = True

        if adjacent_to_shape_1 and adjacent_to_shape_2:
            output_grid[wr, wc] = color_1

    return output_grid