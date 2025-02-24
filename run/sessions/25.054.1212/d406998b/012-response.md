# d406998b • 012 • refine_coder

---
```python
"""
Transforms a grid by changing specific gray pixels to green based on their position and row, with row-specific rules.

- Row 1: Change gray pixels to green, skipping at least one gray pixel after each change.
- Row 2: Change at most one gray pixel to green, starting at index 0.
- Row 3: Change up to three non-adjacent gray pixels to green.
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
            # First row: change gray pixels, skipping at least one
            changed_indices = []
            skip_next = False
            for j in gray_indices:
                if skip_next:
                    skip_next = False
                    continue
                output_grid[i, j] = 3
                changed_indices.append(j)
                skip_next = True


        elif i == 1:
            # Second row: change at most one gray pixel to green
            if gray_indices:
                output_grid[i, gray_indices[0]] = 3  # Change the first gray pixel

        elif i == 2:
            # Third row: Change up to three non-adjacent gray pixels
            changed_count = 0
            changed_indices = []
            for j in gray_indices:
                if changed_count < 3 and not any(abs(j-k) <= 1 for k in changed_indices):
                     output_grid[i,j] = 3
                     changed_indices.append(j)
                     changed_count += 1
    return output_grid
```
