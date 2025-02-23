"""
1.  **Identify the Target Object:** Locate the contiguous 3x3 block of green (value '3') pixels within the input grid.
2.  **Extract the green square:** Isolate the 3x3 green square, along with a one pixel thick white border on top and bottom edges of the square.
3. **Construct output:** Construct a 5 x 3 grid that represents the extracted region including the white border.
"""

import numpy as np

def find_green_square(grid):
    # Find the coordinates of all green pixels.
    green_coords = np.argwhere(grid == 3)

    # Check for a 3x3 contiguous block.
    for coord in green_coords:
        row, col = coord
        # Check if a 3x3 block exists starting at this coordinate.
        if row + 2 < grid.shape[0] and col + 2 < grid.shape[1]:
            if np.all(grid[row:row+3, col:col+3] == 3):
                return row, col #return top-left corner
    return None  # Return None if no 3x3 green square is found

def transform(input_grid):
    # Find the top-left corner of the 3x3 green square.
    top_left = find_green_square(input_grid)

    if top_left is None:
        #handle a case with no green square (we will not test this yet)
        return np.zeros((5,3), dtype=int)
      
    row, col = top_left

    # construct the 5 x 3 output
    output_grid = np.zeros((5,3),dtype=int)

    #fill in the green square
    output_grid[1:4,:] = 3
    
    return output_grid