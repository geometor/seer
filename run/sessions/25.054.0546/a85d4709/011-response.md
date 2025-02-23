# a85d4709 • 011 • refine_coder

---
```python
"""
If gray pixels in input have different x and y, then
  gray(x,y) => green(x,y) if y = x + 1
  gray(x,y) => yellow(x,y) if x == y
  gray(x,y) => red(x,y) if y = x-1 OR y = x - 2
if gray pixels in input are in the same column, then always map to green.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    gray_positions = np.argwhere(input_grid == 5)
    
    # if all gray pixels are in same column, map to green
    if len(gray_positions) > 0:
      if all(pos[1] == gray_positions[0][1] for pos in gray_positions):
          output_grid[:] = 3
          return output_grid

    # change output pixels 
    for x, y in gray_positions:
        if y == x + 1:
            output_grid[x, y] = 3
        elif x == y:
            output_grid[x, y] = 4
        elif y == x - 1 or y == x - 2:
            output_grid[x, y] = 2

    return output_grid
```
