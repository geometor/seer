# 6ecd11f4 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify the target region:** Locate the 3x3 multi-colored region at the bottom section of the input grid, ignoring all pixels above.
2.  **Extract the colors:** Extract each pixel's color from the target region.
3.  **Create the output grid and Arrange:** Construct a 3x3 output grid. Fill this grid with the corresponding pixel's color.
"""

import numpy as np

def find_multicolored_region(grid):
    # Find the 3x3 region with various colors in it at the bottom of the input
    rows, cols = grid.shape
    for r in range(rows - 2):
        for c in range(cols -2):
            subgrid = grid[r:r+3, c:c+3]
            if np.unique(subgrid).size > 1 and subgrid.min() != subgrid.max() :
                 return r,c
    return None
def transform(input_grid):
    """Transforms the input grid by extracting a 3x3 multicolored region."""
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Find the multicolored 3x3 region
    start_row, start_col = find_multicolored_region(input_grid)

    # Extract the region
    output_grid = input_grid[start_row:start_row+3, start_col:start_col+3].copy()

    return output_grid.tolist()
```
