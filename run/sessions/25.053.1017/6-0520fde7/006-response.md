# 6-0520fde7 • 006 • example_3 - CODE

---
```python
"""
1.  **Remove the Central Column:** Delete the entire central column (column index 3, 0-indexed) of the input grid, which consists of gray (5) pixels.
2.  **Remove Columns:** remove one more column of pixels to the left of the original central column, and two columns of pixels from the right of the original central column.
3.  **Change Blue to Red:** In the remaining grid, any pixel that had color 1(blue) becomes color to 2 (red) in the output.
4.  **Retain Whites:** white (0) colored pixels are not changed.
"""

import numpy as np

def transform(input_grid):
    # Create a copy of the input grid as a NumPy array.  We'll modify this copy.
    output_grid = np.copy(input_grid)

    # 1. Remove the central column (index 3).
    output_grid = np.delete(output_grid, 3, axis=1)
    
    # 2. Remove additional columns
    output_grid = np.delete(output_grid, 2, axis=1)
    output_grid = np.delete(output_grid, 3, axis=1)
    output_grid = np.delete(output_grid, 3, axis=1)


    # 3. Change blue (1) to red (2).
    output_grid[output_grid == 1] = 2

    return output_grid
```
