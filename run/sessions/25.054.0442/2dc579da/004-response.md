# 2dc579da • 004 • refine_coder

---
```python
"""
Extracts the top-left subgrid from the input grid, stopping at the first major discontinuity in color.
"""

import numpy as np

def find_discontinuity(grid):
    """
    Finds the point of first discontinuity in the grid, starting from the top-left.
    Discontinuity is defined as a change in color that breaks a perceived pattern.

    Args:
        grid (numpy.ndarray): The input grid.

    Returns:
        tuple: (row_end, col_end), the indices (exclusive) up to which the subgrid is continuous.
    """
    rows, cols = grid.shape
    row_end = rows
    col_end = cols

    # Check for vertical discontinuity
    for r in range(1, rows):
        if not np.all(grid[r, :min(col_end, grid.shape[1])] == grid[0, :min(col_end, grid.shape[1])]):
            row_end = r
            break
            
    # Check for horizontal discontinuity.
    for c in range(1, cols):
        if not np.all(grid[:min(row_end,grid.shape[0]), c] == grid[:min(row_end, grid.shape[0]), 0]):
            col_end = c
            break

    return row_end, col_end

def transform(input_grid):
    """
    Extracts the top-left subgrid of the input grid, stopping at the first discontinuity.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The extracted subgrid.
    """
    # Find the point of discontinuity.
    row_end, col_end = find_discontinuity(input_grid)

    # Extract the subgrid.
    output_grid = input_grid[:row_end, :col_end]

    return output_grid
```
