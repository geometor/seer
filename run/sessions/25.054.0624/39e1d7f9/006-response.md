# 39e1d7f9 • 006 • refine_coder

---
```python
"""
The transformation rule is to swap the colors magenta (6) and green (3) only within the bottom-right quadrant of the grid. If the grid's dimensions are odd, the "center" row and column are included in the bottom-right quadrant.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by swapping magenta (6) and green (3) pixels
    within the bottom-right quadrant of the grid.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The transformed grid.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Determine the start indices for the bottom-right quadrant.
    row_start = rows // 2
    col_start = cols // 2

    # Create a mask for the bottom-right quadrant.
    quadrant_mask = np.zeros_like(input_grid, dtype=bool)
    quadrant_mask[row_start:, col_start:] = True

    # Swap colors only within the masked region.
    temp_grid = np.copy(output_grid) # create temp to swap in place
    output_grid[(temp_grid == 6) & quadrant_mask] = 3
    output_grid[(temp_grid == 3) & quadrant_mask] = 6

    return output_grid
```
