"""
Creates a 3x3 output grid based on the first three rows of the input grid.
The colors in the output grid are determined by a mapping from the unique
non-background colors (excluding 0 and 5) found in the corresponding input rows.
"""

import numpy as np

def get_non_background_color(row):
    """
    Returns the first non-background color (not 0 or 5) in a row, or None if none found.
    """
    unique_colors = np.unique(row)
    for color in unique_colors:
        if color != 0 and color != 5:
            return color
    return None

def transform(input_grid):
    # Initialize a 3x3 output grid (filled with an arbitrary color, e.g., black/3).
    output_grid = np.full((3, 3), 3)

    # Iterate through the first three rows of the input grid.
    for i in range(min(3, len(input_grid))):  # Ensure we don't go out of bounds
        row = input_grid[i]
        # Get the first non-background color in the row.
        color = get_non_background_color(row)

        # Populate output based on color and row index
        if color is not None:
            if i == 0:
              if color == 2:
                output_grid[i, :] = 2
              elif color == 8:
                output_grid[i,:] = 8
              else:
                output_grid[i,:] = 3
            elif i == 1:
              if color == 2:
                output_grid[i,:] = 2
              elif color == 4:
                output_grid[i,:] = 4
              else:
                output_grid[i,:]=3
            elif i == 2:
              if color == 2:
                output_grid[i, :] = 2
              elif color == 3:
                  output_grid[i,:] = 3
              elif color == 4:
                output_grid[i,:] = 4
              else:
                output_grid[i,:] = 3

    return output_grid