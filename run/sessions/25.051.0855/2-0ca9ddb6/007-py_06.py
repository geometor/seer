import numpy as np

def find_objects(grid, color):
    # Find coordinates of all cells with the specified color.
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    # Initialize output grid as all zeros.
    output_grid = np.zeros_like(input_grid)

    # Preserve single cells of color 8, 2, 1 and 6.
    for color in [8, 2, 1, 6]:
        objects = find_objects(input_grid, color)
        for obj in objects:
            row, col = obj
            output_grid[row, col] = color

    # Find the objects of color 2 and 1.
    objects_2 = find_objects(input_grid, 2)
    objects_1 = find_objects(input_grid, 1)

    # Apply rules for object of color 2.
    for obj_2 in objects_2:
        row, col = obj_2
        # Place color 4 cells above and below, to the left and right.
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
        # Place color 7 above.
        if row - 1 >= 0:
            output_grid[row - 1, col] = 7
        # Place color 7 in the 3x3 neighborhood, excluding the center.
        for i in range(max(0, row - 1), min(row + 2, output_grid.shape[0])):
            for j in range(max(0, col - 1), min(col + 2, output_grid.shape[1])):
                if (i, j) != (row, col):  # Exclude the center cell itself.
                    output_grid[i, j] = 7

    return output_grid