# 1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
1.  **Identify Key Pixels:** In the input grid, identify pixels with the values 1, 4, 6, and 9.

2.  **Preserve Key Pixels values and position:**
    Copy the values of the pixels from the last row into the output, at their respective position

3. **Remove other position:** Remove the non key pixels from the first, second and third rows.

4.  **Rearrange Zeroes:**
Fill the remaining cells of the output grid with zeros.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with zeros and same dimensions as input.
    output_grid = np.zeros_like(input_grid)

    # Get the dimensions of the input grid
    rows, cols = input_grid.shape
    
    # Iterate through the last row to preserve relevant pixels
    for c in range(cols):
      output_grid[rows-1, c] = input_grid[rows-1, c]

    # copy any cell in row 3 with any of 1,4,6,9
    for r in range(rows):
       for c in range(cols):
          if input_grid[r,c] in [1,4,6,9]:
             output_grid[3,c] = input_grid[r,c]
    
    return output_grid
```
