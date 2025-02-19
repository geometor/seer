"""
The positions of red cells are moved based on the existence of yellow cells vertically. If there are any yellow blocks in the same column, the red cell will be placed on top of it. If not, then it is placed on row 7.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all cells with the given color
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None  # Return None if no object of the specified color is found
    return coords

def transform(input_grid):
    """
    Transforms the input grid based on the observed rule.
    The positions of red cells are determined based on the positions of the yellow
    square.
    """
    output_grid = np.copy(input_grid)
    red_coords_input = find_object(input_grid, 2)
    yellow_coords_output = find_object(output_grid, 4)
    yellow_columns = []

    if yellow_coords_output is not None:
      yellow_columns = np.unique(yellow_coords_output[:, 1])

    if red_coords_input is not None:
      for coord in red_coords_input:
        x = coord[1]
        output_grid[coord[0]][coord[1]] = 1
        has_yellow = False
        if yellow_coords_output is not None:
            for y_coord in yellow_coords_output:
                if y_coord[1] == x:
                    #find topmost yellow block
                    top_yellow = output_grid.shape[0]
                    for yel_y in yellow_columns:
                      if yel_y == x:
                        for k in range(output_grid.shape[0]):
                          if output_grid[k][yel_y] == 4:
                            top_yellow = k
                            break
                        break

                    output_grid[top_yellow-1][x] = 2
                    has_yellow= True
                    break
        if not has_yellow:
            output_grid[6][x] = 2

    return output_grid