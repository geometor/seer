# 5-150deff5 • 004 • Response

---

*text:*

```python
"""
1.  **Identify the Object:** Locate the single connected object composed of color 5 in the input grid.

2.  **Change to 8:** all the color 5 is changed to 8.

3.  **Substitution by Component**: the object, now composed by the color 8, has some part replaced by color 2, according to the rule: Every cell color 8 that form an horizontal line of 3 cells long, has the center cell changed to color 2.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all cells with the specified color.
    coords = np.argwhere(grid == color)
    return coords

def transform(input_grid):
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)

    # Find the object with color 5.
    object_coords = find_object(input_grid, 5)

    # Change all instances of color 5 to color 8.
    for r, c in object_coords:
        output_grid[r, c] = 8

    # Iterate through the output grid to find horizontal lines of 3 cells with color 8.
    rows, cols = output_grid.shape
    for r in range(rows):
        for c in range(cols - 2):
            if output_grid[r, c] == 8 and output_grid[r, c+1] == 8 and output_grid[r, c+2] == 8:
                # Change the center cell of the 3-cell line to color 2.
                output_grid[r, c+1] = 2

    return output_grid
```

