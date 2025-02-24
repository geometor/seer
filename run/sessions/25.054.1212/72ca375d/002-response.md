# 72ca375d • 002 • example_1 • investigate_coder

---
```python
"""
1. Identify the Target Color: The program focuses on a single color within the input grid, in this instance magenta (represented by the digit 6).
2. Locate the Bounding Box: Determine the smallest rectangular area that encloses all pixels of the target color (magenta) in the input grid. Note the row and column of the upper-left and lower right pixels.
3. Extract the area: Create the ouput grid that represents a cropped view of the input grid, using the coordinates of the bounding box identified in step 2, filled with the pixels of the target color.
"""

import numpy as np

def find_bounding_box(grid, target_color):
    """
    Finds the bounding box of a target color in a grid.
    Returns (min_row, min_col, max_row, max_col)
    """
    rows, cols = np.where(grid == target_color)
    if len(rows) == 0:
        return None  # Target color not found
    min_row, min_col = np.min(rows), np.min(cols)
    max_row, max_col = np.max(rows), np.max(cols)
    return min_row, min_col, max_row, max_col

def transform(input_grid):
    """
    Extracts a rectangular region of a specific color from the input grid.
    """
    input_grid = np.array(input_grid)  # Ensure input is a NumPy array.
    target_color = 6

    # Find the bounding box of the target color.
    bounding_box = find_bounding_box(input_grid, target_color)
    if bounding_box is None:
        return [[]] # Return empty grid.

    min_row, min_col, max_row, max_col = bounding_box

    # Extract the region.
    output_grid = input_grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid.tolist()
```
