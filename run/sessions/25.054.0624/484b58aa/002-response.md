# 484b58aa • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is to remove all pixels of color 0 (white) from the input grid, keeping all other pixels in their original positions and with their original colors.
"""

import numpy as np

def transform(input_grid):
    """
    Removes all white (0) pixels from the input grid.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array with white pixels removed.
    """
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)

    # Iterate through each cell in the grid.
    for row_index, row in enumerate(input_grid):
        for col_index, pixel_value in enumerate(row):
            # Check if the pixel is white (value 0).
            if pixel_value == 0:
                # set output pixel to input pixel
                output_grid[row_index, col_index] = pixel_value

    # set output to original pixel for all other cells
    output_grid = np.where(input_grid == 0, 0, input_grid)
    return output_grid
```
