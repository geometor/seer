# AboveBelow10 • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify the diagonal:** Locate the existing diagonal line of yellow (4) pixels extending from the top-left corner downwards.
2.  **Fill below the diagonal:** For each row, starting from the top, change all pixels to the left of the yellow diagonal pixel in that row to yellow (4). Stop when reaching the bottom of the grid or end of a row. The result is a filled triangle.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid by filling the area below the diagonal with yellow."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each row
    for i in range(rows):
        # Find the index of the yellow pixel in the current row
        yellow_index = -1
        for j in range(cols):
            if output_grid[i, j] == 4:
                yellow_index = j
                break  # Stop searching after finding the first yellow pixel

        # Fill pixels to the left of the yellow pixel with yellow
        if yellow_index != -1:
            for j in range(yellow_index):
                output_grid[i, j] = 4

    return output_grid
```

