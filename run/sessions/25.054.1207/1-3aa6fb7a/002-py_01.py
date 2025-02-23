"""
1. Identify Azure Regions: Locate all contiguous regions of azure (8) pixels in the input grid.
2. Identify Topmost Pixels: Within each azure region, find the azure pixel with the smallest row index (topmost).
3. Change Color: Change the color of the identified topmost azure pixel to blue (1).
4. Preserve Other Pixels: All other pixels remain unchanged.
"""

import numpy as np

def find_contiguous_regions(grid, color):
    """Finds contiguous regions of a specific color in a grid."""
    visited = set()
    regions = []

    def dfs(row, col, current_region):
        """Depth-first search to explore contiguous regions."""
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_region.append((row, col))
        # Check adjacent cells (up, down, left, right)
        dfs(row + 1, col, current_region)
        dfs(row - 1, col, current_region)
        dfs(row, col + 1, current_region)
        dfs(row, col - 1, current_region)


    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_region = []
                dfs(row, col, current_region)
                regions.append(current_region)
    return regions

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    azure_regions = find_contiguous_regions(output_grid, 8)

    for region in azure_regions:
        # Find the topmost pixel (smallest row index)
        topmost_pixel = min(region, key=lambda x: x[0])
        output_grid[topmost_pixel[0], topmost_pixel[1]] = 1

    return output_grid