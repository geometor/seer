# d406998b • 010 • refine_coder

---
```python
"""
Transforms a grid by changing specific gray pixels to green based on their position and row, skipping adjacent pixels.

The transformation follows these rules:
- Gray pixels (5) are changed to green pixels (3).
- The transformation occurs row by row.
- Within each row:
 - If row 1: If a gray pixel changes to green, skip the adjacencies
 - If row 2: Only one gray pixel, if any, changes to green
 - If row 3: If gray pixels change to green, and there are exactly three changes, they can't be adjacent
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each row
    for i in range(rows):
        gray_indices = [j for j in range(cols) if output_grid[i, j] == 5]
        
        if i == 0:
            # First row: alternate gray pixels, skipping adjacencies
            changed_indices = []
            for j in gray_indices:
              if not any(abs(j - k) <= 1 for k in changed_indices):
                  output_grid[i,j] = 3
                  changed_indices.append(j)

        elif i == 1:
            # Second row: change at most one gray pixel to green
            if gray_indices:
                output_grid[i, gray_indices[0]] = 3  # Change the first gray pixel

        elif i == 2:
            # Third row: Change up to three non-adjacent gray pixels
            changed_count = 0
            changed_indices = []
            for j in gray_indices:
                if changed_count < 3 and not any(abs(j-k) <=1 for k in changed_indices):
                     output_grid[i,j] = 3
                     changed_indices.append(j)
                     changed_count += 1
    return output_grid
```
