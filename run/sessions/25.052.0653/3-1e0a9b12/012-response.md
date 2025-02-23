# 3-1e0a9b12 • 012 • refine_code - CODE

---
```python
"""
Moves all non-zero single-cell objects to the last row of the grid,
maintaining their relative horizontal order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero single-cell objects to the last row,
    maintaining their relative horizontal order.
    """
    # Convert input_grid to a NumPy array
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                # Check for single-cell object
                is_single = True
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i != 0 or j != 0) and 0 <= r + i < rows and 0 <= c + j < cols:
                            if input_grid[r + i, c + j] == input_grid[r, c]:
                                is_single = False
                                break
                    if not is_single:
                        break

                # Move single-cell object to last row
                if is_single:
                    output_grid[rows - 1, c] = input_grid[r, c]
                    if r != rows -1:
                        output_grid[r,c] = 0

    return output_grid.tolist()  # Convert back to list for consistency

```

