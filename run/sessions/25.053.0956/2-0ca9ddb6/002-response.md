# 2-0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
The program identifies 'key pixels' in the input. If it is red, it creates a 2x2 yellow square, and if blue, a 3x3 orange square is created in the output, with specific positions relative to the original key pixel position.
"""

import numpy as np

def get_key_pixels(grid):
    # Find coordinates and colors of non-zero pixels.
    key_pixels = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] != 0:
                key_pixels.append(((i, j), grid[i, j]))
    return key_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    
    # get key pixels (non-zero pixels)
    key_pixels = get_key_pixels(input_grid)

    # change output pixels based on key pixel color and location
    for (row, col), color in key_pixels:
        if color == 2:  # Red pixel
            output_grid[row-1:row+1, col-1:col+1] = 4  # 2x2 yellow square
        elif color == 1:  # Blue pixel
            output_grid[row-1:row+2, col-1:col+2] = 7  # 3x3 orange square

    return output_grid
```
