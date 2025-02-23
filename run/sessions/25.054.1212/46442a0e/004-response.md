# 46442a0e • 004 • refine_coder

---
```python
"""
Replicate the input grid to create an output grid with doubled dimensions.
"""

import numpy as np

def transform(input_grid):
    # Determine input grid dimensions.
    input_height, input_width = input_grid.shape

    # Calculate output grid dimensions.
    output_height = 2 * input_height
    output_width = 2 * input_width

    # Initialize the output grid with zeros.
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through the input grid and replicate each cell.
    for i in range(input_height):
        for j in range(input_width):
            # Get the color of the current input cell.
            color = input_grid[i, j]

            # Replicate the color to the corresponding four cells in the output grid.
            output_grid[2 * i, 2 * j] = color
            output_grid[2 * i + 1, 2 * j] = color
            output_grid[2 * i, 2 * j + 1] = color
            output_grid[2 * i + 1, 2 * j + 1] = color

    return output_grid
```

