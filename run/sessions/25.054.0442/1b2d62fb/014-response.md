# 1b2d62fb • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify the Target Column:** Find the column in the input grid that is entirely filled with blue (1) pixels.
2.  **Extract Columns:** Extract the target column, one to the right of the blue pixels, and one to the left of the blue pixels.
3.  **Construct Output:** Create a new grid using the extracted columns.
4.  Change color. Change all of the blue (1) pixels to azure (8) pixels.
5.  Maintain the other non-blue pixels with original color and location relative to the central column.
"""

import numpy as np

def find_blue_column(grid):
    # Iterate through each column
    for j in range(grid.shape[1]):
        # Check if all elements in the column are equal to 1 (blue)
        if np.all(grid[:, j] == 1):
            return j  # Return the index of the blue column
    return -1  # Return -1 if no such column is found

def transform(input_grid):
    # Find the index of the blue column
    blue_column_index = find_blue_column(input_grid)

    # Handle the case where no blue column is found (should not happen, per task instructions, but still good to check.)
    if blue_column_index == -1:
        return None # Or raise an exception, or return a copy of the input, or whatever is appropriate

    # Determine the range of columns to extract.

    left_column_index = blue_column_index - 1
    right_column_index = blue_column_index + 1

    #check column bounds
    if left_column_index < 0:
        left_column_index = 0
    if right_column_index > input_grid.shape[1]-1:
        right_column_index = input_grid.shape[1]-1

    # Extract columns including bounds check.
    extracted_columns = []
    if left_column_index >= 0:
      extracted_columns.append(input_grid[:, left_column_index])
    extracted_columns.append(input_grid[:,blue_column_index])

    if right_column_index < input_grid.shape[1]:
        extracted_columns.append(input_grid[:, right_column_index])

    # Create the output grid
    output_grid = np.stack(extracted_columns, axis=1)

    #change blue to azure
    output_grid[output_grid == 1] = 8

    return output_grid
```
