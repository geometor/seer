# 00d62c1b • 024 • refine_coder

---
```python
"""
1.  **Identify Green Regions:** Find all contiguous regions of green (color value 3) pixels in the input grid.  A contiguous region is a group of pixels of the same color that are connected horizontally or vertically (not diagonally).  Use a depth-first search (DFS) algorithm to achieve this.

2.  **Identify Inner Pixels within Each Region:** For *each* identified green region, iterate through its pixels. A green pixel is considered "inner" if and only if it is part of the green region *and* is directly adjacent (above, below, left, and right) to four other green pixels *that are also part of the same region*.

3.  **Transform Inner Pixels:** Change the color of all identified "inner" green pixels from green (3) to yellow (4).

4.  **Output:** The output is the input grid, modified with "inner" green pixels changed to yellow. The dimensions of the output grid are identical to the input grid.
"""

import numpy as np

def find_contiguous_regions(grid, color):
    """Finds contiguous regions of a specific color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def dfs(row, col):
        """Depth-first search to explore a contiguous region."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return []

        visited[row, col] = True
        region = [(row, col)]

        region.extend(dfs(row + 1, col))
        region.extend(dfs(row - 1, col))
        region.extend(dfs(row, col + 1))
        region.extend(dfs(row, col - 1))
        return region

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] == color:
                regions.append(dfs(row, col))

    return regions

def is_inner_pixel(region, row, col):
    """Checks if a pixel is an inner pixel within a region."""
    # Check if the given (row, col) is surrounded by other pixels *within the region*.
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for r, c in neighbors:
        if (r, c) not in region:
            return False  # Not an inner pixel
    return True


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # identify green regions
    green_regions = find_contiguous_regions(input_grid, 3)

    # identify and transform inner green pixels *within each region*
    for region in green_regions:
        for r, c in region:
            if is_inner_pixel(region, r, c):
                output_grid[r, c] = 4

    return output_grid
```
