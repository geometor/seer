"""
1. Identify the operative color: For each input grid, find the color that appears in the top row and also in other rows. This is the "operative color".
2. Remove operative color except on top row: Iterate through the entire grid. If a pixel's color matches the operative color *and* the pixel is *not* in the top row (row index 0), change the pixel's color to black (0).
3. Leave other pixels unchanged: Pixels that do not match the operative color, or that *are* on the top row, should remain their original color.
"""

import numpy as np

def get_operative_color(grid):
    """
    Finds the color that appears in the top row and also in other rows.
    """
    top_row_colors = set(grid[0])
    other_rows_colors = set()
    for i in range(1, grid.shape[0]):
        other_rows_colors.update(grid[i])
    operative_colors = top_row_colors.intersection(other_rows_colors)
    # Handle edge case: it is possible no operative color is found.
    # This occurs on the test input, but not the training set.
    if len(operative_colors) > 0:
      return operative_colors.pop() # return one of the operative colors
    else:
      return None

def transform(input_grid):
    """
    Transforms the input grid by removing all pixels of the operative color 
    except for those present on the top row (row index 0).
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Identify the operative color
    operative_color = get_operative_color(input_grid)

    if operative_color is None:
      return output_grid

    # Iterate through the input grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Check if the pixel is the operative color.
            if output_grid[i, j] == operative_color:
                # Check if the pixel is NOT on the top row (row index 0).
                if i != 0:
                    # Change the pixel to black (value 0).
                    output_grid[i, j] = 0

    return output_grid