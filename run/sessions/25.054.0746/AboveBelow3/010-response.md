# AboveBelow3 • 010 • refine_coder

---
```python
"""
The transformation rule is to identify the top-most contiguous region of any color and shift it upwards by one row, unless it's already at the top edge.
"""

import numpy as np

def find_topmost_region(grid):
    """Finds the top-most contiguous region in the grid."""
    rows, cols = grid.shape
    topmost_region = []
    topmost_row = rows  # Initialize with a value larger than any possible row index
    
    # Find the highest row with any non-zero pixels
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                topmost_row = min(topmost_row,r)

    if topmost_row == rows:
        return []
    # Find all connected pixels starting from the topmost row
    first_color = 0
    for c in range(cols):
        if grid[topmost_row,c] != 0:
            first_color = grid[topmost_row,c]
            break

    visited = set()
    
    def is_valid(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def dfs(row, col):
        if (row, col) in visited or not is_valid(row, col) or grid[row, col] != first_color:
            return
        visited.add((row, col))
        topmost_region.append((row, col))
        
        # Explore adjacent cells (up, down, left, right)
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for c in range(cols):
        if grid[topmost_row,c] == first_color:
            dfs(topmost_row,c)

    return topmost_region

def transform(input_grid):
    """Transforms the input grid by shifting the top-most region up by one row."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the top-most region
    topmost_region = find_topmost_region(input_grid)

    if not topmost_region:
        return output_grid

    # Determine the color of the region
    region_color = input_grid[topmost_region[0]]

    # Clear the original region in the output grid
    for r, c in topmost_region:
        output_grid[r, c] = 0

    # Shift the region up by one row, handling boundary conditions
    for r, c in topmost_region:
        new_r = r - 1
        if new_r >= 0:  # Ensure we don't go out of bounds (top edge)
            output_grid[new_r, c] = region_color
        else:
            output_grid[r,c] = region_color #add the original position back

    return output_grid
```
