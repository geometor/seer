# eb5a1d5d • 008 • example_2 • investigate_coder

---
```python
"""
Reduces a large grid to a 3x3 representation. The center pixel of the output represents the color of the inner, centered region of the input, and the output border has the same color as the input border.
"""

import numpy as np

def get_border_color(grid):
    # Return color of the top-left pixel.  Assumes a filled rectangle.
    return grid[0, 0]

def get_center_color(grid):
    # find the center of the grid
    center_y = grid.shape[0] // 2
    center_x = grid.shape[1] // 2

    # start from the center and search outward for first different color

    color = grid[center_y, center_x]
    
    return color

def transform(input_grid):
    # Get the border color.
    border_color = get_border_color(input_grid)

    # Get the center color.
    center_color = get_center_color(input_grid)

    # Create a 3x3 output grid filled with the border color.
    output_grid = np.full((3, 3), border_color, dtype=int)

    # Set the center pixel of the output grid to the center color.
    output_grid[1, 1] = center_color

    return output_grid
```
