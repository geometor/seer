"""
1.  **Identify Green Regions:** Find all contiguous regions of green (color value 3) pixels in the input grid.  A contiguous region is a group of pixels of the same color that are connected horizontally or vertically (not diagonally).

2.  **Identify Inner Green Pixels:** Within each green region, identify "inner" green pixels. A green pixel is considered "inner" if and only if it is directly adjacent (above, below, left, and right) to *four* other green pixels.

3.  **Transform Inner Pixels:** Change the color of all identified "inner" green pixels from green (3) to yellow (4).

4. **Output:** The output is the input grid modified with "inner" green cells changed to yellow.
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

def is_inner_pixel(grid, row, col, color):
    """Checks if a pixel is an inner pixel (surrounded by the same color)."""
    rows, cols = grid.shape
    if grid[row,col] != color:
        return False

    # Check boundaries and adjacent pixels
    if (
        row <= 0
        or row >= rows - 1
        or col <= 0
        or col >= cols - 1
        or grid[row - 1, col] != color
        or grid[row + 1, col] != color
        or grid[row, col - 1] != color
        or grid[row, col + 1] != color
    ):
        return False

    return True

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # identify green regions (this step isn't strictly necessary, but keeps the code organized)
    green_regions = find_contiguous_regions(input_grid, 3)
    
    # identify and paint inner green pixels
    for region in green_regions:
        for r, c in region:
            if is_inner_pixel(input_grid, r, c, 3):
                 output_grid[r,c] = 4
    
    return output_grid