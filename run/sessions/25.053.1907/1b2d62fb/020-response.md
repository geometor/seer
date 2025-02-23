# 1b2d62fb • 020 • example_4 - CODE

---
```python
"""
1.  **Identify the central column:** Find the vertical line of pixels with the color blue (value 1) in the input grid.
2.  **Resize:** The width is changed from the original to a new smaller width
3.  **Translate:** Create the output grid, copying the height of the input
4. **Recolor** Change the color of the vertical line from blue (1) to azure (8).
5. **Fill Surrounding:** Change the remaining of the output grid to white (0).
"""

import numpy as np

def find_central_blue_line(grid):
    # Find the column index where all rows have the value 1 (blue).
    rows, cols = grid.shape
    for j in range(cols):
        if np.all(grid[:, j] == 1):
            return j
    return -1  # Return -1 if no such column is found

def transform(input_grid):
    # Find the central blue line's column index.
    blue_line_col = find_central_blue_line(input_grid)

    # Initialize the output grid with the same height as the input and width 3, filled with white (0).
    rows, _ = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)

    # If a blue line was found, replace the corresponding pixels in the output grid with azure (8).
    if blue_line_col != -1:
        for i in range(rows):
            output_grid[i, 0] = 0  # white
            output_grid[i, 1] = 8  # azure
            output_grid[i, 2] = 0

    return output_grid
```
