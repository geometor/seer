"""
1.  **Identify Green Regions:** Find all contiguous regions of green (color value 3) pixels in the input grid.  Pixels are contiguous if they are connected horizontally, vertically, *or diagonally*.

2.  **Determine Boundaries:** For each green region, identify its boundary pixels. A pixel is part of the boundary if *any* of its eight neighbors (horizontal, vertical, and diagonal) is:
    *   A pixel of a different color.
    *   Outside the bounds of the input grid.

3.  **Change Inner Pixels to Yellow:** Iterate through all pixels within each green region.
    *   If a pixel is green and *not* a boundary pixel (i.e., it's an "inner" pixel), change its color to yellow (color value 4).
    *   If a pixel is green *and* is a boundary pixel, its color remains unchanged.

4.  **Preserve Other Colors:** All pixels that are not part of a green region in the input grid should remain unchanged in the output grid.

5.  **Output:** The output is the modified grid.
"""

import numpy as np

def find_contiguous_regions(grid, color):
    """Finds contiguous regions of a given color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def is_valid(x, y):
        """Checks if a coordinate is within the grid bounds."""
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_region):
        """Performs Depth-First Search to find contiguous pixels."""
        if not is_valid(x, y) or visited[x, y] or grid[x, y] != color:
            return

        visited[x, y] = True
        current_region.append((x, y))

        # Explore adjacent pixels (up, down, left, right, and diagonals)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                dfs(x + dx, y + dy, current_region)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and not visited[x, y]:
                current_region = []
                dfs(x, y, current_region)
                regions.append(current_region)
    return regions

def is_boundary(grid, x, y, region):
    """Checks if a pixel is on the boundary of its region (including diagonals)."""
    rows, cols = grid.shape
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if not (0 <= nx < rows and 0 <= ny < cols):
                return True  # Adjacent to grid boundary
            if (nx, ny) not in region:
                return True  # Adjacent to a pixel outside the region
    return False

def transform(input_grid):
    # Initialize output_grid
    output_grid = input_grid.copy()

    # Find green regions
    green_regions = find_contiguous_regions(input_grid, 3)

    # Iterate through each green region and change inner green pixels to yellow
    for region in green_regions:
        for x, y in region:
            if not is_boundary(output_grid, x, y, region):
                output_grid[x, y] = 4

    return output_grid