# 017c7c7b • 008 • example_2 • investigate_coder

---
```python
"""
The transformation rule is to identify the checkerboard pattern of white (0) and blue (1) pixels in the input grid, 
substitute all blue (1) pixels with red (2) pixels, repeat the pattern vertically, and maintain the white (0) pixels unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid based on input grid dimensions.  We'll vertically extend it later.
    output_grid = np.copy(input_grid)

    # Substitute blue (1) with red (2).
    output_grid[output_grid == 1] = 2
    
    # Calculate how many rows to add to output grid for the extra repetition.
    rows_to_add = output_grid.shape[0] // 2

    # add rows
    new_rows = output_grid[:rows_to_add, :]    
    output_grid = np.concatenate((output_grid, new_rows))
    
    return output_grid
```
