import numpy as np

def get_object(grid, color):
    """
    Finds the contiguous region of a specified color.

    Returns a mask where object pixels are True, and the background is False.
    """
    mask = (grid == color)
    return mask

def transform(input_grid):
    """
    Transforms the input grid by recoloring a gray (5) object with azure (8) and red (2) sub-shapes,
    while preserving the background (0).  Azure is applied to the right-most portions of the gray object.
    """
    output_grid = np.copy(input_grid)
    gray_mask = get_object(input_grid, 5)
    coords = np.argwhere(gray_mask)

    # Create a dictionary to store the right-most column index for each row within the gray object.
    rightmost_cols = {}
    for r, c in coords:
        if r not in rightmost_cols or c > rightmost_cols[r]:
            rightmost_cols[r] = c

    # Apply color changes based on the right-most rule.
    for r, c in coords:
        if c == rightmost_cols.get(r, -1) :
           output_grid[r,c] = 8 #rightmost
        elif c == rightmost_cols.get(r, -1) - 1 and output_grid[r,c+1] == 8:
           output_grid[r,c] = 8 # second rightmost if contiguous
        elif input_grid[r, c] == 5:
            output_grid[r, c] = 2  # Red for the remaining parts


    return output_grid