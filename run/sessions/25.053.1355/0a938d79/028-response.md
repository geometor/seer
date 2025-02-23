# 0a938d79 • 028 • refine_coder

---
```python
"""
1.  **Identify Colored Rows:** Find all rows in the input grid that contain non-zero pixels. Note the color and the row index of each.
2.  **Expand Rows:** For each colored row found, create a new row where every cell containing 0 is set to the color of the original row.
3.  **Create Repeating Pattern:** The expanded rows form a repeating pattern in the output. The pattern appears as alternating rows of the expanded color.
4. **Output Size**: Output size is input size.
"""

import numpy as np

def find_colored_rows(grid):
    """Finds rows with non-zero pixels and returns a dictionary of row_index: color."""
    colored_rows = {}
    for i, row in enumerate(grid):
        for pixel in row:
            if pixel != 0:
                colored_rows[i] = pixel
                break  # Only need the first color in the row
    return colored_rows

def expand_row(grid, row_index, color):
    """Expands a row by replacing all 0s with the specified color."""
    rows, cols = grid.shape
    new_row = np.zeros(cols, dtype=int)
    for i in range(cols):
      if grid[row_index, i] != 0:
        new_row[i] = grid[row_index,i]
      else:
        new_row[i] = color if grid[row_index,i]==0 else grid[row_index,i]
    return new_row

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, _ = output_grid.shape

    # Find colored rows
    colored_rows = find_colored_rows(input_grid)
    
    # Create expanded rows
    expanded_rows = {}
    for row_index, color in colored_rows.items():
        expanded_rows[row_index] = expand_row(input_grid, row_index, color)

    # Build the repeating pattern
    row_indices = sorted(expanded_rows.keys())
    
    output_row_index = 0
    
    while output_row_index < rows:
      for i in row_indices:
          if output_row_index < rows:
              output_grid[output_row_index] = expanded_rows[i]
              output_row_index +=1

    return output_grid
```
