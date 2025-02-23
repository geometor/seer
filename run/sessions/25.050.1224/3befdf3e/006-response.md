# 3befdf3e • 006 • example_3 - CODE

---
```python
"""
The transformation consists of two actions: the blue square transforms into a hollow blue square with a frame and the green rectangle changes its shape, in a complex mode.
"""
import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the blue object
    blue_coords = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 1:
                blue_coords.append((r, c))

    # Expand the blue object into hollow shape
    if blue_coords:
      min_br = min(r for r,c in blue_coords)
      max_br = max(r for r,c in blue_coords)
      min_bc = min(c for r,c in blue_coords)
      max_bc = max(c for r,c in blue_coords)

      for r in range(min_br -1, max_br+2):
        for c in range(min_bc-1, max_bc + 2):
          if 0<= r < rows and 0 <= c < cols:
            if r == min_br -1 or r == max_br + 1 or c == min_bc -1 or c == max_bc+1:
              output_grid[r,c] = 1

    # find green object
    green_coords = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r,c] == 3:
              green_coords.append((r,c))
    if green_coords:
      min_gr = min(r for r, c in green_coords)
      max_gr = max(r for r, c in green_coords)
      min_gc = min(c for r, c in green_coords)
      max_gc = max(c for r, c in green_coords)
      # copy first and last rows
      for c in range(min_gc, max_gc+1):
        if min_gr > 0:
            output_grid[min_gr-1, c] = 3
        if max_gr < rows -1:
            output_grid[max_gr+1,c] = 3
      # add columns
      for r in range(min_gr-1, max_gr + 2):
          if 0 <= r < rows:
              if min_bc>1:
                  output_grid[r,min_bc-2] = 3
              if max_bc < cols -2:
                  output_grid[r,max_bc+2] = 3
              if min_gc>0:
                  output_grid[r,min_gc-1]=3
              if max_gc < cols-1:
                  output_grid[r, max_gc+1] = 3



    return output_grid
```

