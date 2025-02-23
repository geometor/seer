# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
For each 8-connected region of color 8, change the color of the cell to the right of the topmost cell and to the left of the bottommost cell to color 1, provided they are within the grid and are not already color 8.
"""

import numpy as np

def find_regions(grid, color):
    # Use DFS to find connected regions of the specified color
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def dfs(row, col, current_region):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_region.append((row, col))
        # Check 8-connected neighbors
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc, current_region)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_region = []
                dfs(row, col, current_region)
                regions.append(current_region)
    return regions

def find_top_bottom_cells(region):
    # Find top-most and bottom-most cells in a region
    top_most = min(region, key=lambda x: (x[0], x[1]))
    bottom_most = max(region, key=lambda x: (x[0], x[1])) # corrected to use max, not min
    return top_most, bottom_most

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find all regions of color 8
    regions = find_regions(output_grid, 8)

    # Process each region
    for region in regions:
        # Find top-most and bottom-most cells
        top_most, bottom_most = find_top_bottom_cells(region)

        # Modify cell to the right of top-most
        right_cell = (top_most[0], top_most[1] + 1)
        if right_cell[1] < cols and output_grid[right_cell] != 8:
            output_grid[right_cell] = 1

        # Modify cell to the left of bottom-most
        left_cell = (bottom_most[0], bottom_most[1] - 1)
        if left_cell[1] >= 0 and output_grid[left_cell] != 8:
            output_grid[left_cell] = 1

    return output_grid
```

