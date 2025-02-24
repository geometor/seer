# 1b2d62fb • 030 • refine_coder

---
```python
"""
1.  **Find Azure Column:** Locate the column in the input grid containing azure (color 8) pixels. Note the column index.
2.  **Select Columns:** Identify up to three columns:
    *   The column immediately to the left of the azure column (if it exists).
    *   The azure column itself.
    *   The column immediately to the right of the azure column (if it exists).
3.  **Create Output Grid:** Create an output grid with the same number of rows as the input grid, and with a number of columns the same as the number of `selected_columns`.
4.  **Transform Pixels in Selected Columns**
    * Set all pixels in the selected columns to black (0)
    * For each azure (8) pixel in the original input's azure column, place an azure (8) pixel in the same row in the output grid's middle column.
    * Additionally, place azure pixels in the rows *immediately above and below* the original azure pixel's row in the output grid's middle column, as long as the row is within range. This means the 8 is duplicated above and below its original position.
"""

import numpy as np

def find_azure_column(grid):
    """Finds the column index containing azure (8) pixels."""
    for j in range(grid.shape[1]):
        if 8 in grid[:, j]:
            return j
    return -1

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    azure_column_index = find_azure_column(input_grid)
    rows = input_grid.shape[0]

    # Determine relevant columns
    selected_columns = []
    if azure_column_index - 1 >= 0:
        selected_columns.append(azure_column_index - 1)
    selected_columns.append(azure_column_index)
    if azure_column_index + 1 < input_grid.shape[1]:
        selected_columns.append(azure_column_index + 1)

    # Initialize output_grid
    output_grid = np.zeros((rows, len(selected_columns)), dtype=int)

    # Find the rows where the azure pixel is located in the input
    azure_rows = np.where(input_grid[:, azure_column_index] == 8)[0]

    # Middle column index of the *output* grid
    output_middle_column = len(selected_columns) // 2

    # Place the azure pixels in the center column
    for row in azure_rows:
        output_grid[row, output_middle_column] = 8

        if row - 1 >= 0:
            output_grid[row - 1, output_middle_column] = 8
        if row + 1 < rows:
            output_grid[row + 1, output_middle_column] = 8

    return output_grid
```
