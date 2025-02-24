# 3af2c5a8 • 008 • example_2 • investigate_coder

---
```python
"""
The input grid is expanded to create the output grid. The input grid is doubled in both dimensions (height and width). This is achieved by replicating the input grid twice horizontally and twice vertically, creating a 2x2 tiled pattern of the original input grid.
"""

import numpy as np

def transform(input_grid):
    # Get dimensions of the input grid
    input_rows, input_cols = input_grid.shape

    # Calculate dimensions of the output grid
    output_rows = input_rows * 2
    output_cols = input_cols * 2

    # Initialize the output grid with zeros
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Iterate through the input grid and replicate it in the output grid
    for i in range(input_rows):
        for j in range(input_cols):
            # Copy each pixel of the input grid to four corresponding locations in output
            output_grid[i*2, j*2] = input_grid[i, j]
            output_grid[i*2 + 1, j*2] = input_grid[i, j]
            output_grid[i*2, j*2 + 1] = input_grid[i, j]
            output_grid[i*2 + 1, j*2 + 1] = input_grid[i, j]

    return output_grid
```
