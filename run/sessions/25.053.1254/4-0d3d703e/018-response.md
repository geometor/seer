# 4-0d3d703e • 018 • example_3 - CODE

---
```python
"""
Transforms a 3x3 grid by applying a color mapping. Gray (5) becomes blue (1), 
azure (8) becomes maroon (9), and the last column is unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through rows
    for i in range(rows):
        # Iterate through columns, stopping before the last column
        for j in range(cols - 1):
            # Color Substitution
            if input_grid[i, j] == 5:  # If gray
                output_grid[i, j] = 1  # Change to blue
            elif input_grid[i, j] == 8:  # If azure
                output_grid[i, j] = 9  # Change to maroon

    return output_grid
```
