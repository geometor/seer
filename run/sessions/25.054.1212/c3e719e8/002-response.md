# c3e719e8 • 002 • example_1 • investigate_coder

---
```python
"""
The 3x3 input grid is replicated three times along the main diagonal of the 9x9 output grid, while everything else is a 0.
"""

import numpy as np

def transform(input_grid):
    # Initialize a 9x9 output grid filled with 0s.
    output_grid = np.zeros((9, 9), dtype=int)

    # Get the dimensions of the input grid.
    input_height, input_width = input_grid.shape

    # Replicate the input grid along the diagonal.
    for i in range(3):
        for row in range(input_height):
            for col in range(input_width):
                output_grid[row + i * input_height, col + i * input_width] = input_grid[row, col]

    return output_grid
```
