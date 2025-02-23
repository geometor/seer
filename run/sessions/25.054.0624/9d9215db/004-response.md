# 9d9215db • 004 • refine_coder

---
```python
"""
The input grid's non-white pixels form a "seed" pattern. This pattern is replicated
in a checkered fashion across the output grid. The blue (1) pixels expand to set the
checkered grid. The other colored pixels maintain relative positions to the original
blue pixels.
"""

import numpy as np

def get_non_white_pixels(grid):
    """
    Finds the coordinates and values of non-white pixels in the input grid.
    """
    non_white_pixels = []
    for r_idx, row in enumerate(grid):
        for c_idx, val in enumerate(row):
            if val != 0:
                non_white_pixels.append( ((r_idx, c_idx), val))
    return non_white_pixels

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Find non white pixels and their locations
    non_white_pixels = get_non_white_pixels(input_grid)
    
    # Find the blue pixel to set the checkered pattern.
    blue_pixels = [((r,c), val) for (r,c), val in non_white_pixels if val == 1]

    if not blue_pixels: # Handle edge case, when there are no blue pixels
        return input_grid.tolist()

    blue_row, blue_col = blue_pixels[0][0]

    # Create the checkered pattern based on blue pixel
    for r in range(output_grid.shape[0]):
        for c in range(output_grid.shape[1]):
            if (r + c) % 2 == (blue_row + blue_col) % 2:
                output_grid[r,c] = 1
    
    # Re-place other colored pixels relative to the original blue pixel positions.
    for (r,c), val in non_white_pixels:
        if val != 1:
            row_offset = r - blue_row
            col_offset = c - blue_col

            for r_out in range(output_grid.shape[0]):
                for c_out in range(output_grid.shape[1]):
                    # Check if this is a blue pixel position based on the checkered pattern.
                    if (r_out + c_out) % 2 == (blue_row + blue_col) % 2:
                        new_r = r_out + row_offset
                        new_c = c_out + col_offset

                        if 0 <= new_r < output_grid.shape[0] and 0 <= new_c < output_grid.shape[1]:
                            output_grid[new_r, new_c] = val
                        

    return output_grid.tolist()
```
