# d037b0a7 • 008 • example_2 • investigate_coder

---
```python
"""
If a 'red' color is present, every color in that row below that color becomes 'red'.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the presence of red pixels.
    If a red pixel is found, all pixels in the rows below it
    change to the same color (red).
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    red_pixels = []

    # 1. Identify Red Pixels
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 2:
                red_pixels.append((r, c))

    # 2. Fill Subsequent Rows
    for r, c in red_pixels:
       for next_row in range(r + 1,rows):
            output_grid[next_row,:] = input_grid[r,c] # Fill all colors in the next rows

    return output_grid
```
