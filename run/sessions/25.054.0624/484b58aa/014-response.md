# 484b58aa • 014 • example_3 • investigate_coder

---
```python
"""
The transformation removes all white (0) pixels from the input grid,
while preserving the positions and colors of all other pixels.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid by removing all white pixels.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array with white pixels removed, maintaining
        the relative positions of other pixels.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each pixel in the input grid.
    for row_index, row in enumerate(input_grid):
        for col_index, pixel_value in enumerate(row):
            # Check if the pixel is white (value 0).
            if pixel_value == 0:
                # set white pixels to a different value, such as -1 to exclude in the output
                output_grid[row_index, col_index] = -1

    #remove the -1 values
    output_grid = output_grid[output_grid != -1]

    # reshape output to be the original input
    output_grid = output_grid.reshape(input_grid.shape)

    return output_grid
```
