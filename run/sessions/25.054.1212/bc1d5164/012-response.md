# bc1d5164 • 012 • refine_coder

---
```python
"""
1.  **Find Bounding Rectangle:** Identify the smallest rectangle that encloses all non-zero (non-white) pixels in the input grid. This is done by finding the minimum and maximum row and column indices of the non-zero pixels.
2.  **Extract 3x3 Subgrid:** Extract a 3x3 subgrid from the input grid. The top-left corner of this subgrid corresponds to the top-left corner of the bounding rectangle found in step 1.
3.  **Create Output:** The extracted 3x3 subgrid is the output.  If the input has all zeros, return 3x3 all zero grid.
"""

import numpy as np

def find_bounding_rectangle(input_grid):
    """Finds the top-left corner of the bounding rectangle of non-zero pixels."""
    rows, cols = input_grid.shape
    min_row, min_col = rows, cols
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                min_row = min(min_row, r)
                min_col = min(min_col, c)
    if min_row == rows or min_col == cols:  # Handle all-zero case
        return None, None
    return min_row, min_col

def transform(input_grid):
    """Transforms the input grid to the output grid."""
    input_grid = np.array(input_grid)
    min_row, min_col = find_bounding_rectangle(input_grid)

    # Handle all-zero input case
    if min_row is None or min_col is None:
        return np.zeros((3, 3), dtype=int).tolist()

    # Extract 3x3 subgrid
    output_grid = input_grid[min_row:min_row + 3, min_col:min_col + 3].copy()

    # Ensure output is 3x3, padding with zeros if necessary. This handles
    # cases where the bounding rect is near the edge of the input grid.
    rows, cols = output_grid.shape
    if rows < 3 or cols < 3:
        padded_grid = np.zeros((3, 3), dtype=int)
        padded_grid[:rows, :cols] = output_grid
        output_grid = padded_grid

    return output_grid.tolist()
```
