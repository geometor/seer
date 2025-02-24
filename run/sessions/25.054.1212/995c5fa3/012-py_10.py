"""
1.  **Identify White Columns:** Examine the input grid to identify all columns that contain at least one white (0) pixel.

2.  **Determine output for each index:** For each of the white columns, calculate the column index mod 5:
    *   If index mod 5 is 0, output color 4.
    *   If index mod 5 is 1, output color 2.
    *   If index mod 5 is 2, output color 2.
    *   If index mod 5 is 3, output color 8.
    *   If index mod 5 is 4, output color 3.

3.  **Create Output Grid:** Create a 3x3 output grid.

4.  **Populate Output:** For each unique value of `(index % 5)` when ordered lowest to highest, assign the corresponding color to a row in the output grid.
"""

import numpy as np

def get_white_column_indices(grid):
    """Identifies columns containing at least one white pixel."""
    white_columns = []
    for j in range(grid.shape[1]):
        if 0 in grid[:, j]:
            white_columns.append(j)
    return white_columns

def map_index_to_color(index):
    """Maps a column index to its corresponding output color."""
    mod_result = index % 5
    if mod_result == 0:
        return 4
    elif mod_result == 1 or mod_result == 2:
        return 2
    elif mod_result == 3:
        return 8
    elif mod_result == 4:
        return 3

def transform(input_grid):
    """Transforms input to output based on white column indices."""

    # Identify White Columns
    white_columns = get_white_column_indices(input_grid)

    # Determine output for each index.  Get *unique* and *sorted* mod values
    mod_values = sorted(list(set([col % 5 for col in white_columns])))

    # Create Output Grid
    output_grid = np.zeros((3, 3), dtype=int)

    # Populate Output, one row at a time
    for i, mod_val in enumerate(mod_values):
        if i < 3: # protect against writing out of bounds
            color = map_index_to_color(mod_val)
            output_grid[i, :] = color

    return output_grid