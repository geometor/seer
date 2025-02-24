# 9172f3a0 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is to expand each pixel in the input grid into a 3x3 block of the same color in the output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height = input_height * 3
    output_width = input_width * 3
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # iterate over input grid, and change output pixels
    for i in range(input_height):
        for j in range(input_width):
            # Calculate the top-left corner of the 3x3 block in output_grid
            output_row_start = i * 3
            output_col_start = j * 3
            
            # Fill the 3x3 block with input pixel's value
            output_grid[output_row_start:output_row_start+3, output_col_start:output_col_start+3] = input_grid[i, j]

    return output_grid
```
