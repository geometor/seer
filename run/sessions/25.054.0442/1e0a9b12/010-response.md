# 1e0a9b12 • 010 • refine_coder

---
```python
"""
1.  **Identify all objects**: An object is defined as a single pixel.
2.  **Shift Down**: Every object in the grid attempts to move down by one row.
3. **Blocked**: Objects that have another object directly beneath it in the input grid do not change their position.
4.  **Bottom Right**: If there is a maroon (9) pixel, it moves to the bottom-right corner of the grid, regardless of whether it's blocked. The existing value in bottom-right is removed.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Shift Down and Blocked
    for r in range(rows - 1, -1, -1):  # Iterate from bottom to top
        for c in range(cols):
            if r < rows - 1:  # Not the bottom row
                if input_grid[r+1, c] == 0: # if empty space below, we can move down
                    output_grid[r+1, c] = input_grid[r,c]
                    output_grid[r,c] = 0 # clear original location since it moved

    # Bottom Right (Maroon 9)
    maroon_present = False
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 9:
                maroon_present = True
                output_grid[r, c] = 0  # Clear the original maroon position
                break  # only one maroon, exit inner loop.
        if maroon_present:
            break
    if maroon_present:
        output_grid[rows - 1, cols - 1] = 9

    return output_grid
```
