import numpy as np

def find_objects(grid, color):
    # Find coordinates of all cells with the specified color.
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the objects of color 2, 1 and 6.  These are all single cells.
    objects_2 = find_objects(input_grid, 2)
    objects_1 = find_objects(input_grid, 1)
    objects_6 = find_objects(input_grid, 6)

    # Apply rules for object of color 2.
    for obj_2 in objects_2:
        row, col = obj_2
        if row - 1 >= 0:
            if col - 1 >= 0:
                output_grid[row - 1, col - 1] = 4
            if col + 1 < output_grid.shape[1]:
                output_grid[row - 1, col + 1] = 4
        if row + 1 < output_grid.shape[0]:
            if col - 1 >= 0:
                output_grid[row + 1, col - 1] = 4
            if col + 1 < output_grid.shape[1]:
                output_grid[row + 1, col + 1] = 4

    # Apply rules for object of color 1.
    for obj_1 in objects_1:
        row, col = obj_1
        # Place 7 above
        if row - 1 >= 0:
            output_grid[row - 1, col] = 7
        
        # Place 7 on the left and right, and below
        if col - 1 >= 0:
           output_grid[row,col-1] = 7
        if col + 1 < output_grid.shape[1]:
            output_grid[row,col+1] = 7
        if row + 1 < output_grid.shape[0]:
            output_grid[row+1,col] = 7
            if col - 1 >= 0:
                output_grid[row + 1, col - 1] = 7
            if col + 1 < output_grid.shape[1]:
                output_grid[row + 1, col + 1] = 7
        if row -1 >= 0:
             if col - 1 >= 0:
                output_grid[row - 1, col - 1] = 7
             if col + 1 < output_grid.shape[1]:
                output_grid[row - 1, col + 1] = 7
    return output_grid