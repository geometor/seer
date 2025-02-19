# 1bfc4729 • 002 • example_1 - CODE

---
```python
"""
The transformation rule involves taking each single-cell object in the input, 
and create frame and columns, depending on the original cell color.
If the object is magenta (6), replicate it to top and bottom row. 
Then draw two lines, 3 cells down from the top, and 3 cells up from the bottom.
If the object is orange (7), replicate it to top and bottom row. 
Then draw two lines, 3 cells down from the top, and 3 cells up from the bottom.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the input grid to find single-cell objects
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                color = input_grid[r,c]

                # replicate color to top and bottom rows
                output_grid[0, :] = color
                output_grid[rows - 1, :] = color

                # draw vertical lines
                output_grid[r+1:r+4,0] = color
                output_grid[r+1:r+4,cols-1] = color

    return output_grid
```

