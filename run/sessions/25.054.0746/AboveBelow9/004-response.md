# AboveBelow9 • 004 • refine_coder

---
```python
"""
The transformation rule is to remove all green pixels (value 3) except those on the top row, 
replacing them with black pixels (value 0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by removing all green pixels (value 3) 
    except for those present on the top row (row index 0).
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through the input grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Check if the pixel is green (value 3).
            if output_grid[i, j] == 3:
                # Check if the pixel is NOT on the top row (row index 0).
                if i != 0:
                    # Change the green pixel to black (value 0).
                    output_grid[i, j] = 0

    return output_grid
```

