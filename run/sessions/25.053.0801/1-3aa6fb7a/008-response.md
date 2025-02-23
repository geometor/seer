# 1-3aa6fb7a • 008 • example_2 - CODE

---
```python
"""
Identify all azure (8) pixels in the input grid. For each azure pixel, check if there is an adjacent azure pixel to its right. If not, place a blue (1) pixel to its immediate left.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel of the input grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is azure (8)
            if input_grid[r, c] == 8:
                # Check for adjacent azure pixel to the right
                if c + 1 < cols and input_grid[r, c + 1] != 8:
                    # Add a blue (1) pixel to the left
                    if c > 0:
                        output_grid[r, c - 1] = 1

    return output_grid
```

