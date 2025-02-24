# bd4472b8 • 004 • refine_coder

---
```python
"""
1.  **Identify Pattern Region:** Determine the region of the input grid that defines the transformation, and copy it to the output grid.
2.  **Copy Pattern:** The initial rows with data are copied to top of output.
3.  **Replicate First Row Colors:** For each color in the first row of the input grid:
    *   Create *two* new rows in the output grid filled with that color.
4. **Fill with the background color:** all remaining rows are set to the background color, black (0).
"""

import numpy as np

def get_pattern_region(input_grid):
    # Find the last row with a non-zero value.
    last_non_zero_row = -1
    for i in range(input_grid.shape[0]):
        if np.any(input_grid[i, :] != 0):
            last_non_zero_row = i
        else:
            break # stop looking after a row of zeros

    return input_grid[:last_non_zero_row+1, :]

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    # Identify the pattern region (rows with non-zero values).
    pattern_region = get_pattern_region(input_grid)

    # Initialize the output grid with zeros.
    output_grid = np.zeros_like(input_grid)

    # Copy the original pattern region to the top of the output grid.
    output_grid[:pattern_region.shape[0], :] = pattern_region

    # Current row index in output grid.
    current_row = pattern_region.shape[0]

    # Replicate colors from the first row, creating two new rows per color.
    if pattern_region.shape[0] > 0:
        for color in pattern_region[0, :]:
            output_grid[current_row, :] = color
            current_row += 1
            output_grid[current_row, :] = color
            current_row += 1


    return output_grid
```
