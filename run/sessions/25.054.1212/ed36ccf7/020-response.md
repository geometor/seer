# ed36ccf7 • 020 • example_4 • investigate_coder

---
```python
"""
The transformation rule is a 90-degree clockwise rotation of the grid, followed by swapping the color of the cells in the rotated grid, such that any cell that *was* red in the original grid and *is* red after rotation will remain red after the swap.

1.  **Identify Red Pixels:** Locate all pixels in the input grid with the value '2' (red).
2.  **Rotate:** Rotate the whole grid by 90-degree clockwise
3.  **Swap Colors:** Swap colors on all rotated cells, except where the rotated grid and original grid both had red.
"""

import numpy as np

def rotate_grid_90_clockwise(grid):
    return np.rot90(grid, k=-1)

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Identify red pixels
    red_pixels = (input_grid == 2)

    # Rotate
    rotated_grid = rotate_grid_90_clockwise(input_grid)
    
    rotated_red_pixels = (rotated_grid == 2)

    # perform the color swap based on overlap of original red pixels, and rotated red pixels.
    output_grid = np.where(red_pixels & rotated_red_pixels, 2, rotated_grid)
    output_grid = np.where(output_grid == 2, 0, output_grid) # swap remaining 2s with 0
    output_grid = np.where(output_grid != 0, 2, output_grid) # make every other cell 2

    return output_grid.tolist()
```
