# 1b2d62fb • 006 • refine_coder

---
```python
"""
1.  **Input:** Receive a 2D grid (`input_grid`) of integers (0-9).
2.  **Blue Line Detection:** Find the vertical blue line (all pixels in a column are blue (1)) in the input grid. Note its column index. If no blue line is found, output all 0 grid with the dimensions of the input grid.
3.  **Output Grid Initialization:** Create an output grid (`output_grid`) with the same number of rows as the input grid and 3 columns, initially filled with zeros (0).
4.  **Row Iteration:** Iterate through each row of the `input_grid`.
5.  **Azure Check:** For each row:
    *   If the row contains *any* azure (8) pixels:
        *   Iterate through the columns of the current row in the `input_grid`.
        *   If an azure pixel is found:
            *   If the azure pixel's column index is *less than* the blue line's column index, place an azure (8) in column 0 of the corresponding row in the `output_grid`.
            *   If the azure pixel's column index is *greater than* the blue line's column index, place an azure (8) in column 2 of the corresponding row in the `output_grid`.
            *   If the azure pixel's column index *is equal to* the blue line's column index, place an azure (8) in column 1 of the corresponding row of the output grid.
    *   If the row does *not* contain any azure (8) pixels, the corresponding row in the `output_grid` remains all zeros (0).
6.  **Output:** Return the `output_grid`.
"""

import numpy as np

def find_vertical_line(grid, color):
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i,j] == color for i in range(rows)):
            return j
    return -1

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Blue Line Detection
    blue_line_col = find_vertical_line(input_grid, 1)

    # Output Grid Initialization
    output_grid = np.zeros((rows, 3), dtype=int)

    if blue_line_col == -1:
        return output_grid

    # Row Iteration
    for i in range(rows):
        # Azure Check
        if 8 in input_grid[i]:
            for j in range(cols):
                if input_grid[i, j] == 8:
                    if j < blue_line_col:
                        output_grid[i, 0] = 8
                    elif j > blue_line_col:
                        output_grid[i, 2] = 8
                    else:
                        output_grid[i, 1] = 8
        # else:  # Implicitly handled by initialization to zeros
        #     output_grid[i, :] = 0  # Keep row all zeros

    # Output
    return output_grid
```
