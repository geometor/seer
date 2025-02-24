# 017c7c7b • 004 • refine_coder

---
```python
"""
The program takes the input grid, increases its height by a factor of 1.5, and replaces blue pixels (1) with red pixels (2) in the corresponding rows of the output grid. White pixels (0) remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid.
    input_height = input_grid.shape[0]
    input_width = input_grid.shape[1]
    output_height = int(input_height * 1.5)
    output_width = input_width
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through each pixel of the input grid.
    for i in range(input_height):
        for j in range(input_width):
            # Change output pixels: If the pixel is blue (1), change it to red (2).
            if input_grid[i, j] == 1:
                output_grid[i, j] = 2
            else:
                output_grid[i,j] = input_grid[i,j]

    return output_grid
```
