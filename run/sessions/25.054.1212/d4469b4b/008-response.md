# d4469b4b • 008 • example_2 • investigate_coder

---
```python
"""
The transformation rule involves reducing a 5x5 grid to a 3x3 grid by focusing on the central 3x3 region. 
Within this region, color 1 (blue) is mapped to color 5 (gray), while color 0 (white) remains unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize a 3x3 output grid filled with zeros (white).
    output_grid = np.zeros((3, 3), dtype=int)

    # Extract the central 3x3 subgrid from the input.
    subgrid = input_grid[1:4, 1:4]

    # Iterate through the subgrid and apply the color mapping.
    for i in range(3):
        for j in range(3):
            if subgrid[i, j] == 1:
                output_grid[i, j] = 5
            else:
                output_grid[i,j] = subgrid[i,j] # added to handle edge cases.

    return output_grid
```
