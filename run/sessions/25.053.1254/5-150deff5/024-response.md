# 5-150deff5 • 024 • refine_coder

---
```python
"""
For each column in the input grid, replace gray (5) pixels with an alternating sequence of azure (8) and red (2) pixels. The alternation begins with azure at the topmost pixel of the column and continues down the entire column, regardless of whether the gray pixels are contiguous or interrupted by other colors. Pixels that are not gray remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through columns
    for c in range(cols):
        # Initialize the alternating color index. 0 for azure, 1 for red.
        color_index = 0
        # Iterate through rows in the current column
        for r in range(rows):
            if input_grid[r, c] == 5:
                # Replace gray with alternating colors
                if color_index == 0:
                    output_grid[r, c] = 8  # Azure
                else:
                    output_grid[r, c] = 2  # Red
                color_index = 1 - color_index  # Toggle the color index (0 -> 1, 1 -> 0)

    return output_grid.tolist()
```

