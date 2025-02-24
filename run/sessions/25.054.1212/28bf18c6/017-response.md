# 28bf18c6 • 017 • refine_coder

---
```python
"""
1. Identify Objects: Find all contiguous regions of non-zero colored pixels in the input grid. Consider each region as a separate object.
2. Extract Object: Extract the object in the input grid.
3. Create new grid: the output grid has 3 rows, and 6 columns
4. Reshape Object: Replicate and interleave the pixels to the correct size. The output object should have the form

   x x 0 x x 0
   x 0 0 x 0 0
   0 x 0 0 x 0

5. Output the resulting grid.
"""

import numpy as np

def find_object(grid):
    """Finds the bounding box of the non-zero object in the grid."""
    rows, cols = np.where(grid != 0)
    if len(rows) == 0:
        return None  # No object found
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return (min_row, min_col, max_row, max_col)

def extract_object(grid, bbox):
    """Extracts the object from the grid based on the bounding box."""
    min_row, min_col, max_row, max_col = bbox
    return grid[min_row:max_row+1, min_col:max_col+1]

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros((3, 6), dtype=int)

    # Find and extract Object
    bbox = find_object(input_grid)
    if bbox is None:
        return output_grid.tolist() # Return empty grid if no object
    
    object_pixels = extract_object(input_grid, bbox).flatten()
    object_pixels = object_pixels[object_pixels != 0] # Remove any zeros that were in the bounding box
    
    if len(object_pixels) == 0:
        return output_grid.tolist()

    object_color = object_pixels[0]

    # Reshape and interleave the object.
    pattern = [
      [1, 1, 0, 1, 1, 0],
      [1, 0, 0, 1, 0, 0],
      [1, 1, 1, 1, 1, 1]
    ]

    # Place object color
    for r in range(3):
      for c in range(6):
        if pattern[r][c] == 1:
          output_grid[r,c] = object_color

    return output_grid.tolist()
```
