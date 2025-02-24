# 62c24649 • 006 • refine_coder

---
```python
"""
The input grid's pixels are each duplicated into 2x2 blocks of the
same color in the output grid. The output grid is exactly twice the
size of the input grid in each dimension.
"""

import numpy as np

def transform(input_grid):
    # Get input grid dimensions
    input_height, input_width = input_grid.shape

    # Calculate output grid dimensions (exactly doubled)
    output_height = input_height * 2
    output_width = input_width * 2

    # Initialize output grid with zeros
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Duplicate each input pixel into a 2x2 block in the output grid
    for i in range(input_height):
        for j in range(input_width):
            output_grid[2*i, 2*j] = input_grid[i, j]
            output_grid[2*i+1, 2*j] = input_grid[i, j]
            output_grid[2*i, 2*j+1] = input_grid[i, j]
            output_grid[2*i+1, 2*j+1] = input_grid[i, j]

    return output_grid
```

