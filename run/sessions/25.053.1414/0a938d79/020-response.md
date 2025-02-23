# 0a938d79 • 020 • example_4 - CODE

---
```python
"""
The transformation rule is as follows:
1. Identify rows that contain a non-zero value.
2. Replicate these rows a certain number of times (4 times in this case).
3. Stack them together to create the output grid.
"""

import numpy as np

def get_non_zero_rows(grid):
    # Find the indices of rows that contain non-zero values
    non_zero_rows = []
    for i, row in enumerate(grid):
        if any(row):  # Check if any element in the row is non-zero
            non_zero_rows.append(i)
    return non_zero_rows

def replicate_and_stack(grid, row_indices):
    # Create a list to hold the new rows
    new_rows = []
    num_replications = 4

    # For each row index, get the row, replicate it, and add to new_rows
    for row_index in row_indices:
      row = grid[row_index].copy() # get a copy of the row
      color = 0
      for c in row:
          if c != 0:
              color = c
              break
      
      row.fill(color)

      for _ in range(num_replications):
            new_rows.append(row.copy())
            
    return new_rows

def transform(input_grid):
    # Convert input grid to a NumPy array
    input_grid = np.array(input_grid)

    # initialize output grid as same size and all zeros
    output_grid = np.zeros_like(input_grid)

    # Find row indices of non zero rows
    non_zero_row_indices = get_non_zero_rows(input_grid)
    
    # replicate the non zero rows and make stacks
    replicated_rows = replicate_and_stack(input_grid, non_zero_row_indices)
    
    # fill the output grid with the replicated rows, repeat as necessary
    row_count = 0;
    for i in range(len(output_grid)):
        if (len(replicated_rows) > 0):
          output_grid[i] = replicated_rows[row_count % len(replicated_rows)]
          row_count += 1
    

    return output_grid
```
