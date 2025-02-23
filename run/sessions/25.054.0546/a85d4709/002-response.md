# a85d4709 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation replaces '0' (white) values in the input grid based on their position. '5' (gray) values are ignored. '0' values on the top-left to bottom-right diagonal are replaced as follows: top-left '0' becomes '3' (green), center '0' becomes '4' (yellow), and bottom-right '0' becomes '2' (red).
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # iterate through the grid
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # check if the current value is 0
            if output_grid[i, j] == 0:
                # check if the current position is on the top-left to bottom-right diagonal
                if i == j:
                    # replace based on position on the main diagonal
                    if i == 0:
                        output_grid[i, j] = 3  # Top-left
                    elif i == 1:
                        output_grid[i, j] = 4  # Center
                    elif i == 2:
                        output_grid[i, j] = 2  # Bottom-right

    return output_grid
```

