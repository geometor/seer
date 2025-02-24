# bd4472b8 • 006 • refine_coder

---
```python
"""
1.  **Identify Pattern Region:** Determine the region of the input grid that contains the initial pattern. This is the set of contiguous rows at the top of the input grid that contain non-black (non-zero) pixels.
2.  **Copy Pattern:** Copy this identified pattern region directly to the top of the output grid.
3.  **Replicate First Row Colors:** For each *unique* color present in the *first* row of the input (pattern region), create *one* new row in the output grid, filled entirely with that color. These rows are added immediately below the copied pattern region.
4.  **Implicit Background:** The remaining rows of the grid, if any, should be left with the background, which is black (0). These are not changed by the core transformation.
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

    # Current row index in output grid, just below the copied pattern.
    current_row = pattern_region.shape[0]

    # Replicate colors from the first row, creating one new row per color.
    if pattern_region.shape[0] > 0:
        for color in pattern_region[0, :]:
            output_grid[current_row, :] = color
            current_row += 1  # Increment row index *only once* per color.

    return output_grid
```
