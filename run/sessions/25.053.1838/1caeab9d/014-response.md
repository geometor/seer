# 1caeab9d • 014 • example_3 - CODE

---
```python
"""
1.  **Identify Objects:** Scan the input grid and identify contiguous blocks of pixels with the same color. Consider each of these blocks as a single object.
2.  **Check for Vertical Adjacency and Merge, or move down:** Iterate through the grid, focusing on vertically adjacent pixel pairs.
    *   If two vertically adjacent pixels have the same color, they stay.
    *   If at least one object in a row is not eliminated, the row should be moved down
3.  **Remove Top Row:** After processing vertical adjacency, remove the top-most row of the grid.
4. Ensure empty positions are the background color (0).
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rules."""

    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Check for Vertical Adjacency and move down if not adjacent
    for r in range(rows - 1):
      for c in range(cols):
        if output_grid[r,c] == output_grid[r+1, c]:
            continue
        else:
          if output_grid[r+1,c]!=0:
            output_grid[r+1,:]=0
            non_zero_indices = np.nonzero(output_grid[r,:])
            output_grid[r, 1:len(non_zero_indices[0])+1] = output_grid[r,non_zero_indices]
            output_grid[r,0]=0
            output_grid[r,len(non_zero_indices[0])+1:]=0

    # Remove Top Row
    output_grid = np.delete(output_grid, 0, axis=0)
    new_top_row = np.zeros((1, cols), dtype=int)
    output_grid = np.vstack([new_top_row, output_grid])

    return output_grid.tolist()
```
