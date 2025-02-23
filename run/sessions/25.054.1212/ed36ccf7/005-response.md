# ed36ccf7 • 005 • refine_coder

---
```python
"""
Perform a partial color swap between white (0) pixels and the color of the pixel at input[0][0]. The swap occurs based on relative positions of non-white and white pixels within only the first row and first column. Pixels not located in the first row or first column are not changed.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the specified color-swapping rule.

    Args:
        input_grid: The input grid as a list of lists.

    Returns:
        The transformed grid as a list of lists.
    """
    # Initialize output_grid as a copy of input_grid
    output_grid = [row[:] for row in input_grid]
    height = len(input_grid)
    if height == 0:
        return output_grid
    width = len(input_grid[0])
    if width == 0:
      return output_grid

    # Determine the non-white color to swap (from the top-left pixel)
    swap_color = input_grid[0][0]

    # Handle the trivial case where the top-left pixel is already white
    if swap_color == 0:
        return output_grid

    # Iterate through the first row
    for j in range(width):
        if input_grid[0][j] == 0 and j < input_grid[0].index(swap_color) if swap_color in input_grid[0] else True:
            output_grid[0][j] = swap_color
        elif input_grid[0][j] == swap_color and (j < input_grid[0].index(0) if 0 in input_grid[0] else False):
            output_grid[0][j] = 0


    # Iterate through the first column
    for i in range(height):
        if input_grid[i][0] == 0 and i < [row[0] for row in input_grid].index(swap_color) if swap_color in [row[0] for row in input_grid] else True :
            output_grid[i][0] = swap_color
        elif input_grid[i][0] == swap_color and (i < [row[0] for row in input_grid].index(0) if 0 in [row[0] for row in input_grid] else False):
             output_grid[i][0] = 0

    return output_grid
```
