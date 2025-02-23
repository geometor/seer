# 2dee498d • 004 • example_2 - CODE

---
```python
"""
The transformation rule can be described as follows:

1. **Identify Columns:** Examine the input grid, which is 4x12.
2. **Select Columns:** Take every fourth column of the input grid starting from the first column. That is, consider column 0, column 4, and column 8.
3. Remove other columns.
4. **Construct Output:** Arrange the content of these selected columns to construct the output grid of size 4x4, preserving the original order of rows.

In other words, the output grid is formed by sampling specific columns from the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by selecting every fourth column starting from the first.
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Get the dimensions of the input grid.
    rows, cols = input_array.shape

    # Initialize an empty list to store the selected columns.
    selected_columns = []

    # Iterate through the columns, selecting every fourth column starting from 0.
    for i in range(0, cols, 4):
        selected_columns.append(input_array[:, i])

    # Stack the selected columns horizontally to form the output grid.
    output_grid = np.stack(selected_columns, axis=1)
    
    return output_grid.tolist()
```

