# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
1.  **Identify Azure Regions:** Locate all contiguous regions of azure (8) pixels within the input grid.
2.  **Find Minimum Column for each Row with Azure:** In each row, identify the azure pixel that has the minimum column value.
3.  **Introduce Blue Pixel:** Change the identified azure pixel value to blue pixel (1).
4  **All Else:** keep the original input
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
    azure_regions = find_contiguous_regions(input_grid, 8)

    # Create a dictionary to store the minimum column for azure pixels in each row
    min_col_per_row = {}

    # Iterate through all azure regions to collect the minimum column index per row.
    for region in azure_regions:      
        for row, col in region:
            if row not in min_col_per_row:
                min_col_per_row[row] = float('inf')  # Initialize with a large value
            min_col_per_row[row] = min(min_col_per_row[row], col)

    # change the identified azure to blue
    for row, min_col in min_col_per_row.items():
         output_grid[row,min_col] = 1

    return output_grid
```
