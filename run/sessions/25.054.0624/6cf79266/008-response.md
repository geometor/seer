# 6cf79266 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify the Target Region:** Locate a region on the grid where the original color is white. It seems to be a 3x3 shaped region on the left, vertically centered.
2.  **Change Color:** Change the color of the internal 3x3 pixels of that region to blue (1).
3. **Preserve other pixels**: All other pixels keep the colors from the input to the output.
"""

import numpy as np

def find_white_region(grid):
    # Find contiguous white regions
    rows, cols = grid.shape
    for r in range(rows - 2):
        for c in range(cols -2):
            if grid[r, c] == 0 and grid[r+1,c] == 0 and grid[r+2, c] == 0:
                if  grid[r, c+1] == 0 and grid[r+1,c+1] == 0 and grid[r+2, c+1] == 0:
                    if  grid[r, c+2] == 0 and grid[r+1,c+2] == 0 and grid[r+2, c+2] == 0:

                        return (r,c)
    return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the target region
    region_start = find_white_region(input_grid)

    if region_start:
      # Change color of the 3x3 region to blue
      for r in range(region_start[0], region_start[0] + 3):
          for c in range(region_start[1], region_start[1] + 3):
              if output_grid[r,c] == 0:
                output_grid[r, c] = 1

    return output_grid
```
