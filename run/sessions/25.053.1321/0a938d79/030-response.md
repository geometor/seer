# 0a938d79 • 030 • refine_coder

---
```python
"""
1.  **Identify Significant Rows:** Scan the input grid to find rows that contain exactly one non-zero (non-white) color value. Record the row index and the color value for each.
2.  **Expand Significant Rows:** For each significant row, the single non-zero color will fill an entire row in the output.
3.  **Determine Output Row Pattern**: Create a repeating pattern of rows in this order:
    - expanded row with color from first significant row
    - a row of all zeros
    - expanded row with color from second significant row
    - a row of all zeros
4. **Build output:** create rows in the output using the order from step 3, repeating as necessary to create an output with the same dimensions as the input.
"""

import numpy as np

def get_significant_rows(grid):
    """Finds rows with exactly one non-zero color."""
    significant_rows = []
    for i, row in enumerate(grid):
        non_zeros = row[row != 0]
        if len(non_zeros) == 1:
            significant_rows.append((i, non_zeros[0]))
    return significant_rows

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    
    # Find significant rows (rows with only one non-zero color)
    significant_rows = get_significant_rows(input_grid)
    
    # Build the output pattern
    output_row_index = 0
    num_sig_rows = len(significant_rows)

    if num_sig_rows > 0:  # Handle cases with no significant rows
      pattern = []
      for _, color in significant_rows:
          pattern.append(np.full(input_grid.shape[1], color))  # Expanded row
          pattern.append(np.zeros(input_grid.shape[1], dtype=int)) # Zero row

      while output_row_index < output_grid.shape[0]:
            for row in pattern:
                if output_row_index < output_grid.shape[0]:
                    output_grid[output_row_index, :] = row
                    output_row_index += 1
                else:
                    break


    return output_grid
```
