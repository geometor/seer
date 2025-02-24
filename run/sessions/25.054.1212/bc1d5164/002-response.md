# bc1d5164 • 002 • example_1 • investigate_coder

---
```python
"""
Extracts a subgrid from the input grid, defined by the outermost azure (8) pixels.
"""

import numpy as np

def get_bounding_box(grid, color):
    # Find coordinates of all pixels of the specified color.
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None  # Handle cases where the color doesn't exist
    min_row, min_col = coords.min(axis=0)
    max_row, max_col = coords.max(axis=0)
    return (min_row, min_col, max_row, max_col)

def transform(input_grid):
    """
    Extracts the subgrid defined by azure frame.
    """
    # Convert input to numpy array for easier manipulation
    input_grid = np.array(input_grid)

    # Get the bounding box defined by the azure pixels.
    bounding_box = get_bounding_box(input_grid, 8)
    if bounding_box is None:
      return []

    min_row, min_col, max_row, max_col = bounding_box

    # Extract the subgrid.
    output_grid = input_grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid.tolist()
```
