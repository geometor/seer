# 3-1e0a9b12 • 004 • refine_coder

---
```python
"""
Iterates through each non-zero pixel in the input grid. Attempts to move each pixel down as far as possible within its original column. If the pixel cannot move down in its original column (bottom of grid reached or another non-zero pixel blocks it), then, if all cells below in that column are zero, it's moved to the last row of the output grid, maintaining the original horizontal order with other moved pixels.
"""

import numpy as np

def transform(input_grid):
    output_grid = np.zeros_like(input_grid)
    moved_to_last_row = []
    last_row_index = 0

    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r, c] != 0:
                pixel_value = input_grid[r, c]
                moved_down = False

                # Check if the entire column below is empty
                all_zeros_below = True
                for row_below in range(r + 1, input_grid.shape[0]):
                    if input_grid[row_below, c] != 0:
                        all_zeros_below = False
                        break

                if all_zeros_below:
                  moved_to_last_row.append((pixel_value, (r,c)))
                  continue


                # Try to move down within the same column
                for target_r in range(r + 1, input_grid.shape[0]):
                    if output_grid[target_r, c] == 0:
                        output_grid[target_r, c] = pixel_value
                        moved_down = True

                        if target_r == input_grid.shape[0] -1:
                            break
                    else:

                        break

                if not moved_down:
                    output_grid[r,c] = pixel_value
    #process pixels to move to last row
    moved_to_last_row.sort(key=lambda x: x[1][1])  # Sort by original column
    for pixel_info in moved_to_last_row:
        pixel_value = pixel_info[0]
        while last_row_index < output_grid.shape[1] and output_grid[-1, last_row_index] != 0 :
              last_row_index += 1
        if last_row_index < output_grid.shape[1]:
          output_grid[-1, last_row_index] = pixel_value



    return output_grid
```
