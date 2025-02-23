# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
1.  **Collect:** Gather all non-zero pixels from the input grid.
2.  **Sort:** Sort the gathered non-zero pixels in ascending order.
3. **Place in last row:** Place these sorted, non-zero pixels into the last row of the output grid, starting from the leftmost position and moving right.
4. If any non zero pixels existed in row 2 (index=1) of the input, set them to zero in the output.
5.  **Clear other rows:** All other cells in the output grid, are set to zero (white).
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with zeros, same size as input
    output_grid = np.zeros_like(input_grid)
    
    # Gather all non-zero pixels
    non_zero_pixels = []
    for row_index, row in enumerate(input_grid):
        for col_index, value in enumerate(row):
            if value != 0:
                non_zero_pixels.append(value)
    
    # Sort non-zero pixels in ascending order
    non_zero_pixels.sort()
    
    # Place sorted pixels in the last row
    last_row_index = output_grid.shape[0] - 1
    for col_index, value in enumerate(non_zero_pixels):
        output_grid[last_row_index, col_index] = value

    return output_grid
```
