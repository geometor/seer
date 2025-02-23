# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
Shifts all non-white objects to the last row, preserving their original column order, and filling the remaining cells with white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the last row,
    maintaining their original column order, and filling the rest with zeros.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    last_row = output_grid.shape[0] - 1

    # Find non-zero elements and their column indices
    non_zero_elements = []
    for col in range(input_grid.shape[1]):
        for row in range(input_grid.shape[0]):
            if input_grid[row, col] != 0:
                non_zero_elements.append((input_grid[row, col], col))

    # Sort the non-zero elements by their column index
    non_zero_elements.sort(key=lambda x: x[1])

    # Place the non-zero elements in the last row of the output grid
    for i, (value, col) in enumerate(non_zero_elements):
        output_grid[last_row, col] = value
    
    # Return the transformed grid.
    return output_grid
```

