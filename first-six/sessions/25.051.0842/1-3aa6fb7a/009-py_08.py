"""
Find the largest blue square in the input grid. Move it down by two cells. If there's no blue square, don't change anything.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds all contiguous objects of the specified color in the grid.
    Returns a list of objects, where each object is a list of (row, col) coordinates.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects
def is_square(object_coords, grid):
    """Checks if an object (represented by its coordinates) is a square."""
    if not object_coords:
        return False

    # Find min and max row/col to determine bounding box
    min_row = min(r for r, _ in object_coords)
    max_row = max(r for r, _ in object_coords)
    min_col = min(c for _, c in object_coords)
    max_col = max(c for _, c in object_coords)

    # Check if bounding box dimensions are equal (square)
    width = max_col - min_col + 1
    height = max_row - min_row + 1

    if width != height:
        return False
    
    #Check that all the coordinates are present
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if (r,c) not in object_coords:
                return False
    
    return True
    

def get_object_size(object_coords):
     """Return the size of an object."""
     return len(object_coords)
    

def transform(input_grid):
    """
    Finds the largest blue square in the input grid and moves it down by two cells.
    """
    # initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # find all blue objects
    blue_objects = find_objects(input_grid, 1)  # 1 represents blue

    # find the largest blue square
    largest_blue_square = None
    largest_blue_square_size = 0
    
    for obj in blue_objects:
        if is_square(obj, input_grid):
            size = get_object_size(obj)
            if size > largest_blue_square_size:
                largest_blue_square = obj
                largest_blue_square_size = size

    # move the largest blue square down by two cells (if found)
    if largest_blue_square:
        # erase the square from its original position
        for r, c in largest_blue_square:
            output_grid[r, c] = 0  # 0 represents white (background)

        # draw the square at the new position
        for r, c in largest_blue_square:
            new_r = r + 2
            # make sure the new position is within the grid bounds
            if new_r < output_grid.shape[0]:
                output_grid[new_r, c] = 1  # 1 represents blue

    return output_grid