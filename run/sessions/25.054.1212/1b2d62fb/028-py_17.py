"""
1.  **Find Azure:** Locate the column in the input grid that contains azure (color 8) pixels. Note its index.
2.  **Select Columns:** Select three columns from the input grid:
    *   The column immediately to the *left* of the azure column (if it exists). If the azure column is the first column, do not include a left-adjacent column.
    *   The azure column itself.
    *   The column immediately to the *right* of the azure column (if it exists). If the azure column is the last column, do not include a right-adjacent column.
3. **Create Output:** Create an output grid with a number of rows the same as the input, and three columns wide
4.  **Copy Pixels:** Copy all the pixels from the selected columns to the new grid in the same order as they are selected.
"""

import numpy as np

def find_azure_column(grid):
    """Finds the column index containing azure (8) pixels."""
    for j in range(grid.shape[1]):
        for i in range(grid.shape[0]):
            if grid[i, j] == 8:
                return j
    return -1  # Should not happen in well-formed inputs

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    # Find the azure column
    azure_column_index = find_azure_column(input_grid)

    # Determine relevant columns
    selected_columns = []
    
    left_adjacent_index = azure_column_index - 1
    if left_adjacent_index >= 0:
        selected_columns.append(left_adjacent_index)

    selected_columns.append(azure_column_index)

    right_adjacent_index = azure_column_index + 1
    if right_adjacent_index < input_grid.shape[1]:
        selected_columns.append(right_adjacent_index)
    
    # Initialize output_grid with the correct dimensions.
    output_grid = np.zeros((input_grid.shape[0], len(selected_columns)), dtype=int)

    # Copy the selected columns
    for output_col_index, input_col_index in enumerate(selected_columns):
        for i in range(input_grid.shape[0]):
            output_grid[i, output_col_index] = input_grid[i, input_col_index]

    return output_grid