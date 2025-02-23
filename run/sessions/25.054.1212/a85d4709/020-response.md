# a85d4709 • 020 • example_4 • investigate_coder

---
```python
"""
Iterate through each pixel in the input grid.
If a pixel's value is 0 (white), change it to 4 (yellow) in the output grid.
If a pixel's value is 5 (gray), change it to 3 (green) in the output grid.
The size and shape of the grid does not change.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""

    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Get the dimensions of the input (and output) grid.
    rows, cols = input_grid.shape
        
    # Iterate through each pixel in the grid.
    for i in range(rows):
        for j in range(cols):
            # Apply the transformation rules based on the input pixel's value.
            if input_grid[i, j] == 0:
                output_grid[i, j] = 4
            elif input_grid[i, j] == 5:
                output_grid[i, j] = 3

    return output_grid
```

