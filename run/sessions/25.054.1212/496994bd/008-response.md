# 496994bd • 008 • example_2 • investigate_coder

---
```python
"""
The transformation rule is a selective vertical reflection. It swaps the positions of the rows containing only 'azure' (8) and 'red' (2) pixels, while leaving the rows containing only 'white' (0) pixels unchanged.
"""

import numpy as np

def find_rows_by_color(grid, color):
    """Finds rows that are entirely a specific color."""
    rows = []
    for i, row in enumerate(grid):
        if np.all(row == color):
            rows.append(i)
    return rows

def transform(input_grid):
    """
    Transforms the input grid by swapping the positions of rows containing only azure (8) and red (2) pixels.
    Rows with only white (0) remain unchanged.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find the indices of rows that are all azure (8) or all red (2)
    azure_rows = find_rows_by_color(input_grid, 8)
    red_rows = find_rows_by_color(input_grid, 2)
    
    # Check if we have the same number of azure and red rows (as expected in a swap)
    if len(azure_rows) != len(red_rows):
      # cannot perform reflection if numbers of rows don't match
      return None

    # Swap the rows in the output grid
    for i in range(len(azure_rows)):
        output_grid[azure_rows[i]] = input_grid[red_rows[i]]
        output_grid[red_rows[i]] = input_grid[azure_rows[i]]

    return output_grid
```
