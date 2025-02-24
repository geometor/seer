# b8cdaf2b • 010 • refine_coder

---
```python
"""
1.  **Copy Bottom Row:** Preserve the entire bottom row of the input grid in the output grid.
2.  **Find Bottom Row Non-Zero Pixels**: Identify all colors in the bottom row that are non-zero.
3. **Replicate and Offset:** For each identified non-zero pixel:

    *   Replicate the colors of the pixels identified in the bottom row.
    *   Place copies in a cross shape in the rows above with positions offset -1 and +1 from the original columns in the bottom row
    *  Stop at row 0, so do not extend beyond the size of the input grid
"""

import numpy as np

def find_bottom_row_nonzero_pixels(grid):
    """Finds the positions and colors of non-zero pixels in the bottom row."""
    bottom_row = grid[-1]
    pixels = []
    for col_idx, color in enumerate(bottom_row):
        if color != 0:
            pixels.append(((len(grid) - 1, col_idx), color))  # ((row, col), color)
    return pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    height = len(input_grid)

    # find the non-zero pixels on the bottom row
    bottom_row_pixels = find_bottom_row_nonzero_pixels(input_grid)

    # replicate and offset.
    for (row, col), color in bottom_row_pixels:

        #offsets for the cross shape, two rows up
        offsets = [(-1, -1), (-1, 1), (-2, -1), (-2, 1)]

        for row_offset, col_offset in offsets:
            new_row = row + row_offset
            new_col = col + col_offset

            # bounds check, and only modify if the current output is 0
            if 0 <= new_row < height and 0 <= new_col < len(input_grid[0]):
                output_grid[new_row, new_col] = color

    return output_grid
```
