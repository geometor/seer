# fafffa47 • 012 • refine_coder

---
```python
"""
Transforms the top half of the input grid to a 3x3 output grid, mapping maroon (9) to red (2) and white(0) to white(0). The positions of red pixels in the output are determined by the presence of maroon pixels in the first/last rows and first/last columns of the top half of the input.
"""

import numpy as np

def transform(input_grid):
    # Initialize a 3x3 output grid filled with zeros (white).
    output_grid = np.zeros((3, 3), dtype=int)
    input_height = input_grid.shape[0]
    input_width = input_grid.shape[1]
    top_half_height = input_height // 2

    # Get the top half of the input grid.
    top_half = input_grid[:top_half_height, :]

    # Determine output positions based on maroon presence in top half boundaries.
    for i in range(3):
        for j in range(3):
            #check for first row presence
            if i == 0 and np.any(top_half[0,:] == 9):
                output_grid[i,j] = 2 if np.any(top_half[0,j] == 9) else output_grid[i,j]
            #check for last row presence in top half
            if i==2 and np.any(top_half[top_half_height -1, :] == 9 ):
                output_grid[i,j] = 2 if np.any(top_half[top_half_height-1,j] == 9) else output_grid[i,j]
            #check for first col presence
            if j==0 and np.any(top_half[:,0] == 9):
                output_grid[i,j] = 2 if np.any(top_half[i,0] == 9) and i<top_half_height else output_grid[i,j]
            #check for last col presence
            if j==2 and np.any(top_half[:,input_width-1] == 9):
                output_grid[i,j] = 2 if np.any(top_half[i,input_width-1] == 9) and i < top_half_height else output_grid[i,j]
            if top_half[i,j] == 0 and i < top_half_height:
                output_grid[i,j] = 0

    return output_grid
```
