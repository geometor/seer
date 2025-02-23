# a64e4611 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation overlays a green (3) cross shape onto the existing background grid. The background grid consists
of azure (8) and white (0) pixels. The cross shape is centered on the grid.
"""

import numpy as np

def find_background(grid):
    # simple function to find the most prevalent colors to ignore
    # in this case return the two most freqent color, which will be ignored as background.
    unique, counts = np.unique(grid, return_counts=True)
    # sort to put most frequent colors at the end
    return unique[np.argsort(counts)][-2:]

def create_cross(grid, cross_color=3):
    # initialize cross grid based on size of input_grid
    rows, cols = grid.shape
    cross = np.zeros_like(grid)

    background_colors = find_background(grid)
    
    # find center row, col
    center_row = rows // 2
    center_col = cols // 2

    # Determine a reasonable thickness, this may need further refinement
    thickness = 1
    if rows>15:
        thickness = 3
    elif rows > 25:
        thickness = 5
    # else:
    #   thickness = 1

    # vertical part of the cross - starting at center row, and based on thickness 
    cross[center_row-thickness:center_row+thickness+1, :] = cross_color

    # horizontal part of cross - start at center col
    cross[:, center_col-thickness:center_col+thickness+1] = cross_color

    return cross

def transform(input_grid):
    """
    Overlays a green cross shape onto the input grid.
    """
    # initialize output_grid as copy of input
    output_grid = input_grid.copy()

    # create cross based on the input_grid size
    cross = create_cross(input_grid)
    
    background_colors = find_background(input_grid)

    # overlay
    for r in range(output_grid.shape[0]):
      for c in range(output_grid.shape[1]):
        if cross[r][c]!=0:
          output_grid[r,c] = cross[r,c]
    
    return output_grid
```
