"""
The input grid is duplicated vertically. The rows of the input grid are then
copied to specific positions in the output grid according to a fixed mapping.
"""

import numpy as np

def transform(input_grid):
    # Create output_grid with double the height and same width, filled with zeros.
    output_grid = np.zeros((input_grid.shape[0] * 2, input_grid.shape[1]), dtype=int)

    # Row mapping (based on examples 2, 3, and 4)
    row_mapping = {
        0: [2, 3],
        1: [1, 4],
        2: [0, 5]
    }

    # Copy rows based on the mapping.
    for input_row_index, output_row_indices in row_mapping.items():
        if input_row_index < input_grid.shape[0]:  # Make sure the input row index is valid
          for output_row_index in output_row_indices:
              output_grid[output_row_index] = input_grid[input_row_index]

    return output_grid