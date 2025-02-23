"""
1. Identify Azure Regions: Find all contiguous regions of azure (8) pixels in the input grid.
2. Iterate Through Regions: For each identified azure region:
    a. Find Occupied Columns: Determine the set of columns that contain at least one pixel from the current region.
    b. Iterate Through Columns: For each column identified in step 2a:
        i. Find Topmost Azure Pixel: Within the current column and current region, find the azure pixel with the smallest row index (the topmost one in that column).
        ii. Change Color: Change the color of this topmost azure pixel to blue (1).
3. Preserve Other Pixels: Ensure all pixels that were not identified as the topmost azure pixel in a column of an azure region retain their original color.
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
        # Find Occupied Columns
        columns = set(pixel[1] for pixel in region)

        # Iterate Through Columns
        for col in columns:
            # Find Topmost Azure Pixel in the current column and region
            pixels_in_column = [pixel for pixel in region if pixel[1] == col]
            if pixels_in_column:  # Check if the list is not empty
               topmost_pixel = min(pixels_in_column, key=lambda x: x[0])
               output_grid[topmost_pixel[0], topmost_pixel[1]] = 1

    return output_grid