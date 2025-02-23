# 1cf80156 • 002 • example_1 - CODE

---
```python
"""
1.  **Identify:** Find the bounding box of the red colored object within the input grid.
2.  **Crop:** Extract this bounding box, from input.
3. **Rotate:** rotate cropped part clockwise by 90 degrees.
4.  **Output:** Present the rotated and cropped section.
"""

import numpy as np

def get_bounding_box(grid, color):
    rows, cols = np.where(grid == color)
    if len(rows) == 0:  # Handle the case where the color is not found
        return None, None, None, None
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return min_row, max_row, min_col, max_col

def rotate_clockwise(grid):
    return np.rot90(grid, k=-1)

def transform(input_grid):
    # Convert input_grid to a NumPy array for easier manipulation
    input_grid = np.array(input_grid)

    # 1. Identify the red object and its bounding box
    min_row, max_row, min_col, max_col = get_bounding_box(input_grid, 2)

    # 2. Crop the bounding box
    cropped_grid = input_grid[min_row:max_row+1, min_col:max_col+1]
    
    #3. Rotate
    rotated_grid = rotate_clockwise(cropped_grid)

    return rotated_grid.tolist()
```
