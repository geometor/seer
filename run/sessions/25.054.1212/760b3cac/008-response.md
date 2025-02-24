# 760b3cac • 008 • example_2 • investigate_coder

---
```python
"""
The azure region in the top half of the grid expands horizontally within its original rows, filling available white space, but is blocked by other colored blocks. The yellow region does not change.
"""

import numpy as np

def get_azure_region(grid):
    """
    Identifies the azure (8) region in the top half of the grid.
    Returns a list of (row, col) tuples for azure pixels.
    """
    rows, cols = grid.shape
    azure_pixels = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 8:
                azure_pixels.append((r, c))
    return azure_pixels

def expand_horizontally(grid, azure_pixels):
    """
    Expands the azure region horizontally, filling white (0) pixels.
    """
    output_grid = np.copy(grid)
    rows_processed = set()
    
    for r, c in azure_pixels:
        if r in rows_processed:
            continue  # avoid expanding rows twice

        #get start and stop for this continuous block
        
        rows_processed.add(r)

        # Expand left
        c_left = c
        while c_left > 0 and output_grid[r, c_left - 1] == 0:
            c_left -= 1
            output_grid[r, c_left] = 8

        # Expand Right
        c_right = c
        while c_right < output_grid.shape[1] - 1 and output_grid[r, c_right + 1] == 0 :
            c_right += 1
            output_grid[r,c_right] = 8
        
        # find the start and end of connected component on this row
        c_current = c
        while c_current > 0 and output_grid[r,c_current-1] == 8:
          c_current = c_current - 1

        while c_current < output_grid.shape[1] - 1 and output_grid[r,c_current] == 8:
            output_grid[r,c_current] = 8
            c_current += 1
            

    return output_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # get azure pixels
    azure_pixels = get_azure_region(output_grid)
    
    # expand azure horizontally
    output_grid = expand_horizontally(output_grid, azure_pixels)

    return output_grid
```
