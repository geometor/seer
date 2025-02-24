# 93b581b8 • 004 • refine_coder

---
```python
"""
1.  **Identify the Central Block:** Find the 2x2 block of non-zero pixels in the input grid. This block is guaranteed to be present.

2.  **Top Extension**:
    *   Copy the *top row* of the 2x2 central block to the *top two rows* of the output grid.  This copied row forms the first two rows of the entire output.

3.  **Bottom Extension**:
    *   Copy the *bottom row* of the 2x2 central block to the *bottom two rows* of the output grid. This copied row forms the last two rows of the output.

4.  **Preserve Center:** The original 2x2 central block from the input remains unchanged at the same location in the output grid.

5. **Leave Blank:** All other spaces that are not the top two rows, bottom two rows, or central 2x2 block are zero filled.
"""

import numpy as np

def find_central_block(grid):
    # Find the bounding box of non-zero elements
    rows, cols = np.where(grid != 0)
    if len(rows) == 0:  # Handle empty grid case
        return None
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)

    # Check if it's a 2x2 block
    if max_row - min_row == 1 and max_col - min_col == 1:
        return (min_row, min_col, max_row, max_col)
    else:
        return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the central 2x2 block
    central_block_coords = find_central_block(input_grid)
    if central_block_coords is None:
        return output_grid # Return original grid if central block not present (should not happen, based on the task)

    min_row, min_col, max_row, max_col = central_block_coords

    # Top Extension: Copy top row of central block to first two rows of output
    output_grid[0:2, :] = input_grid[min_row, min_col:max_col+1]

    # Bottom Extension: Copy bottom row of central block to last two rows of output
    output_grid[rows-2:rows, :] = input_grid[max_row, min_col:max_col+1]

    # Preserve Center: Copy central block
    output_grid[min_row:max_row+1, min_col:max_col+1] = input_grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid
```
