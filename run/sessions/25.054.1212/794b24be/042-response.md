# 794b24be • 042 • refine_coder

---
```python
"""
Transforms an input grid by identifying a region of blue pixels, creating a bounding box around them,
and then drawing a filled red rectangle of the same dimensions as the bounding box onto a 3x3 output grid.
"""

import numpy as np

def _find_blue_region(input_grid):
    """Finds the bounding box of blue pixels in the input grid."""
    blue_pixels = np.where(input_grid == 1)
    if len(blue_pixels[0]) == 0:
        return None  # No blue pixels found
    min_row, min_col = np.min(blue_pixels, axis=1)
    max_row, max_col = np.max(blue_pixels, axis=1)
    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.

    Args:
        input_grid: A numpy array representing the input grid.

    Returns:
        A 3x3 numpy array representing the transformed output grid.
    """
    # Create bounding box
    bounding_box = _find_blue_region(input_grid)

    # initialize output_grid as 3x3 and filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Draw red rectangle
    if bounding_box:
        (min_row, min_col), (max_row, max_col) = bounding_box
        #clamp the coordinates to the output grid bounds
        min_row = max(0,min_row)
        min_col = max(0, min_col)
        max_row = min(2, max_row)
        max_col = min(2, max_col)
        output_grid[min_row:max_row+1, min_col:max_col+1] = 2

    return output_grid
```
