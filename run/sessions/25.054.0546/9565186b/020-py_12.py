"""
1. **Identify the Retained Color:** Examine the input grid and find the color that makes up the entire middle row. This is the "retained color". In this example the middle row is yellow, represented by the digit '4'.

2.  **Change other colors:** all other digits in the grid will be replaced by the digit '5'.

3.  **Construct the Output Grid:** Create a new 3x3 grid. Fill any cell that was occupied by another color, to '5'. Transfer the middle row color to the new grid.
"""

import numpy as np

def get_middle_row_color(grid):
    """Helper function to extract the color of the middle row."""
    middle_row_index = grid.shape[0] // 2
    middle_row = grid[middle_row_index, :]
    # Check if all elements in the middle row are the same
    if np.all(middle_row == middle_row[0]):
        return middle_row[0]
    else:
        return None  # Or raise an exception, depending on desired behavior


def transform(input_grid):
    # initialize output_grid
    output_grid = np.full(input_grid.shape, 5, dtype=int)

    # find retained color
    retained_color = get_middle_row_color(input_grid)

    # change output pixels 
    if retained_color is not None:
      middle_row_index = input_grid.shape[0] // 2
      output_grid[middle_row_index,:] = retained_color

    return output_grid