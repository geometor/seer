# 2-0ca9ddb6 • 004 • Response

---

*text:*

```python
"""
Yellow crosses are added, centered on each red pixel, and orange crosses are centered on each blue pixel. All original red, blue, and azure pixels are kept.
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

    # Find all red pixels
    red_positions = get_object_positions(input_grid, 2)
    for red_row, red_col in red_positions:
        # Create yellow cross
        for r, c in [(red_row - 1, red_col), (red_row + 1, red_col)]:
            if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                output_grid[r, c] = 4

    # Find all blue pixels
    blue_positions = get_object_positions(input_grid, 1)
    for blue_row, blue_col in blue_positions:
        # Create orange cross
        for r, c in [(blue_row, blue_col - 1), (blue_row, blue_col + 1), (blue_row - 1, blue_col), (blue_row + 1, blue_col)]:
            if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                output_grid[r, c] = 7

    return output_grid
```

