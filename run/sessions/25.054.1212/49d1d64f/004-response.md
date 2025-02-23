# 49d1d64f • 004 • refine_coder

---
```python
"""
1.  **Initialization:** Create an output grid with dimensions two times the input grid's dimensions *plus* two (for one row/column of padding on each side): `(2 * input_height + 2, 2 * input_width + 2)`. Initialize all cells of the output grid to 0 (black).

2.  **Replication:** For each pixel in the input grid:
    *   Copy the pixel's value.
    *   Create a 2x2 block in the output grid.
    *   The top-left corner of this 2x2 block should be at position `(2 * row + 1, 2 * column + 1)` in the output grid, where `row` and `column` are the coordinates of the current input pixel.  This "+ 1" offsets into the output grid to account for the zero-padding.
    *   Fill all four cells of this 2x2 block with the copied pixel value.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height, output_width = 2 * input_height + 2, 2 * input_width + 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels
    for row in range(input_height):
        for col in range(input_width):
            # replication with offset for padding
            pixel_value = input_grid[row, col]
            output_grid[2*row+1:2*row+3, 2*col+1:2*col+3] = pixel_value

    return output_grid
```

