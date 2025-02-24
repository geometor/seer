# 794b24be • 028 • refine_coder

---
```python
"""
Identify all blue pixels (value 1) in the input grid. Change all blue pixels to red (value 2). Change all non-zero pixels to zero.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing all blue pixels to red and other non-zero to zero.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the coordinates of all blue pixels (value 1)
    blue_pixel_coords = np.where(output_grid == 1)

    # Change the value of all blue pixels to red (value 2)
    output_grid[blue_pixel_coords] = 2

    # set non-zero, non-red to zero
    output_grid[(output_grid != 0) & (output_grid != 2)] = 0

    return output_grid
```

