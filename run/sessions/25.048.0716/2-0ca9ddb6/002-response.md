# 2-0ca9ddb6 • 002 • Response

---

*text:*

```python
"""
A yellow cross centered on the red pixel and an orange cross centered on the blue pixel is added to the grid. The red and blue pixel are preserved.
"""

import numpy as np

def get_object_positions(grid, color):
    # Helper function to find positions of a specific color
    return np.argwhere(grid == color).tolist()

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the red pixel
    red_positions = get_object_positions(input_grid, 2)
    if red_positions:
        red_row, red_col = red_positions[0]

        # Create yellow cross
        for r, c in [(red_row - 1, red_col), (red_row + 1, red_col)]:
            if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                output_grid[r, c] = 4

    # Find the blue pixel
    blue_positions = get_object_positions(input_grid, 1)
    if blue_positions:
        blue_row, blue_col = blue_positions[0]

        # Create orange cross
        for r, c in [(blue_row, blue_col - 1), (blue_row, blue_col + 1), (blue_row - 1, blue_col), (blue_row + 1, blue_col)]:
            if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                output_grid[r, c] = 7

    return output_grid
```

