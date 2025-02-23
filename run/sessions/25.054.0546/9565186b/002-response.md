# 9565186b • 002 • example_1 • investigate_coder

---
```python
"""
Iterate through each pixel in the input grid.  If a pixel is red (2), it remains red in the output. If a pixel is blue (1) or azure (8), it becomes gray (5) in the output.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each pixel in the grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the color transformation rules.
            if output_grid[i, j] == 2:
                continue  # Red remains red.
            elif output_grid[i, j] == 1 or output_grid[i, j] == 8:
                output_grid[i, j] = 5  # Blue and azure become gray.

    return output_grid
```
