# 0a938d79 • 026 • example_4 - CODE

---
```python
"""
1.  **Identify Significant Rows:** Scan the input grid to find rows that contain exactly one non-zero (non-white) color value, and the rest are zeros.
2.  **Expand Rows:** For each significant row found, expand the single non-zero color to fill the entire row.
3. **Create Pattern**: Copy rows from top to bottom, replicating the row below the single color row twice, and repeating the pattern to the bottom of the grid.
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
        
    # Create pattern
    for row_index, color in significant_rows:
      output_grid[row_index, :] = color #expand color to whole row

    # start pattern from top of grid
    pattern_start = 0

    for row_index, color in significant_rows:

        # copy the row to the output grid and the rows below according to the pattern
        output_grid[pattern_start,:] = color

        if pattern_start + 1 < output_grid.shape[0]:
             output_grid[pattern_start+1,:] = color
        
        if pattern_start + 2 < output_grid.shape[0]:
            output_grid[pattern_start + 2, :] = output_grid[row_index + 1 if row_index + 1 < input_grid.shape[0] else row_index,:]

        pattern_start +=3

    return output_grid
```
