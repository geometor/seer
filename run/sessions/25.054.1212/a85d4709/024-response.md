# a85d4709 • 024 • refine_coder

---
```python
"""
1.  **Grid:** The input and output grids have the same dimensions.
2.  **White Pixels:**
    *   White(0) pixels on even numbered *rows* map to yellow(4). White(0) pixels on odd numbered rows are unchanged.
3.  **Gray Pixels:**
    *   Gray(5) pixels on even numbered *columns* map to color 2 (red).
    *   Gray(5) pixels on odd numbered *columns* map to 3 (green).
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the row/column-based color rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 0:  # White
                if row % 2 == 0:  # Even row
                    output_grid[row, col] = 4  # Yellow
                #else odd row, so unchanged

            elif input_grid[row, col] == 5:  # Gray
                if col % 2 == 0:  # Even column
                    output_grid[row, col] = 2  # Red
                else:  # Odd column
                    output_grid[row, col] = 3  # Green

    return output_grid
```

