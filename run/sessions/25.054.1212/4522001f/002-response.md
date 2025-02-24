# 4522001f • 002 • example_1 • investigate_coder

---
```python
"""
The transformation expands the input grid by a factor of 3 in both dimensions. 
It replicates the shape formed by adjacent green (3) pixels in the input to the output, 
with coordinate of the object multiplied by 3.
Other pixels in output is filled by white (0) color.
"""

import numpy as np

def expand_shape(input_grid):
    """
    Identifies the shape formed by adjacent green pixels and its coordinates.
    """
    green_pixels = []
    rows, cols = input_grid.shape
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 3:
                green_pixels.append((r, c))

    return green_pixels

def transform(input_grid):
    # initialize output_grid
    input_rows, input_cols = input_grid.shape
    output_rows, output_cols = input_rows * 3, input_cols * 3
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Find the green shape
    green_pixels = expand_shape(input_grid)

    # Replicate the green shape in the output grid, scaled by 3.
    for r, c in green_pixels:
        for i in range(3):
            for j in range(3):
                output_grid[r*3 + i, c*3 + j] = 3

    return output_grid
```
