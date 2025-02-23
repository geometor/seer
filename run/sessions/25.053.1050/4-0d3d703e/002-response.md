# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
The program performs a direct substitution of each value.
1.  For every pixel in the input grid:
    *   If the pixel's value is 1, replace it with 4.
    *   If the pixel's value is 2, replace it with 5.
    *   If the pixel's value is 3, replace it with 6.
    *   Otherwise, keep the pixel's value.
2.  Output is the resulting grid
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid by applying a value substitution."""

    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Define the substitution mapping.
    substitution_map = {
        1: 4,
        2: 5,
        3: 6
    }

    # Iterate through the grid and apply the substitution.
    for row_index, row in enumerate(input_grid):
        for col_index, value in enumerate(row):
            if value in substitution_map:
                output_grid[row_index, col_index] = substitution_map[value]

    return output_grid
```

