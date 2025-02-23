"""
1.  **Identify Static Objects:** The yellow '4' pixels form a static object and do not change position.
2.  **Identify Moving Object 9:** The maroon '9' pixel is a moving object
3.  **Identify Coupled Object 7 and 8:** The orange '7' and azure '8' form a coupled object.
4.  **Move Object 9**: Move object 9 to the last row of the grid, maintaining the column.
5.  **Move Coupled Object 7 and 8**: move the couple object to the initial row index of Object 9.
"""

import numpy as np

def find_object(grid, color):
    # find the coordinates of the object with specified color
    coords = np.argwhere(grid == color)
    return coords

def move_object(grid, coords, new_row, new_col=None):
    #Create a copy to modify
    new_grid = np.copy(grid)

    # Check if it's a single coordinate or multiple
    if len(coords) == 1:
        row, col = coords[0]
         # clear original position
        new_grid[row, col] = 0
        if new_col is None:
            new_col = col
        # Set new position
        new_grid[new_row, new_col] = grid[row, col]
    else:  # Handle multiple coordinates (coupled object)
        # find the shift in row and column to be applied
        row_shift = new_row - coords[0][0]
        for coord in coords:
            row, col = coord
            new_grid[row,col] = 0
        
        for coord in coords:
            row, col = coord
            new_grid[row + row_shift, col] = grid[row,col]

    return new_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find static object '4'
    static_object_coords = find_object(output_grid, 4)

    # Find moving object '9'
    moving_object_coords = find_object(output_grid, 9)

    # Find coupled object '7' and '8'
    coupled_object_7_coords = find_object(output_grid, 7)
    coupled_object_8_coords = find_object(output_grid, 8)
    coupled_object_coords = np.concatenate((coupled_object_7_coords, coupled_object_8_coords), axis=0)

    # Move object '9' to the last row
    if len(moving_object_coords) > 0:
        output_grid = move_object(output_grid, moving_object_coords, output_grid.shape[0] - 1)

    # Move coupled object '7' and '8' to the row of moving object 9 initial position
    if len(moving_object_coords) > 0 and len(coupled_object_coords) > 0 :
        initial_row_9 = moving_object_coords[0][0]
        output_grid = move_object(output_grid, coupled_object_coords, initial_row_9)


    return output_grid