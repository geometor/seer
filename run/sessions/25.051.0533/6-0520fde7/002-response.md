# 6-0520fde7 • 002 • example_1 - CODE

---
```python
"""
The transformation extracts the color from the center of the input grid.
If the color in the center of the grid is 5, it becomes 2 in output grid. Otherwise, it is 0.
The output is a 3x3 grid filled with color 0, with a centered pixel of color 2.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid to a 3x3 output grid. The output grid is filled with 0s,
    except for the center pixel, which becomes 2 if the center of input is 5.
    """
    # Initialize output_grid as a 3x3 array filled with 0s.
    output_grid = np.zeros((3, 3), dtype=int)

    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Find the center pixel of the input grid.
    center_row = rows // 2
    center_col = cols // 2
    center_color = input_grid[center_row, center_col]

    # Set the center pixel of the output grid.
    if center_color == 5:
      output_grid[1, 1] = 2
    else:
      output_grid[1,1] = 0

    return output_grid
```

