# 6e02f1e3 • 008 • example_2 • investigate_coder

---
```python
"""
Transforms a 3x3 input grid to a 3x3 output grid based on the following rule:
- Green (3) and Yellow (4) in the input become White (0) in the output.
- Red (2) in the input becomes Gray (5) in the output.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input.
    output_grid = np.zeros_like(input_grid)

    # Iterate through each cell of the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply the transformation rules based on the input cell's color.
            if input_grid[i, j] == 3 or input_grid[i,j] == 4:  # Green or Yellow
                output_grid[i, j] = 0  # White
            elif input_grid[i, j] == 2:  # Red
                output_grid[i, j] = 5  # Gray

    return output_grid
```
