# d4469b4b • 028 • refine_coder

---
```python
"""
The input 5x5 grid is reduced to a 3x3 output grid. 
The output grid summarizes 3x3 regions of the input grid.
If any of the input pixels in a 3x3 region centered at the corresponding output pixel's location have a value other than 0, the output pixel is grey (5). 
Otherwise, the output pixel is white (0).
"""

import numpy as np

def get_region(input_array, row, col):
    """Extracts a 3x3 region from the input array centered at (row, col)."""
    row_start = max(0, row - 1)
    row_end = min(input_array.shape[0], row + 2)
    col_start = max(0, col - 1)
    col_end = min(input_array.shape[1], col + 2)
    return input_array[row_start:row_end, col_start:col_end]

def transform(input_grid):
    """Transforms a 5x5 input grid to a 3x3 output grid based on summarization and color transformation."""

    input_array = np.array(input_grid)
    output_array = np.zeros((3, 3), dtype=int)

    # Iterate through the 3x3 output grid
    for i in range(3):
        for j in range(3):
            # Get the 3x3 region centered at the corresponding input pixel
            region = get_region(input_array, i, j)

            # Check if any pixel in the region is not 0
            if np.any(region != 0):
                output_array[i, j] = 5  # Set output to grey (5)
            else:
                output_array[i, j] = 0  # Set output to white (0)

    return output_array.tolist()
```
