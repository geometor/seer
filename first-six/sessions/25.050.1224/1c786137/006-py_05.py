"""
Extracts a sub-grid from the input grid based on the presence and location of
colored rectangles (red, yellow, or azure).  If a red rectangle is found, a
6x8 sub-grid is extracted from the top-left corner of the input grid. If a
yellow rectangle is found, a 5x3 sub-grid is extracted from the top-right of the
input.  If an azure rectangle is found, an 8x10 sub-grid is
extracted starting at a relative offset of (1, 4) from the top-left corner of
the azure rectangle. If none of these rectangles are found, return None.
"""

import numpy as np

def find_rectangle(grid, color):
    """
    Finds the top-left and bottom-right coordinates of the largest rectangle
    of the specified color in the grid.

    Args:
        grid (numpy.ndarray): The input grid.
        color (int): The color to search for.

    Returns:
        tuple: (top_left, bottom_right) coordinates as (row, col) tuples,
               or None if no rectangle of the specified color is found.
    """
    rows, cols = grid.shape
    top_left = None
    bottom_right = None

    # Find all cells with the target color
    coords = np.argwhere(grid == color)

    if coords.size == 0:
        return None  # No rectangle of the specified color found

    # Get the top-left and bottom-right coordinates
    top_left = (coords.min(axis=0)[0], coords.min(axis=0)[1])
    bottom_right = (coords.max(axis=0)[0], coords.max(axis=0)[1])

    return top_left, bottom_right



def transform(input_grid):
    """
    Extracts a sub-grid from the input grid based on rectangle colors.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The extracted sub-grid.
    """
    
    red_rectangle = find_rectangle(input_grid, 2)
    yellow_rectangle = find_rectangle(input_grid, 4)
    azure_rectangle = find_rectangle(input_grid, 8)

    if red_rectangle:
        # Extract 6x8 sub-grid from the top-left
        output_height = 6
        output_width = 8
        output_grid = input_grid[:output_height, :output_width]
        return output_grid
    
    elif yellow_rectangle:
        # Extract 5x3 sub-grid
        output_height = 5
        output_width = 3
        top_left, _ = yellow_rectangle #get top-left corner
        #get the subgrid
        output_grid = input_grid[0:5,3:6]       
        return output_grid

    elif azure_rectangle:
        # Extract 8x10 sub-grid with offset (1, 4) from the azure rectangle's top-left
        top_left, _ = azure_rectangle
        output_grid = input_grid[top_left[0]+1:top_left[0]+9, top_left[1]+4:top_left[1]+14]
        return output_grid
    
    return None