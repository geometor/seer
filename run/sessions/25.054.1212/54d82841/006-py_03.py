"""
The transformation identifies all white (0) pixels in the last row of the input grid that are located at the 3rd position, and at the 3rd from last position, and changes their color to yellow (4). All other pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Get the index of the last row.
    last_row_index = input_grid.shape[0] - 1

    # Get the width of the grid
    width = input_grid.shape[1]

    # Define the column indices to check, ensuring they are within bounds.
    col_indices = []
    if width >= 3:
        col_indices.append(2)  # 3rd column (index 2)
    if width >= 3:
        col_indices.append(width - 3)  # 3rd from last column

    # Change the color of the specified pixels to yellow (4) if they are white (0).
    for col_index in col_indices:
        if output_grid[last_row_index, col_index] == 0:
            output_grid[last_row_index, col_index] = 4

    return output_grid