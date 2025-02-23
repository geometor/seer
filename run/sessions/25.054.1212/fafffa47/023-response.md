# fafffa47 • 023 • refine_coder

---
```python
"""
1.  **Identify Maroon Pixels:** Locate all pixels in the input grid with a value of 9 (maroon).
2.  **Bounding Box:** Determine a rectangle bounding box containing all the maroon pixels. The top left corner of this box is the origin, and the bottom right marks the bounds.
3.  **Output Grid:** Create a new output grid. Initialize all cells as black (0). The dimensions are always 3x3.
4. **Top Row corners**: In the output grid, examine the top row of the input's maroon bounding box. If a maroon pixel exists in the top row of the bounding box, then turn the corresponding top corner(s) of the output to red (2).
5. **Vertical Mirror**: If a maroon pixel exists in input grid column `c` in the bottom half of the input (rows 3-5) then set the cell at `(2,c)` to red.
"""

import numpy as np

def get_maroon_bounding_box(grid):
    maroon_positions = np.argwhere(grid == 9)
    if maroon_positions.size == 0:
        return None  # No maroon pixels
    min_row = maroon_positions[:, 0].min()
    max_row = maroon_positions[:, 0].max()
    min_col = maroon_positions[:, 1].min()
    max_col = maroon_positions[:, 1].max()
    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    # initialize output_grid as 3x3 array of all zeros
    output_grid = np.zeros((3, 3), dtype=int)
    input_grid = np.array(input_grid)

    # Get bounding box of maroon pixels
    bounding_box = get_maroon_bounding_box(input_grid)
    if bounding_box is None:
        return output_grid

    (min_row, min_col), (max_row, max_col) = bounding_box

    # Check top row of bounding box for corners
    for c in range(min_col, max_col + 1):
       if input_grid[min_row,c] == 9:
           if c == min_col:
                output_grid[0, 0] = 2  # Top-left
           if c == max_col:
                output_grid[0, 2] = 2  # Top-right
           if min_col < c < max_col:
               output_grid[0,1] = 2 # Top-middle

    # Vertical Mirror for bottom half
    for r in range(3,6):
        for c in range(3):
            if input_grid[r,c] == 9:
                output_grid[2,c] = 2

    return output_grid
```
