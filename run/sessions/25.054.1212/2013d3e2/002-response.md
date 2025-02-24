# 2013d3e2 • 002 • example_1 • investigate_coder

---
```python
"""
Extracts a 3x3 subgrid from the input grid, starting from the top-left corner of the central non-zero object.
"""

import numpy as np

def find_top_left_object(grid):
    """Finds the top-left corner coordinates of the non-zero object."""
    rows, cols = np.where(grid != 0)
    if len(rows) == 0:  # Handle the case where there are no non-zero pixels
        return None, None
    top_left_row = np.min(rows)
    top_left_col = np.min(cols)
    return top_left_row, top_left_col

def transform(input_grid):
    """
    Extracts a 3x3 subgrid representing the top-left of the object.
    """
    # Convert input_grid to numpy array for easier manipulation
    input_grid = np.array(input_grid)

    # Find the top-left corner of the central object.
    start_row, start_col = find_top_left_object(input_grid)
    
    if start_row is None or start_col is None:  # No object found
        return np.zeros((3, 3), dtype=int).tolist() # return blank 3x3 grid.


    # Extract the 3x3 subgrid.
    output_grid = input_grid[start_row:start_row+3, start_col:start_col+3]

    return output_grid.tolist()
```
