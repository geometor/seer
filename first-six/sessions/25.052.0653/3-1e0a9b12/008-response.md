# 3-1e0a9b12 • 008 • refine_code - CODE

---
```python
"""
Transforms the input grid by shifting all non-zero objects downwards. The shift amount for each object is determined by the number of empty (all-zero) rows below the object.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by shifting non-zero objects downwards.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)
    
    # Create a list to store non-zero elements and their new positions
    non_zero_elements = []

    # 1. Identify Non-Zero Objects and Their Positions, and empty rows below
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                empty_rows_below = 0
                for r_below in range(r + 1, rows):
                    if np.all(input_grid[r_below, :] == 0):
                        empty_rows_below += 1

                non_zero_elements.append(((r, c), input_grid[r, c], empty_rows_below))

    # 2. Calculate new positions and fill the output grid
    for (r, c), value, empty_rows_below in non_zero_elements:
        new_row = r + empty_rows_below
        if new_row < rows: #boundary condition check
           output_grid[new_row, c] = value

    # 3. Remove top empty rows
    first_non_empty_row = 0
    for r in range(rows):
        if np.any(output_grid[r,:] !=0):
            first_non_empty_row = r
            break
    
    output_grid = output_grid[first_non_empty_row:, :]

    return output_grid.tolist()
```
