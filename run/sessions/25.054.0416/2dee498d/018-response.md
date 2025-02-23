# 2dee498d • 018 • refine_coder

---
```python
"""
The input grid is transformed into the output grid by keeping every 4th column, starting with the first column. The output grid retains the height (number of rows) of the input grid. The values (colors) in the kept columns are preserved.  The *last* column is *always* included.
"""

import numpy as np

def transform(input_grid):
    # Convert input_grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Get the dimensions of the input grid.
    rows, cols = input_array.shape

    # Initialize an empty list to store the indices of the columns to be kept.
    kept_column_indices = []

    # Always keep the first column (index 0).
    kept_column_indices.append(0)

    # Iterate through the columns, keeping every 4th column, starting from the first.
    for i in range(4, cols, 4):  # Start at index 4, increment by 4
        kept_column_indices.append(i)

    # Always keep the last column.
    if cols > 0: # Handle the edge case where input has zero columns
        kept_column_indices.append(cols - 1)
    
    #remove any duplicates by converting to a set and back to list
    kept_column_indices = list(set(kept_column_indices))
    kept_column_indices.sort() #ensure correct order

    # Initialize an empty list to store the columns to be kept, based on collected indices
    kept_columns = []
    for i in kept_column_indices:
        kept_columns.append(input_array[:, i])


    # Stack the kept columns horizontally to form the output grid.
    output_array = np.stack(kept_columns, axis=1)

    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()

    return output_grid
```
