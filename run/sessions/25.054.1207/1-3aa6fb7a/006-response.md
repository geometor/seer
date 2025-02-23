# 1-3aa6fb7a • 006 • refine_coder

---
```python
"""
1. Identify Contiguous Regions: Find all distinct, contiguous regions of azure (8) pixels in the input grid. Two pixels are considered part of the same region if they are adjacent (up, down, left, or right) and have the same color.

2. Process Each Region Independently: For *each* identified azure region:

    a. Determine Occupied Columns: Find the set of columns that contain at least one pixel from *this specific* region.

    b. Find Topmost Azure Pixel *within the region and column*:** For each column identified in step 2a, find the azure pixel within *this specific region* that has the smallest row index (the topmost one).

    c. Change Color: Change the color of this topmost azure pixel (identified in 2b) to blue (1).

3. Preserve Other Pixels: All pixels that were not identified as the topmost azure pixel within a specific region and its occupied column retain their original color.
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
    # initialize output_grid
    output_grid = np.copy(input_grid)
    # Find all contiguous regions of azure color
    azure_regions = find_contiguous_regions(output_grid, 8)

    # Process each region independently
    for region in azure_regions:
        # Determine occupied columns for the current region
        columns = set(pixel[1] for pixel in region)

        # Iterate through each column occupied by the current region
        for col in columns:
            # Find the topmost azure pixel within the current region and column
            topmost_pixel = None
            min_row = float('inf')
            for row, c in region:
                if c == col and row < min_row:
                    min_row = row
                    topmost_pixel = (row, col)

            # Change the color of the topmost pixel to blue
            if topmost_pixel:
                output_grid[topmost_pixel[0], topmost_pixel[1]] = 1

    return output_grid
```

