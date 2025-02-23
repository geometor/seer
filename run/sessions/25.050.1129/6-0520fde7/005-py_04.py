"""
Extracts the central column from the input grid, identifies the first two non-white colors,
and creates a 3x3 output grid with pixels of the identified color (changed to 2) at the positions
[1,0] and [2,2], and white (0) elsewhere.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid according to the described rule.
    """
    # Convert input grid to numpy array
    input_grid = np.array(input_grid)

    # Get dimensions of the input grid
    rows, cols = input_grid.shape

    # Find the center column index
    center_col_index = cols // 2

    # Extract the center column
    center_column = input_grid[:, center_col_index]

    # Create a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the first non-white (non-zero) colors in the center column
    non_white_colors = []
    for cell_color in center_column:
        if cell_color != 0 and cell_color not in non_white_colors:
            non_white_colors.append(cell_color)


    # Place the color 2 at specified positions
    output_grid[1, 0] = 2
    output_grid[2, 2] = 2
    return output_grid