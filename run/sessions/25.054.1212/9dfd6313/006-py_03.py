"""
Transforms the input grid by rearranging the non-zero values in each column of the input grid into the output columns.
The non-zero input values are assigned sequentially to output columns, starting with the output column corresponding to the input column index.
If an output column already has a non-zero value at a position, the input value is placed in the next available column, wrapping around to the beginning if necessary.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [[0] * cols for _ in range(rows)]

    # Iterate through each input column
    for j in range(cols):
        input_column_values = [input_grid[i][j] for i in range(rows)]
        non_zero_values = [val for val in input_column_values if val != 0]

        output_col_index = j  # Start with the corresponding output column
        row_index = 0
        for val in non_zero_values:
          
            placed = False
            while not placed:
                if row_index >= rows:
                    row_index = 0
                    output_col_index = (output_col_index + 1) % cols
                if output_grid[row_index][output_col_index] == 0:
                    output_grid[row_index][output_col_index] = val
                    placed = True
                
                row_index+=1

    return output_grid