"""
1.  **Identify all colors present in the input grid.**
2.  **Identify the color of the middle row of the grid.**
3. **Determine the "retained color":**
   *   If the middle row is all one color the retained color is that color.
   *  If the middle row is *not* uniform:
       * The retained color is the color which makes up the outline of the output.
4. **Construct the output grid:** Create a new grid of the same dimensions as the input grid.
5. **Populate the output grid:**
    *  Fill all pixels in the output that match the retained color from the Input.
   *   Fill any remaining pixels with the color '5' (gray).
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

def get_retained_color(grid):
    """
    Determines the retained color based on the middle row and grid outline.
    """
    middle_row_color = get_middle_row_color(grid)
    if middle_row_color is not None:
        return middle_row_color # If uniform, return the middle row's color.
    else:
        # check for outline.  If the middle row isn't uniform
        # Find the color that forms the 'outline' (top and bottom rows in this 3x3 case)
        top_row_color = grid[0, 0]
        bottom_row_color = grid[-1,0]

        if np.all(grid[0, :] == top_row_color) and np.all(grid[-1, :] == top_row_color):
             return top_row_color #return top if top and bottom are the same

        # if top_row_color == bottom_row_color:
        #     return top_row_color

    return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.full(input_grid.shape, 5, dtype=int)

    # find retained color
    retained_color = get_retained_color(input_grid)

    # change output pixels
    if retained_color is not None:
        for i in range(input_grid.shape[0]):
            for j in range(input_grid.shape[1]):
                if input_grid[i,j] == retained_color:
                    output_grid[i,j] = retained_color

    return output_grid