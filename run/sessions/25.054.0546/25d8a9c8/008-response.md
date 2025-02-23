# 25d8a9c8 • 008 • example_2 • investigate_coder

---
```python
"""
The transformation rule appears to perform a color replacement. Examine the input grid. If a pixel is orange (7) or green (3), change it to white (0). If a pixel is magenta (6), change it to gray (5). All other colors, if any, remain unchanged, although, in this example, only these three colors are present. The position of the pixels within the grid does not appear to affect the color changes.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid with the same dimensions as the input
    output_grid = np.copy(input_grid)

    # Iterate through each pixel in the grid
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the color replacement rules
            if output_grid[i, j] == 7 or output_grid[i, j] == 3:
                output_grid[i, j] = 0  # Change orange and green to white
            elif output_grid[i, j] == 6:
                output_grid[i, j] = 5  # Change magenta to gray

    return output_grid
```
