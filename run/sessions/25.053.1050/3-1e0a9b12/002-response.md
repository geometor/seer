# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
Extracts all non-zero pixels from the input grid and places them in the last row of the output grid, maintaining their original order. The rest of the cells are made or remain zero.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid, then set it all to zero
    output_grid = np.zeros_like(input_grid)
    
    # Find all non-zero pixels in the input grid
    non_zero_pixels = []
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r, c] != 0:
                non_zero_pixels.append(input_grid[r, c])

    # Place the non-zero pixel values into the last row of the output grid
    for i, value in enumerate(non_zero_pixels):
        if i < output_grid.shape[1]:  # Ensure we don't go out of bounds
           output_grid[-1, i] = value
    
    return output_grid
```

