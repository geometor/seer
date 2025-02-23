# 29ec7d0e • 008 • example_2 • investigate_coder

---
```python
"""
Removes all pixels of color 0 (white) from the input grid, preserving the position and color of all other pixels.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by removing all white (0) pixels.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array with the same dimensions as the input, but with all 0-value pixels removed.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = input_grid.copy()

    # Iterate through each pixel in the input grid.
    for row_index, row in enumerate(input_grid):
        for col_index, pixel_value in enumerate(row):
            # Check if the pixel's color is white (0).
            if pixel_value == 0:
                # "remove" - by doing nothing to this pixel, the output remains unchanged
                pass
            else:
                # Preserve - copy other values to output
                output_grid[row_index, col_index] = input_grid[row_index, col_index]

    return output_grid
```

