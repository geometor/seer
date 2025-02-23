# 7df24a62 • 004 • refine_coder

---
```python
"""
1. Identify the Blue Region: Find the contiguous blue (1) region in the input grid.
2. Determine Bounding Box: Calculate the bounding box (min/max rows and columns) of this blue region.
3. Identify original yellow pixels: Find all of the yellow pixels (4) within the bounding box.
4. Fill Bounding Box: Iterate through all pixels within the bounding box, changing any non-blue to blue.
5. Change initial yellow pixels from yellow to blue.
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

    # Identify original yellow pixels within the bounding box
    original_yellow_pixels = []
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if input_grid[row, col] == 4:
                original_yellow_pixels.append((row, col))

    # Fill Bounding Box: Iterate through all pixels within the bounding box
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            #change to blue
            output_grid[row,col] = 1

    #restore non yellow, non blue
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
          if input_grid[row,col] != 1 and input_grid[row,col] != 4:
            output_grid[row,col] = input_grid[row,col]
            

    #Change initial yellow pixels from yellow to blue.
    for row, col in original_yellow_pixels:
       output_grid[row,col] = 1

    return output_grid
```
