# 2dee498d • 002 • example_1 • investigate_coder

---
```python
"""
The transformation extracts a 3x3 sub-grid from the input grid. 
The sub-grid represents every other element along the width of the input grid, 
maintaining the relative positions of colors.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a 3x3 sub-grid from the input grid, taking every other element on x axis.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, (cols+1)//2), dtype=int)

    # Iterate through the input grid and select every other column.
    
    for i in range(rows):
        for j in range(0,cols,2):
            output_grid[i, j//2] = input_grid[i, j]

    return output_grid.tolist()
```
