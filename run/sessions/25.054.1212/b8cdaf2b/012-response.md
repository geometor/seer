# b8cdaf2b • 012 • refine_coder

---
```python
"""
1.  **Identify Source Pixels:** Examine the bottom row of the input grid. Identify the non-zero pixels. Note their positions (row, column) and colors. We will call them "source pixels".
2.  **Selective Replication**: For each *source pixel* check if it is one of the colors: 1, 2, 3, or 4.
3. **Targeted Placement**: If the source pixel color is 1,2,3,or 4 then place a pixel of that same color two rows above and one column to the left of the source pixel, and two rows above and one column to the right of the source pixel.
4.  **Boundary Check**: When calculating the positions, skip the replication if the position is beyond the bounds of the input grid.
5. **Overwrite any existing color**: if a position has a color, overwrite it.
"""

import numpy as np

def find_source_pixels(grid):
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
    width = len(input_grid[0])

    # find the source pixels on the bottom row
    source_pixels = find_source_pixels(input_grid)

    # replicate and offset.
    for (row, col), color in source_pixels:
        # selective replication based on color
        if color in [1, 2, 3, 4]:
            # targeted placement: two rows up, one column left and right
            offsets = [(-2, -1), (-2, 1)]
            for row_offset, col_offset in offsets:
                new_row = row + row_offset
                new_col = col + col_offset

                # boundary check
                if 0 <= new_row < height and 0 <= new_col < width:
                    # Overwrite the existing pixel
                    output_grid[new_row, new_col] = color

    return output_grid
```

