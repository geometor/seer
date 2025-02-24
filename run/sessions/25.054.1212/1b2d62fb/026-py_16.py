"""
The transformation identifies the column containing azure (8) pixels in the input grid. It then creates an output grid that includes two columns: one to the immediate left of the azure column, and the azure column itself. Only the white(0) and azure(8) are copied. Additionally, the output grid is cropped vertically, starting from the second row and ending at the second-to-last row of the input grid.
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
    selected_columns = [azure_column_index -1, azure_column_index]
    
    # Initialize output_grid as all white (0) with the correct dimensions.
    output_grid = np.zeros((input_grid.shape[0]-2, len(selected_columns)), dtype=int)

    row_offset = 1

    # Copy the selected columns with filtering
    for output_col_index, input_col_index in enumerate(selected_columns):
      if 0 <= input_col_index < input_grid.shape[1]:
        for i in range(row_offset, input_grid.shape[0]-1):
          if input_grid[i,input_col_index] == 8 or input_grid[i, input_col_index] == 0:
              output_grid[i-row_offset, output_col_index] = input_grid[i, input_col_index]

    return output_grid