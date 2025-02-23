# 1e0a9b12 • 002 • example_1 • investigate_coder

---
```python
"""
Identify all non-zero elements in the input grid. Move these non-zero elements to the last row of the output grid, maintaining their original order from left to right, top to bottom as they appeared in the input. Fill all other cells of the output grid with zeros.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid, then filled with zeros.
    output_grid = np.zeros_like(input_grid)
    
    # Flatten the input grid and filter out the zero elements
    non_zero_elements = input_grid[input_grid != 0]

    # Place the non_zero elements in the last row of the output grid.
    output_grid[-1, :len(non_zero_elements)] = non_zero_elements
    
    return output_grid
```
