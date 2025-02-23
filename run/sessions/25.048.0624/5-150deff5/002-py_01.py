"""
The input grid contains a single object of color 5 (gray) on a background of color 0 (white).
The transformation replaces the gray object with two colors: 8 (azure) and 2 (red).
The "top arm" of the gray object is replaced with color 8, while the rest of the gray object is replaced with color 2.
The background remains unchanged.
"""

import numpy as np

def find_object(grid, color):
    """Finds the coordinates of all cells with the given color."""
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""

    # Initialize the output grid as a copy of the input grid.
    output_grid = input_grid.copy()

    # Find the object with color 5 (gray).
    object_5_coords = find_object(input_grid, 5)

    # If no object with color 5 is found, return the original grid.
    if object_5_coords.size == 0:
        return output_grid

    # Find the "top arm" of the object.
    # Starting from row 2 (index 1), identify the two leftmost cells of color 5.
    row2_indices = np.where(object_5_coords[:, 0] == 1)[0]
    if row2_indices.size > 0 :
        row2_coords = object_5_coords[row2_indices]
        row2_coords_sorted = row2_coords[row2_coords[:,1].argsort()]
        top_arm_coords = row2_coords_sorted[:2]

        #The cells in the following row, under these identified cells, that contains the color 5.
        next_row_coords = []
        for cell in top_arm_coords:
          next_row_cell_down = [cell[0]+1, cell[1]]
          indices = np.where((object_5_coords == next_row_cell_down).all(axis=1))[0]
          if indices.size > 0:
            next_row_coords.append(object_5_coords[indices[0]])
        top_arm_coords = np.vstack([top_arm_coords,next_row_coords])

        # change color of the top arm
        for coord in top_arm_coords:
                output_grid[coord[0], coord[1]] = 8

    # Replace the remaining cells of object 5 with color 2.
    for coord in object_5_coords:
        if output_grid[coord[0], coord[1]] == 5:
            output_grid[coord[0], coord[1]] = 2

    return output_grid