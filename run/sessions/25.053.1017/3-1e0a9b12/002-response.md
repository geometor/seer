# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
The transformation moves the non-zero elements of the input grid to the last row of the output grid, preserving their original values, and all other cells are zeros. The last row ordering by index in original grid.
"""

import numpy as np

def get_nonzero_elements(grid):
    # Find indices and values of non-zero elements
    indices = np.nonzero(grid)
    values = grid[indices]
    # Combine row, col indices with values and sort them
    elements = []
    for i in range(len(values)):
        elements.append((indices[0][i], indices[1][i], values[i]))
    elements.sort()  # Sorts by row, then by column
    return elements

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    
    # Find non-zero elements and their original positions
    nonzero_elements = get_nonzero_elements(input_grid)

    # Place these elements in the last row of the output grid
    last_row_index = 0
    for _, _, value in nonzero_elements:
        output_grid[-1, last_row_index] = value
        last_row_index += 1

    return output_grid
```
