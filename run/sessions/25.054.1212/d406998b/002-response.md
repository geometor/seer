# d406998b • 002 • example_1 • investigate_coder

---
```python
"""
Transform the input grid by selectively replacing '5' (gray) pixels with '3' (green) pixels based on their position within each row and relative to other '5' pixels. '0' (white) pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each row.
    for i in range(rows):
        # Row 1: Change from the right.
        if i == 0:
          fives = np.where(output_grid[i] == 5)[0]
          if len(fives) > 0:
            output_grid[i, fives[-1]] = 3  #change last five to a three
          if len(fives) > 1:
            output_grid[i, fives[-3] if len(fives) > 2 else fives[-2]]  = 3
        # Row 2: Change from the left.
        elif i == 1:
          fives = np.where(output_grid[i] == 5)[0]
          if len(fives) > 0:
            output_grid[i, fives[1] if len(fives) > 1 else fives[0] ] = 3
          if len(fives) > 2:
            output_grid[i, fives[3] if len(fives) > 3 else fives[2]] = 3

        # Row 3: No changes.
        elif i == 2:
          fives = np.where(output_grid[i] == 5)[0]
          if len(fives) > 1:
            output_grid[i, fives[1]] = 3

    return output_grid
```
