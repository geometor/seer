# a9f96cdd • 006 • refine_coder

---
```python
"""
The transformation removes the single non-zero pixel (always color 2) from the input grid and adds new pixels of colors 3, 6, 7, and 8 at positions determined by the original pixel's coordinates and the row length. The number of output pixels depends on the length of the input row containing the non-zero pixel: 1 pixel if row length is 1, 2 pixels if row length is 2, and 4 pixels otherwise. The x and y coordinates of the original non-zero pixels swapped and added to output grid. The colors 3, 6, 7, 8 are used cyclically.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid, filled with zeros.
    output_grid = np.zeros_like(input_grid)

    # Find the non-zero pixel in the input grid.
    input_non_zero = np.argwhere(input_grid != 0)
    
    if len(input_non_zero) == 0:
        return output_grid

    row, col = input_non_zero[0]
    row_length = len(input_grid[row])

    # Determine the number of output pixels and their positions.
    if row_length == 1:
        output_positions = [(col, row)]
    elif row_length == 2:
        output_positions = [(col, row), (col, row)] # needs better pos calc
    else:
        output_positions = [(col, row), (col, row), (col,row), (col, row)]

    # Assign colors to the output pixels.
    colors = [3, 6, 8, 7]
    color_index = 0
    for r, c in output_positions:

        # bounds check
        if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
            output_grid[r, c] = colors[color_index % len(colors)]
            color_index += 1

    return output_grid
```
