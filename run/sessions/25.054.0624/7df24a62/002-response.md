# 7df24a62 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation involves identifying contiguous blue (1) regions and isolated yellow (4) pixels in the input grid. The blue region is conceptually treated as a square. Yellow pixels within or on the boundary of this original blue square are replaced by blue in the output. Yellow pixels outside this region are retained in their original positions.
"""

import numpy as np

def find_blue_region(grid):
    # Find coordinates of all blue pixels
    blue_coords = np.argwhere(grid == 1)
    if blue_coords.size == 0:
        return None, None, None, None  # No blue region

    # Find the bounding box of the blue region
    min_row = np.min(blue_coords[:, 0])
    max_row = np.max(blue_coords[:, 0])
    min_col = np.min(blue_coords[:, 1])
    max_col = np.max(blue_coords[:, 1])

    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = input_grid.copy()

    # Find the bounding box of the blue region
    min_row, max_row, min_col, max_col = find_blue_region(input_grid)

    if min_row is None:  # Handle cases with no blue region
          return output_grid
    
    # Iterate through all yellow pixels
    yellow_coords = np.argwhere(input_grid == 4)
    for y_row, y_col in yellow_coords:
        # Check if the yellow pixel is within or on the boundary of the original blue square
        if min_row <= y_row <= max_row and min_col <= y_col <= max_col:
            output_grid[y_row, y_col] = 1  # Replace with blue

    #fill blue square
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            output_grid[row,col] = 1

    return output_grid
```
