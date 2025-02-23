# 0a938d79 • 008 • example_2 - CODE

---
```python
"""
Transforms an input grid by replicating non-zero values (1 and 3) horizontally in an alternating pattern.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    
    Args:
        input_grid: A 2D numpy array representing the input grid.
    
    Returns:
        A 2D numpy array representing the transformed output grid.
    """
    # Initialize output_grid with the same dimensions and filled with 0s.
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each row
    for r in range(rows):
        # Iterate through each column in the current row
        for c in range(cols):
            # Check if the current cell value is 1 or 3
            if input_grid[r, c] == 1:
                # Replicate 1 and 3 alternately across the row
                for i in range(c, cols):
                    output_grid[r, i] = 1 if (i - c) % 2 == 0 else 3
            elif input_grid[r, c] == 3:
                # Replicate 3 and 1 alternately across the row
                for i in range(c, cols):
                    output_grid[r, i] = 3 if (i - c) % 2 == 0 else 1
            elif input_grid[r,c] == 0:
                # keep 0s
                output_grid[r,c] = 0

    return output_grid
```
