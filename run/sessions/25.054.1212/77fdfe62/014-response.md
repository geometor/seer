# 77fdfe62 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation rule involves extracting the colors from the four corners of a blue (1) frame within the input grid and using these colors to populate a smaller 4x4 output grid. Each corner color of the input's blue frame corresponds to a 2x2 block in the output grid. The remaining cells in the output grid are filled with white (0).
"""

import numpy as np

def get_frame_corners(grid):
    # Find the outermost blue (1) frame.  We assume it's a single-pixel wide frame.
    rows, cols = grid.shape
    top_left = None
    top_right = None
    bottom_left = None
    bottom_right = None

    # Find top-left
    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == 1:
                top_left = (r,c)
                break
        if top_left:
            break

    #Find other coners based on knowledge that it is rectangular and 1 pixel wide
    if top_left:
      for r in range(rows):
        for c in range(cols):
          if grid[r,c] == 1:
            if r == top_left[0] and c > top_left[1]:
                top_right = (r,c)
            if c == top_left[1] and r > top_left[0]:
                bottom_left = (r, c)
            if bottom_left and top_right and r > top_left[0] and c > top_left[1] and grid[r, c] ==1:
                bottom_right = (r, c)
    return top_left, top_right, bottom_left, bottom_right
            

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""

    # Get the corner coordinates of the blue frame
    top_left, top_right, bottom_left, bottom_right = get_frame_corners(input_grid)

    # Extract corner colors from input
    corner_colors = {
        'top_left': input_grid[top_left[0]-1, top_left[1]-1],
        'top_right': input_grid[top_right[0]-1, top_right[1]+1],
        'bottom_left': input_grid[bottom_left[0]+1, bottom_left[1]-1],
        'bottom_right': input_grid[bottom_right[0]+1, bottom_right[1]+1]
    }


    # Initialize the output grid (4x4)
    output_grid = np.zeros((4, 4), dtype=int)

    # Populate the output grid
    output_grid[0:2, 0:2] = corner_colors['top_left']  # Top-left quadrant
    output_grid[0:2, 2:4] = corner_colors['top_right'] # Top-right quadrant
    output_grid[2:4, 0:2] = corner_colors['bottom_left'] # Bottom-left quadrant
    output_grid[2:4, 2:4] = corner_colors['bottom_right'] # Bottom-right quadrant
    
    return output_grid
```
