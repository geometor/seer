"""
This transformation identifies azure objects and adds a blue pixel inside of them. The position is at the corner pixel of L shaped objects.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds all contiguous objects of a given color in the grid.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return

        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def is_l_shape(object_pixels):
    """
    Checks if a set of pixels forms an L-shape (size 3).
    Returns the corner coordinates if it is, otherwise returns None.
    """
    if len(object_pixels) != 3:
        return None

    # Convert list of tuples to numpy array for easier manipulation
    pixels = np.array(object_pixels)
    
    #find min and max of rows and cols
    min_row, min_col = np.min(pixels, axis=0)
    max_row, max_col = np.max(pixels, axis=0)
    
    # Calculate differences in row and col coordinates
    row_diffs = pixels[:, 0] - min_row
    col_diffs = pixels[:, 1] - min_col

    # Check for the three possible L-shape configurations:
    if (np.array_equal(row_diffs, [0, 0, 1]) and np.array_equal(col_diffs, [0, 1, 0])) or \
       (np.array_equal(row_diffs, [0, 1, 1]) and np.array_equal(col_diffs, [0, 0, 1])) or \
       (np.array_equal(row_diffs, [0, 1, 0]) and np.array_equal(col_diffs, [0, 0, 1]))or \
       (np.array_equal(row_diffs, [0, 0, 1]) and np.array_equal(col_diffs, [0, 1, 1])):
       
       #find corner using min and max values
       if (np.array_equal(row_diffs, [0, 0, 1]) and np.array_equal(col_diffs, [0, 1, 0])):
          corner = (max_row,min_col)
       elif (np.array_equal(row_diffs, [0, 1, 1]) and np.array_equal(col_diffs, [0, 0, 1])):
          corner = (min_row,min_col)
       elif (np.array_equal(row_diffs, [0, 1, 0]) and np.array_equal(col_diffs, [0, 0, 1])):
          corner = (min_row, max_col)
       else:
          corner = (max_row,max_col)
       return corner
    else:
        return None


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)  # 8 is for azure

    # Iterate through each azure object
    for obj in azure_objects:
        # Check if it's an L-shape and get the corner
        corner = is_l_shape(obj)
        if corner:
            # Determine insertion point based on L-shape orientation
            row, col = corner
            output_grid[row,col] = 1 #set the corner

    return output_grid