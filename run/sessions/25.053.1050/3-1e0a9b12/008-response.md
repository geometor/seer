# 3-1e0a9b12 • 008 • refine_coder

---
```python
"""
Iterates through each non-zero pixel in the input grid. If a pixel is blocked by another non-zero pixel, it falls down until it encounters an obstacle. Otherwise the objects falls to the bottom row.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with zeros
    output_grid = np.zeros_like(input_grid)

    # Iterate through each cell in the input grid
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
                    #find first empty spot on bottom row
                    for target_c in range(output_grid.shape[1]):
                        if output_grid[-1,target_c] == 0:
                            output_grid[-1, target_c] = pixel_value
                            break
                else:
                    # Try to move down within column, stopping above other pixels
                    target_r = r
                    for check_r in range(r + 1, input_grid.shape[0]):
                        if output_grid[check_r, c] == 0:
                            target_r = check_r
                        else:
                            break
                    output_grid[target_r, c] = pixel_value

    return output_grid
```
