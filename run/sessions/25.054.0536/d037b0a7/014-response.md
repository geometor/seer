# d037b0a7 • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify Key Pixels:** Locate the yellow pixel at the top-left corner (0, 0) and the red pixel at the center (1,1) and all the white pixels.
2.  **Yellow Expansion:** Copy the yellow pixel downwards, replacing all the pixels until the end of the column, inclusive.
3.  **Red stays in place:** The red pixel at (1,1) doesn't change.
4.  **Copy Red below:** The red pixel at (1,1) is copied in the pixels below it.
5.  **Preserve Whites:** All white pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # find yellow pixel (4)
    yellow_pos = np.argwhere(input_grid == 4)
    if len(yellow_pos) > 0:
      yellow_row, yellow_col = yellow_pos[0]
      # Copy yellow downwards
      for i in range(yellow_row, rows):
          output_grid[i, yellow_col] = 4

    # find red pixel(2)
    red_pos = np.argwhere(input_grid == 2)
    if len(red_pos) > 0:
        red_row, red_col = red_pos[0]
        # Copy red downwards
        for i in range(red_row, rows):
          output_grid[i,red_col] = 2


    return output_grid
```
