"""
The transformation identifies regions of magenta (6) and green (3) pixels. It preserves the magenta pixels in the top three rows and the green pixels, while changing all other magenta pixels to white (0).
"""

import numpy as np

def find_contiguous_regions(grid, color):
    """Finds contiguous regions of the specified color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def dfs(row, col, region):
        """Depth-First Search to explore a contiguous region."""
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        region.append((row, col))
        dfs(row + 1, col, region)
        dfs(row - 1, col, region)
        dfs(row, col + 1, region)
        dfs(row, col - 1, region)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                region = []
                dfs(row, col, region)
                regions.append(region)
    return regions

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    magenta_regions = find_contiguous_regions(input_grid, 6)
    green_regions = find_contiguous_regions(input_grid, 3)

    # Preserve top magenta and erase the rest
    for region in magenta_regions:
        for row, col in region:
            if row > 2:  # Not in the top three rows
                output_grid[row, col] = 0

    return output_grid