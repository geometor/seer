# bd4472b8 • 008 • example_2 • investigate_coder

---
```python
"""
1. **Copy:** Copy the first two rows of the input grid directly to the output grid.
2. **Repeat:** Take the first row of the input grid.
3. **Fill Bottom:** Starting from the third row of the output grid, fill all subsequent rows by repeating the sequence of digits from the first row. Repeat the first row sequence four times in total to fill the output. The rows created are 4 * 2 = 8 rows.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid to avoid modifying the original
    output_grid = np.copy(input_grid)

    # Copy the first two rows
    # This is already done by initializing output_grid as a copy of input_grid

    # Get the first row
    first_row = input_grid[0]

    # Fill the rest of the output grid
    for i in range(2, len(output_grid), 2):  #start at row index 2 which is the third row
        output_grid[i] = first_row
        if i + 1 < len(output_grid):
            output_grid[i+1] = first_row
    return output_grid
```
