# cf98881b • 012 • refine_coder

---
```python
"""
1. **Identify the Cropping Region:**
    *   Examine the input grid.
    *   Locate a column within the input grid where the red pixels (value 2) form a contiguous vertical line of four.
    *   The top-left coordinate of the 4x4 cropping region is set such that this column of red pixels is included within the region.
    *   If multiple such regions exist, this rule alone is insufficient to define the correct region.

2. **Crop:** Extract the 4x4 sub-grid from the input grid, starting at the identified (row, col) coordinates.

3. **Color Substitution:** Within the cropped 4x4 region:
    *   Change all pixels with the value `2` (red) to `1` (blue).
    *   Leave all other pixels unchanged.
"""

import numpy as np

def find_red_column(input_grid):
    """Finds the column index containing a contiguous vertical line of four red pixels (value 2)."""
    grid = np.array(input_grid)
    rows, cols = grid.shape
    for j in range(cols):
        for i in range(rows - 3):
            if grid[i:i+4, j].tolist() == [2, 2, 2, 2]:
                return i, j  # Return row and column of the top of the red column
    return None  # Return None if no such column is found

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Find the starting coordinates of the cropping region based on red column
    red_coords = find_red_column(input_grid)

    if red_coords:
        start_row, start_col = red_coords
          # Ensure the 4x4 crop stays within bounds.
        start_row = max(0, min(start_row, input_grid.shape[0] - 4))
        start_col = max(0, min(start_col, input_grid.shape[1] - 4))
    else:
        start_row, start_col = 0, 0  #default to 0,0



    # Crop the 4x4 region
    cropped_grid = input_grid[start_row:start_row+4, start_col:start_col+4]

    # Apply color substitution within the cropped region
    output_grid = np.copy(cropped_grid)  # Work on a copy
    output_grid[output_grid == 2] = 1

    return output_grid.tolist()
```
