# 94f9d214 • 014 • example_3 • investigate_coder

---
```python
"""
Detects horizontal transitions from white (0) to green (3) in the top half of the input grid and marks those locations with red (2) in a smaller output grid. The bottom half of input is ignored.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height = input_height // 2
    output_width = input_width
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # iterate through top half of input grid
    for row in range(output_height):
        # check horizontal transition
        for col in range(input_width - 1):
            if input_grid[row, col] == 0 and input_grid[row, col + 1] == 3:
                # change output to red
                output_grid[row, col + 1] = 2

    return output_grid
```
