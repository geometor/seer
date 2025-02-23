# ff805c23 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation extracts a 5x5 subgrid from the upper-right corner of the input grid. 
The subgrid contains only 0 and 5 values.
"""

import numpy as np

def find_target_region(input_grid, size):
    # Find the top-right 5x5 region of the input
    rows, cols = input_grid.shape
    start_row = 0
    start_col = cols - size
    return start_row, start_col


def transform(input_grid):
    """
    Extracts a 5x5 subgrid from the upper-right corner of the input grid.
    """
    # Convert input grid to a NumPy array
    input_grid = np.array(input_grid)
        
    # Find the starting coordinates of target region
    size = 5
    start_row, start_col = find_target_region(input_grid, size)
    
    # Extract the subgrid
    output_grid = input_grid[start_row:start_row+size, start_col:start_col+size]

    return output_grid.tolist()
```
