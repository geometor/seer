# 6e02f1e3 • 005 • refine_coder

---
```python
"""
1.  **Check for Uniform Input:** If all pixels in the input grid have the same color, create an output grid where the top row is all 5s, and all other pixels are 0s.
2. **Cross Pattern**: Otherwise, create an output where any non-zero input produces a 5 and zeros are placed between to form a cross.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape
    
    # Check for uniform input
    first_pixel = input_grid[0, 0]
    if np.all(input_grid == first_pixel):
        output_grid[0, :] = 5
        return output_grid

    # Cross pattern
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                if r == c or r + c == rows -1:
                  output_grid[r,c] = 5
                elif r == (rows-1)//2 or c == (cols-1)//2:
                  output_grid[r,c] = 5

    return output_grid
```
