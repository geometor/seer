# 3-1e0a9b12 • 006 • Response

---

*text:*

```python
"""
Copies non-zero colored cells from the input grid to the last row of the output grid,
maintaining their relative horizontal order, except for objects in the third and fourth row which stays in place.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero colored cells to the last row,
    maintaining their order, except for objects in the third and fourth row which stay in place.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    
    # Get the height (number of rows) of the grid.
    height = input_grid.shape[0]
    
    # Copy the third and fourth rows from input to output.
    output_grid[height - 3, :] = input_grid[height-3, :]
    output_grid[height - 2, :] = input_grid[height-2, :]

    # Get non-zero elements from the input grid.
    non_zero_indices = np.where(input_grid != 0)
    non_zero_values = input_grid[non_zero_indices]

    # Create a list to store non-zero elements and their original column indices for sorting, filtering third and fourth rows.
    non_zero_elements = []
    for i in range(len(non_zero_values)):
      if non_zero_indices[0][i] != height - 3 and non_zero_indices[0][i] != height - 2: #filter elements from third and fourth row.
        non_zero_elements.append((non_zero_values[i], non_zero_indices[1][i]))

    # Sort the non-zero elements based on their original column index.
    non_zero_elements.sort(key=lambda x: x[1])

    # Place the sorted non-zero elements in the last row of the output grid.
    j=0
    for i in range (input_grid.shape[1]):
      if len(non_zero_elements) > j and input_grid[height-1,i] == 0:
        output_grid[height - 1, i] = non_zero_elements[j][0]
        j+=1

    return output_grid
```

