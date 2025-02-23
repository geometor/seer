# 27a28665 • 014 • example_3 • investigate_coder

---
```python
"""
The program counts the number of separate white (0) regions in the input grid. A region is defined as one or more connected white squares.
"""

import numpy as np

def find_regions(grid, color):
    """
    Finds distinct regions of a specific color in the grid.
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()
    region_count = 0

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(row, col):
        """
        Depth-first search to explore a connected region.
        """
        if (row, col) in visited or not is_valid(row, col) or grid[row][col] != color:
            return
        visited.add((row, col))
        # Explore adjacent cells (up, down, left, right)
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color and (r, c) not in visited:
                dfs(r, c)
                region_count += 1
    return region_count
    

def transform(input_grid):
    """
    Counts the number of distinct white (0) regions in the input grid.
    """
    # Convert input_grid to a NumPy array for easier processing.
    grid = np.array(input_grid)

    # Find and count white regions.
    white_regions_count = find_regions(grid, 0)
    
    # The output should be represented as a single-element grid (1x1) showing
    # the count. The count is a number, using color 'red'=2 for visualization,
    # to represent a count
    output_grid = np.array([[white_regions_count]])
    return output_grid
```
