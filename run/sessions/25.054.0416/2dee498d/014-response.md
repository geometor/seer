# 2dee498d • 014 • example_3 • investigate_coder

---
```python
"""
The input grid is transformed into the output grid by removing every other column, starting with the second column. The output grid retains the height of the input grid, and the color/values are preserved in the remaining columns.
"""

import numpy as np

def transform(input_grid):
    # Convert input_grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Get the dimensions of the input grid.
    rows, cols = input_array.shape

    # Initialize an empty list to store the columns to be kept.
    kept_columns = []

    # Iterate through the columns, keeping only those at odd indices (starting from 1, which corresponds to index 0).
    for i in range(cols):
        if (i + 1) % 2 != 0:  # Keep columns 1, 3, 5, etc. (odd-numbered columns).
            kept_columns.append(input_array[:, i])

    # Stack the kept columns horizontally to form the output grid.
    output_array = np.stack(kept_columns, axis=1)

    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()

    return output_grid
```
