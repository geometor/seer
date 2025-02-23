# 1b2d62fb • 014 • example_3 - CODE

---
```python
"""
1.  **Locate Center:** Identify the central vertical column in the input grid. In this case, it's the column at index 3 (the fourth column).
2.  **Extract Subgrid:** Extract a 5x3 subgrid centered on the identified column. This means take the central column, and one column to the left and one column to the right, preserving all rows.
3.  **Recolor:** In the extracted subgrid, change all pixels in the center column that have a value of 1 (blue) to 8 (azure). Keep the values of all other surrounding columns the same.
4.  **Output:** The resulting 5x3 subgrid is the output.
"""

import numpy as np

def get_central_column_index(grid):
    """Helper function to find the index of the central column."""
    return grid.shape[1] // 2

def extract_subgrid(grid, center_col_index, width):
    """Helper function to extract a subgrid of specified width centered on a column."""
    start_col = max(0, center_col_index - width // 2)
    end_col = min(grid.shape[1], center_col_index + width // 2 + 1)
    return grid[:, start_col:end_col]

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # 1. Locate Center
    center_col_index = get_central_column_index(input_grid)

    # 2. Extract Subgrid
    subgrid = extract_subgrid(input_grid, center_col_index, 3)
    output_grid = subgrid.copy()

    # 3. Recolor
    for i in range(output_grid.shape[0]):
      if output_grid[i, output_grid.shape[1]//2] == 1:
        output_grid[i, output_grid.shape[1]//2] = 8

    # 4. Output
    return output_grid.tolist()
```
