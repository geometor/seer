# 5-150deff5 • 002 • Response

---

*text:*

```python
"""
The transformation rule identifies a single connected gray (color 5) object in the input grid. This object is then divided into two parts based on the main diagonal of its bounding box. The upper-left part, above or on the diagonal (excluding the last row of the bounding box ), is colored azure (8). The bottom-right part, below the diagonal (excluding the top row of the bounding box), is colored red (2). Cells outside the gray object remain unchanged (color 0).
"""

import numpy as np

def get_bounding_box(grid, color):
    """
    Returns the bounding box of the object with the specified color.
    """
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find the gray object (color 5)
    bounding_box = get_bounding_box(input_grid, 5)
    if bounding_box is None:
        return output_grid

    (min_row, min_col), (max_row, max_col) = bounding_box

    # Iterate through the gray object's cells
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if input_grid[r, c] == 5:
                # Determine if the cell is above/on or below the diagonal
                # Adjust row and col relative to the bounding box's top-left
                rel_row = r - min_row
                rel_col = c - min_col

                if rel_row < (max_row - min_row +1 ) and rel_col <= (max_col-min_col) and rel_row <= rel_col:
                  output_grid[r,c] = 8
                elif rel_row > 0 and rel_col < (max_col - min_col+1) and rel_row > rel_col:
                    output_grid[r, c] = 2

    return output_grid
```
