# bc1d5164 • 004 • refine_coder

---
```python
"""
Extracts a subgrid from the input grid, defined by the outermost pixels of a single color forming a rectangular frame.
"""

import numpy as np

def find_frame_color(grid):
    # Check the color of the top-left pixel.
    #  Iterate to find the frame.
    rows, cols = grid.shape
    
    # Find top-left non-zero pixel - this is not correct but captures the essence
    for r in range(rows):
      for c in range(cols):
          if grid[r,c] != 0:
              return grid[r,c]
    return 0 #should never reach here

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
    Extracts the subgrid defined by the frame.
    """
    # Convert input to numpy array for easier manipulation
    input_grid = np.array(input_grid)

    # Find the framing color
    frame_color = find_frame_color(input_grid)
    if frame_color == 0:
       return []

    # Get the bounding box defined by the frame pixels.
    bounding_box = get_bounding_box(input_grid, frame_color)
    if bounding_box is None:
      return []

    min_row, min_col, max_row, max_col = bounding_box

    # Extract the subgrid.
    output_grid = input_grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid.tolist()
```
