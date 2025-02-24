# 99b1bc43 • 002 • example_1 • investigate_coder

---
```python
"""
The input grid of 9 rows and 4 columns is transformed into an output grid of 4 rows x 4 columns by:
1. Taking sections of the input of 2 rows at a time.
2. If a 2-row section only contains 0s (and 1s), it's output is white.
3.  If an input row is all the same non-zero color, it becomes all green.
4. Two rows of mixed 0 and non-zero become all green
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((4, cols), dtype=int)

    # Process the first four rows (two 2-row sections)
    for i in range(2):
        subgrid = input_grid[i*2:i*2+2, :]
        unique_colors = np.unique(subgrid)
        if all(color in [0, 1] for color in unique_colors):
            output_grid[i, :] = 0  # Output white
        
    # process row 5
    unique_colors = np.unique(input_grid[4,:])
    if len(unique_colors) == 1 and unique_colors[0] != 0:
      output_grid[2,:] = 3

    # process rows 6&7 and 8&9
    for i in range(2):
      subgrid = input_grid[5 + i*2:5 + i*2 + 2,:]
      unique_colors = np.unique(subgrid)
      if any(color != 0 for color in unique_colors):
        output_grid[3,:] = 3

    return output_grid.tolist()
```
