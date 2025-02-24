# 794b24be • 010 • refine_coder

---
```python
"""
Counts the number of blue pixels in the input grid. Creates a red bar in the
first row of the output grid. The width of the red bar is equal to the number of
blue pixels, capped at the width of the grid (3). All other pixels are white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.

    Args:
        input_grid: A 3x3 NumPy array representing the input grid.

    Returns:
        A 3x3 NumPy array representing the transformed output grid.
    """
    # Initialize output_grid as all white.
    output_grid = np.zeros_like(input_grid)

    # Count blue pixels.
    blue_count = np.sum(input_grid == 1)

    # Determine the width of the red bar (capped at grid width).
    red_bar_width = min(blue_count, input_grid.shape[1]) # shape[1] is width

    # Create the red bar in the first row.
    output_grid[0, :red_bar_width] = 2

    return output_grid
```

