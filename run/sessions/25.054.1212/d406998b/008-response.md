# d406998b • 008 • example_2 • investigate_coder

---
```python
"""
Transforms a grid by changing specific gray pixels to green based on their position.

The transformation follows these rules:
- In the first row, change the gray pixel to green in the second and fourth columns.
- In the second row, change the gray pixel to green in the eighth column.
- In the third row, change the gray pixel to green in the sixth, tenth, and twelfth columns.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each row
    for i in range(rows):
        # Apply transformation rules based on row index
        if i == 0:
            # First row: change gray to green in columns 2 and 4 (index 1 and 3)
            for j in [1, 3]:
                if j < cols and output_grid[i, j] == 5:
                    output_grid[i, j] = 3
        elif i == 1:
            # Second row: change gray to green in column 8 (index 7)
            j = 7
            if j < cols and output_grid[i, j] == 5:
                output_grid[i, j] = 3
        elif i == 2:
            # Third row: change gray to green in columns 6, 10, and 12 (index 5, 9, 11)
            for j in [5, 9, 11]:
                if j < cols and output_grid[i, j] == 5:
                    output_grid[i, j] = 3

    return output_grid
```
