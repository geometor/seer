"""
Transformation Rule:
1. Locate all occurrences of the L-shaped object of color 8 (azure).
2. For each L-shaped object:
   a. If the object is on the left side of the grid, insert a single cell of color 1 (blue) to its immediate right.
   b. If the object is on the right side of the grid, insert a single cell of color 1 (blue) to its immediate left.
"""

import numpy as np

def find_l_shape_objects(grid, color):
    """
    Finds L-shaped objects of a specified color in the grid.
    Returns a list of (row, col) tuples representing the "corner" of the L-shape.
    """
    objects = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for all 4 possible L-shape orientations
                if grid[r + 1, c] == color and grid[r, c + 1] == color:  # Standard L
                    objects.append((r, c))
                elif grid[r, c + 1] == color and grid[r + 1, c + 1] == color:  # Rotated 90
                    objects.append((r, c))
                elif grid[r + 1, c] == color and grid[r + 1, c + 1] == color:  # Rotated 180
                    objects.append((r, c))
                elif grid[r, c + 1] == color and grid[r - 1, c + 1] == color: #Upside down
                    objects.append((r,c))

    return objects

def is_object_on_left(grid, obj_pos):
    """
    Checks if the object is on the left side of the grid.
    """
    _, cols = grid.shape
    return obj_pos[1] < cols / 2

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    objects = find_l_shape_objects(output_grid, 8)
    rows, cols = output_grid.shape

    for obj_pos in objects:
        insert_row, insert_col = obj_pos

        if is_object_on_left(output_grid, obj_pos):
            # Check L-shape orientation and adjust insertion point
            if insert_col + 1 < cols and output_grid[insert_row, insert_col + 1] == 8:
                insert_col += 2  # Insert to the right of the horizontal part
            else:
                insert_col += 1   # standard case

        else: # on the right
             # Check L-shape orientation and adjust insertion point

            if insert_col + 1 < cols and output_grid[insert_row, insert_col + 1] == 8:
                insert_col = insert_col #right side, standard
            elif insert_row + 1 < rows and output_grid[insert_row+1,insert_col] == 8:
                insert_col -= 1 #right side, standard
            else:
                insert_col -= 1 #right side, 90 degree rotation
        # Ensure insertion is within bounds
        if 0 <= insert_row < rows and 0 <= insert_col < cols:
            output_grid[insert_row, insert_col] = 1

    return output_grid