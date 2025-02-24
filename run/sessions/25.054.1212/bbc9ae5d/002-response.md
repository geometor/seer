# bbc9ae5d • 002 • example_1 • investigate_coder

---
```python
"""
The input grid contains a horizontal line of blue and white pixels. The blue region expands downwards and to the right to form a rectangle, while the white region remains unchanged. The output grid always has three rows.
"""

import numpy as np

def find_regions(grid):
    # Find contiguous regions of the same color.
    regions = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def dfs(row, col, color, current_region):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        current_region.append((row, col))
        dfs(row + 1, col, color, current_region)
        dfs(row - 1, col, color, current_region)
        dfs(row, col + 1, color, current_region)
        dfs(row, col - 1, color, current_region)

    for row in range(rows):
        for col in range(cols):
            if not visited[row, col]:
                current_region = []
                dfs(row, col, grid[row, col], current_region)
                regions.append((grid[row, col], current_region))
    return regions

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Find regions in the input grid
    regions = find_regions(input_grid)

    # Determine the number of blue and white columns
    blue_cols = 0
    white_cols = 0

    for color, pixels in regions:
      if color == 1:
        blue_cols = len(pixels)
      elif color == 0:
        white_cols = len(pixels)


    # Initialize the output grid (3 rows, same number of columns as input)
    output_grid = np.zeros((3, input_grid.shape[1]), dtype=int)

    # Expand the blue region
    for r in range(3):
      for c in range(blue_cols + r):
        output_grid[r,c] = 1

    # fill white regions
    for r in range(3):
      for c in range(blue_cols + r, input_grid.shape[1]):
        output_grid[r,c] = 0
        
    return output_grid.tolist()
```
