# b8cdaf2b • 014 • example_3 • investigate_coder

---
```python
"""
Copies the bottom two rows of the input grid to the output grid.
Fills the top two rows of the output grid with white pixels (0).
Replaces, in the third row, white color by blue color for those position where was white in the top three rows.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Fill the top two rows with white (0)
    output_grid[:2, :] = 0

    # Fill the third row from the top with 0
    output_grid[2,:] = 0

    # Find the coordinates of 0 in the top three rows of original input
    coords = np.where(input_grid[:3,:] == 0)

    # Sets to blue only if exist at least one white in the first three rows
    if (len(coords[0])>0):
      output_grid[2,coords[1][0]] = 1
      output_grid[2,coords[1][-1]] = 1

    return output_grid
```
