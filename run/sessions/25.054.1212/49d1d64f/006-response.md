# 49d1d64f • 006 • refine_coder

---
```python
"""
1.  **Initialization:** Create an output grid with dimensions exactly two times the input grid's dimensions: `(2 * input_height, 2 * input_width)`.

2.  **Replication:** For each pixel in the input grid:
    *   Copy the pixel's value.
    *   Create a 2x2 block in the output grid.
    *   The top-left corner of this 2x2 block should be at position `(2 * row, 2 * column)` in the output grid, where `row` and `column` are the coordinates of the current input pixel.
    *   Fill all four cells of this 2x2 block with the copied pixel value.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height, output_width = 2 * input_height, 2 * input_width  # Corrected output size
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels
    for row in range(input_height):
        for col in range(input_width):
            # replication without padding offset
            pixel_value = input_grid[row, col]
            output_grid[2*row:2*row+2, 2*col:2*col+2] = pixel_value # Corrected indexing

    return output_grid
```

