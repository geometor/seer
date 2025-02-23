# 0a938d79 • 028 • refine_coder

---
```python
"""
1.  **Identify Significant Rows:** Scan the input grid to find rows that contain exactly one non-zero (non-white) color value, with all other values in that row being zero (white).
2.  **Expand Significant Rows:** For each "significant row" found, expand the single non-zero color to fill the entire row.
3.  **Build the output:**
   - determine order of the identified colors from significant rows, from
     top to bottom
    - create an output grid of the same dimensions as the input
    - interleave the identified rows in the original order with rows of all
      zeros, repeating this to the bottom of the grid
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
    
    # Expand significant rows and build the output pattern
    output_row_index = 0
    num_sig_rows = len(significant_rows)

    while output_row_index < output_grid.shape[0]:
        for i in range(num_sig_rows):
            # fill the row with expanded color
            color = significant_rows[i][1]

            if output_row_index < output_grid.shape[0]:
                output_grid[output_row_index, :] = color
                output_row_index += 1

            # interleave with a row of zeros
            if output_row_index < output_grid.shape[0]:
                output_row_index += 1

    return output_grid
```
