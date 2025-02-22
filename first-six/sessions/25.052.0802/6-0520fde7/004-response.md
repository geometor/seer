# 6-0520fde7 • 004 • refine_code - CODE

---
```python
"""
The transformation rule is as follows:

1.  **Identify:** Locate the vertical line composed of three contiguous cells of color 5 (gray) in the input grid.
2.  **Center Point:** Determine the central cell within this vertical line.
3.  **Output Grid Initialization:** Create a 3x3 output grid, initially filled entirely with color 0 (white).
4.  **Transformation, Central Cell:** Copy the color 2 to the central cell (1,1) of output grid.
5.  **Transformation - Top Cell:** Copy the color from top of vertical line of color 5 on input and put it on cell (0,2) on output.
6.  **Transformation - Bottom Cell:** Copy the color from the bottom of the vertical line of color 5 on input and put it on cell (2,2) on output.
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find contiguous vertical lines of the specified color
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows - 2):
            if grid[r, c] == color and grid[r+1, c] == color and grid[r+2, c] == color:
                return (r,c)  #return top of the vertical line
    return None

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Convert input grid to numpy array
    input_grid = np.array(input_grid)

    # Find the top cell of the vertical line of color 5
    top_cell = find_vertical_line(input_grid, 5)

    # Initialize the output grid as a 3x3 array filled with 0s
    output_grid = np.zeros((3, 3), dtype=int)

    # If a vertical line of color 5 is found, perform transformation
    if top_cell:
        top_row, center_col = top_cell
        # Place 2 in the center of the output grid
        output_grid[1, 1] = 2
        # Copy the top cell of the vertical line to (0, 2)
        output_grid[0, 2] = input_grid[top_row, center_col]
        # Copy the bottom cell of the vertical line to (2, 2)
        output_grid[2, 2] = input_grid[top_row + 2, center_col]

    return output_grid
```

