# 29c11459 • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify the Target Row:** Find the row (in this case, row 1) containing both a blue pixel (1) and a red pixel (2).
2.  **Locate Start and End:** Identify the column indices of the blue pixel (start) and the red pixel (end) on that row.
3.  **Connect with a line:** Connect the blue pixel to the center, connect the end pixel to the center
4.  **Connect at center**: Add a pixel of color grey at the center.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds the coordinates of all pixels of a given color."""
    return np.argwhere(grid == color)

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the row containing both blue (1) and red (2) pixels
    blue_pixels = find_pixels_by_color(input_grid, 1)
    red_pixels = find_pixels_by_color(input_grid, 2)

    target_row = -1
    for b_row, _ in blue_pixels:
        for r_row, _ in red_pixels:
            if b_row == r_row:
                target_row = b_row
                break
        if target_row != -1:
            break

    if target_row == -1:
        return output_grid  # No such row found

    # Locate Start and End
    blue_cols = [col for row, col in blue_pixels if row == target_row]
    red_cols = [col for row, col in red_pixels if row == target_row]

    if not blue_cols or not red_cols:
      return output_grid
    
    start_col = min(blue_cols)
    end_col = max(red_cols)
    
    center_col = (cols -1) // 2

    #connect blue to center
    for col in range(start_col, center_col):
      output_grid[target_row, col] = 1

    #connect red to center
    for col in range(center_col + 1, end_col + 1):
      output_grid[target_row, col] = 2

    # place grey pixel
    output_grid[target_row, center_col] = 5
    

    return output_grid
```
