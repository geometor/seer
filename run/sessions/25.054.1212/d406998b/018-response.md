# d406998b • 018 • refine_coder

---
```python
"""
Iterates through the input grid, identifying gray (5) pixels. If a gray pixel
has a white (0) pixel immediately to its right or immediately below it,
the gray pixel is changed to green (3).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid.
    for row in range(rows):
        for col in range(cols):
            # Check if the current pixel is gray.
            if output_grid[row, col] == 5:
                # Check the pixel to the right.
                if col + 1 < cols and output_grid[row, col + 1] == 0:
                    output_grid[row, col] = 3
                    continue  # Move to the next pixel after a replacement.

                # Check the pixel below.
                if row + 1 < rows and output_grid[row + 1, col] == 0:
                    output_grid[row, col] = 3
                    continue  # Move to the next pixel after a replacement.

    return output_grid
```

