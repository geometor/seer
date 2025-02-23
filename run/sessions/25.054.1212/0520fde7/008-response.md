# 0520fde7 • 008 • example_2 • investigate_coder

---
```python
"""
1. **Focus Column:** Identify the column in the input grid that contains the value 5 (grey).
2.  **Extraction:** Extract the values from this grey column.
3. **Color Mapping:** Create a new 3x3 grid. For each value extracted in step 2:

    *   If the value is 1 (blue), place a 0 (white) in the corresponding position of the output grid.
    *   If the value is 5 (grey), place a 2 (red) in the corresponding position of the output grid.
    * If the value is 0, leave the default 0.
4. Output the new 3x3 grid
"""

import numpy as np

def find_column_with_value(grid, value):
    # Find the column index where value exists
    for j in range(grid.shape[1]):
        for i in range(grid.shape[0]):
            if grid[i, j] == value:
                return j
    return -1

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the column with the value 5
    column_index = find_column_with_value(input_grid, 5)

    if column_index == -1:
        return output_grid # Return all zeros matrix if no 5

    # Extract values from the column
    extracted_values = input_grid[:, column_index]

    # Map and fill the output grid
    for i, value in enumerate(extracted_values):
        if value == 1:
            output_grid[i, 1] = 0  # Map blue (1) to white (0)
        elif value == 5:
            output_grid[i, 1] = 2  # Map grey (5) to red (2)

    return output_grid
```
