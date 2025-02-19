# 3c9b0459 • 006 • example_3 - CODE

---
```python
"""
The transformation involves a color swap between red and blue, with one blue cell remaining unchanged. The azure cell changes color to blue and also changes its position.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by swapping colors between red and blue,
    keeping one blue cell unchanged, and changing azure to blue.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the color-swapping rules
            if input_grid[i, j] == 2:  # Red becomes blue
                output_grid[i, j] = 1
            elif input_grid[i, j] == 1:  # Blue becomes red, except at (1, 1)
                if i == 1 and j == 1:
                    output_grid[i,j] = 1
                else:
                    output_grid[i, j] = 2
            elif input_grid[i, j] == 8:  # Azure becomes blue
                output_grid[i, j] = 1

    # Move azure
    output_grid[2,1] = 0
    output_grid[0,1] = 8

    return output_grid
```

