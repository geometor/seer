# 2bee17df • 002 • example_1 - CODE

---
```python
"""
Preserves red (2) and azure (8) borders. Changes to green (3) the white pixels vertically aligned with the red frame.
Fills the interior region bounded by the red and azure frames with green (3).
"""

import numpy as np

def find_borders(grid, color):
    # Find the row and column indices where the border color exists.
    rows, cols = np.where(grid == color)
    return rows, cols

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find red (2) and azure (8) borders.
    red_rows, red_cols = find_borders(input_grid, 2)
    azure_rows, azure_cols = find_borders(input_grid, 8)

    # Determine the bounding box of the interior region.
    min_red_row = np.min(red_rows)
    #max_red_row = np.max(red_rows)  # Not strictly needed
    min_red_col = np.min(red_cols) if len(red_cols)> 0 else 0 # add default for case when color is not present
    max_red_col = np.max(red_cols)

    #min_azure_row = np.min(azure_rows) # Not strictly needed
    max_azure_row = np.max(azure_rows)
    min_azure_col = np.min(azure_cols)
    #max_azure_col = np.max(azure_cols) # not strictly needed

    # Find first vertical white line
    for c in range(min_red_col, max_red_col):
      if output_grid[min_red_row + 1, c] == 0:
        for r in range(min_red_row + 1, max_azure_row):
            if output_grid[r,c] == 0:
                output_grid[r,c] = 3
        break


    # Fill the interior with green (3).
    for r in range(min_red_row + 1, max_azure_row):
        for c in range(min_azure_col + 1, max_red_col):
            if output_grid[r, c] == 0:
                output_grid[r, c] = 3

    return output_grid
```

