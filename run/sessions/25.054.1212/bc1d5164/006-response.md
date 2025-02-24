# bc1d5164 • 006 • refine_coder

---
```python
"""
Extracts the inner region of a grid, excluding a single-pixel-wide rectangular frame of a uniform color.
"""

import numpy as np

def find_frame_color(grid):
    # Find the color that forms the outermost rectangular frame.

    rows, cols = grid.shape
    for color in np.unique(grid):
        if color == 0:
          continue
        coords = np.argwhere(grid == color)
        min_row, min_col = coords.min(axis=0)
        max_row, max_col = coords.max(axis=0)

        # Check if it forms a rectangle
        if (max_row - min_row + 1) * (max_col - min_col + 1) == len(coords):
          
          # Check it is actually a frame by looking for different values inside
          is_frame = False
          for r in range(min_row + 1, max_row):
            for c in range(min_col + 1, max_col):
              if grid[r,c] != color:
                is_frame = True
                break
            if is_frame:
              break
          
          if is_frame:
            return color

    return 0 # should never reach here if there is a valid frame

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
    Extracts the inner region of the grid, excluding the frame.
    """
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Find the framing color
    frame_color = find_frame_color(input_grid)
    if frame_color == 0:
      return []

    # Get bounding box
    bounding_box = get_bounding_box(input_grid, frame_color)
    if bounding_box is None:
        return []
    
    min_row, min_col, max_row, max_col = bounding_box

    # Extract inner region
    output_grid = input_grid[min_row+1:max_row, min_col+1:max_col]
    
    return output_grid.tolist()
```
