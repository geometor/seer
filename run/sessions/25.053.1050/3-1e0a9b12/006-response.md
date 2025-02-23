# 3-1e0a9b12 • 006 • refine_coder

---
```python
"""
Iterates through each non-zero pixel in the input grid. Attempts to move each pixel down as far as possible within its original column. If a pixel is blocked by another non-zero pixel and column is not clear, it remains in its original position. If the entire column below the pixel consists of zeros, then the pixel is moved to the last row of the output grid, preserving original column order.
"""

import numpy as np

def transform(input_grid):
    output_grid = np.zeros_like(input_grid)
    last_row_pixels = []

    # Iterate through each cell
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            pixel_value = input_grid[r, c]
            if pixel_value != 0:
                # Check for clear column below
                all_zeros_below = True
                for row_below in range(r + 1, input_grid.shape[0]):
                    if input_grid[row_below, c] != 0:
                        all_zeros_below = False
                        break

                if all_zeros_below:
                    last_row_pixels.append((pixel_value, c)) # Store pixel and its column
                else:
                    # Try to move down within column
                    target_r = r
                    for check_r in range(r + 1, input_grid.shape[0]):
                        if output_grid[check_r, c] == 0:
                            target_r = check_r
                        else:
                            break
                    output_grid[target_r, c] = pixel_value

    # Process last row pixels
    last_row_pixels.sort(key=lambda x: x[1])  # Sort by original column
    last_row_col_index = 0
    for pixel_value, _ in last_row_pixels:
        while last_row_col_index < output_grid.shape[1] and output_grid[-1, last_row_col_index] != 0:
            last_row_col_index += 1
        if last_row_col_index < output_grid.shape[1]:
            output_grid[-1, last_row_col_index] = pixel_value


    return output_grid
```
