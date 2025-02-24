# 54d82841 • 002 • example_1 • investigate_coder

---
```python
"""
We have an 8x8 grid of pixels, primarily white (0) and magenta (6).
Locate two specific white pixel at the bottom row (row index 7). One at column index 2, and the other at column index 6.
Change color of pixels in those locations to yellow (4).
All other pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing the color of two specific pixels
    at the bottom row to yellow.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Define the locations to be changed.
    locations = [[7, 2], [7, 6]]

    # Change the color of the specified pixels to yellow (4).
    for row, col in locations:
        output_grid[row, col] = 4

    return output_grid
```

